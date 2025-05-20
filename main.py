import sys
import os
import time
import ctypes
from ctypes import wintypes

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QScrollArea, QGroupBox, QComboBox, QToolTip
)
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt, QSize, QEvent, QPoint

from commands import COMMANDS

# Optional Win32 imports
try:
    import win32gui
    import win32con
except ImportError:
    win32gui = win32con = None

# ───────── Constants ────────────────────────────────────────────────────────────

ICON_SIZE        = 64
GAP              = 1
CMD_WIDTH        = 360
BTN_H            = 26
PROMPT_WIDTH     = 240
PROMPT_HEIGHT    = 100

# Win32 extended window styles
GWL_EXSTYLE      = -20
WS_EX_NOACTIVATE = 0x08000000
WS_EX_TOOLWINDOW = 0x00000080

# Qt flags
OVERLAY_FLAGS    = Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool

# Virtual-key and flags
VK_RETURN        = 0x0D
VK_SHIFT         = 0x10

KEYEVENTF_KEYUP  = 0x0002
KEYEVENTF_UNICODE = 0x0004
VK_OEM_PERIOD   = 0xBE
MAPVK_VK_TO_VSC  = 0

# Category display names
CATEGORY_DISPLAY = {
    "bloodlegacy":   "Bloodlegacy Commands",
    "classes":       "Class Commands",
    "familiars":     "Familiar Commands",
    "leveling":      "Level Commands",
    "miscellaneous": "Miscellaneous Commands",
    "prestige":      "Prestige Commands",
    "professions":   "Profession Commands",
    "quests":        "Quest Commands",
    "weapon":        "Weapon Commands",
}

# ───────── Helpers ─────────────────────────────────────────────────────────────

def resource_path(rel_path):
    """Resolve path bundled by PyInstaller or running as script."""
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(__file__)
    return os.path.join(base, rel_path)

def make_window_noactivate(hwnd):
    """Mark a window WS_EX_NOACTIVATE|WS_EX_TOOLWINDOW so it never steals focus."""
    ex = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ex |= (WS_EX_NOACTIVATE | WS_EX_TOOLWINDOW)
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, ex)

def find_vrising_window():
    """Find first HWND whose title contains 'v rising' (case‐insensitive)."""
    if not win32gui:
        return None
    results = []
    def enum_cb(hwnd, _):
        if "vrising" in win32gui.GetWindowText(hwnd).lower():
            results.append(hwnd)
    win32gui.EnumWindows(enum_cb, None)
    return results[0] if results else None

# ───────── Key Injection ───────────────────────────────────────────────────────

def press_sc(vk):
    """
    Press+release a key by scan-code using keybd_event.
    Works in elevated EXE as well as interpreter.
    """
    sc = ctypes.windll.user32.MapVirtualKeyW(vk, MAPVK_VK_TO_VSC)
    # key down
    ctypes.windll.user32.keybd_event(vk, sc, 0, 0)
    time.sleep(0.005)
    # key up
    ctypes.windll.user32.keybd_event(vk, sc, KEYEVENTF_KEYUP, 0)
    time.sleep(0.005)

def send_text_sc(text: str):
    """
    Send each character via Unicode key events, with a short pause
    to ensure the game’s input buffer keeps up.
    """
    for ch in text:
        code = ord(ch)
        # key down (Unicode)
        ctypes.windll.user32.keybd_event(
            0,        # vk = 0 for Unicode
            code,     # wScan = Unicode code point
            KEYEVENTF_UNICODE,
            0
        )
        # key up
        ctypes.windll.user32.keybd_event(
            0,
            code,
            KEYEVENTF_UNICODE | KEYEVENTF_KEYUP,
            0
        )
        # give the game a moment to process this char
        time.sleep(0.01)
        
# ───────── Prompt Popup ─────────────────────────────────────────────────────────

class PromptPopup(QWidget):
    def __init__(self, command_panel):
        super().__init__(None, OVERLAY_FLAGS)
        self.command_panel = command_panel
        self.setFocusPolicy(Qt.StrongFocus)
        self.setStyleSheet(
            "background:rgba(40,40,40,220);"
            "border:1px solid rgba(255,255,255,50);"
        )
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8,8,8,8)
        layout.setSpacing(6)
        self.prompt_label = QLabel("", self)
        self.prompt_label.setStyleSheet("color:white;")
        self.combo = QComboBox(self)
        self.combo.setStyleSheet("color:white; background:rgba(50,50,50,200);")
        self.line  = QLineEdit(self)
        self.line.setStyleSheet("color:white; background:rgba(50,50,50,200);")
        btns = QHBoxLayout()
        self.send_btn   = QPushButton("Send",   self)
        self.cancel_btn = QPushButton("Cancel", self)
        for b in (self.send_btn, self.cancel_btn):
            b.setStyleSheet("color:white; background:rgba(80,80,80,200);")
        btns.addWidget(self.send_btn)
        btns.addWidget(self.cancel_btn)
        layout.addWidget(self.prompt_label)
        layout.addWidget(self.combo)
        layout.addWidget(self.line)
        layout.addLayout(btns)
        self.resize(PROMPT_WIDTH, PROMPT_HEIGHT)
        self.send_btn.clicked.connect(self._on_send)
        self.cancel_btn.clicked.connect(self.hide)
        self.combo.activated.connect(self._on_combo)
        self.line.returnPressed.connect(self._on_send)

    def showEvent(self, ev):
        super().showEvent(ev)
        hwnd = int(self.winId())
        ex = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        ex &= ~WS_EX_NOACTIVATE
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, ex)
        ctypes.windll.user32.SetForegroundWindow(hwnd)
        self.activateWindow()
        self.line.setFocus()

    def _on_combo(self, idx):
        self.command_panel._on_prompt_combo(idx)
    def _on_send(self):
        self.command_panel._on_prompt_send()

# ───────── Command Panel ───────────────────────────────────────────────────────

class CommandPanel(QWidget):
    def __init__(self, parent_bar):
        super().__init__(None, OVERLAY_FLAGS)
        self.parent_bar = parent_bar
        self.last_cmd   = None
        self.last_time  = 0
        self._init_ui()
        self.hide()

    def _init_ui(self):
        self.setStyleSheet("background: rgba(30,30,30,180);")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setFocusPolicy(Qt.NoFocus)
        self.scroll = QScrollArea(self); self.scroll.setFrameShape(self.scroll.NoFrame)
        self.scroll.setWidgetResizable(True)
        container = QWidget(); container.setStyleSheet("background:transparent;")
        self.vbox = QVBoxLayout(container); self.vbox.setContentsMargins(10,10,10,10); self.vbox.setSpacing(12)
        self.scroll.setWidget(container)
        main = QVBoxLayout(self); main.setContentsMargins(0,0,0,0); main.addWidget(self.scroll)
        self.resize(CMD_WIDTH, 600)
        self.prompt = PromptPopup(self); self.prompt.hide()

    def show_for_category(self, cat):
        self.current_cat = cat; self._rebuild(); self.show(); self.reposition()

    def reposition(self):
        bar = self.parent_bar.frameGeometry()
        scr = QApplication.primaryScreen().availableGeometry()
        x = bar.right()
        if x + self.width() > scr.right(): x = bar.left() - self.width()
        y = max(scr.top(), min(bar.top(), scr.bottom() - self.height()))
        self.move(x, y); self._reposition_prompt()

    def _rebuild(self):
        while self.vbox.count():
            w = self.vbox.takeAt(0).widget()
            if w: w.deleteLater()
        for grp, cmds in COMMANDS[self.current_cat].items():
            box = QGroupBox(grp); box.setStyleSheet("QGroupBox { color:white; font-weight:bold; }")
            gl = QVBoxLayout(box); gl.setSpacing(6)
            for cmd in cmds:
                row = QHBoxLayout()
                badge = QLabel("⌨" if cmd["params"] else "", box); badge.setStyleSheet("color:white;"); badge.setFixedWidth(16)
                btn = QPushButton(cmd["label"], box)
                btn.setFocusPolicy(Qt.NoFocus); btn.setFixedHeight(BTN_H)
                btn.setStyleSheet(
                    "color:white; background:rgba(80,80,80,200);"
                    "border:1px solid rgba(255,255,255,30); border-radius:3px;"
                )
                btn.setToolTip(cmd["description"])
                btn.clicked.connect(lambda _, c=cmd, b=btn: self._start(c, b))
                row.addWidget(badge); row.addWidget(btn); gl.addLayout(row)
            self.vbox.addWidget(box)

    def hide(self):
        self.prompt.hide()
        super().hide()

    def _start(self, cmd, btn):
        if self.prompt.isVisible():
            if btn is getattr(self, "trigger_btn", None):
                self.prompt.hide(); return
            else:
                self.prompt.hide()
        if not cmd["params"]:
            return self._send(cmd["template"])
        self.prompt_cmd  = cmd
        self.prompt_tmpl = cmd["template"]
        self.prompt_params = list(cmd["params"])
        self.prompt_vals = []
        self.prompt_idx  = 0
        self.trigger_btn = btn
        self._next_param()

    def _next_param(self):
        tag = self.prompt_params[self.prompt_idx]
        opts = self.prompt_cmd.get("options", {}).get(tag, [])
        self.prompt.prompt_label.setText(f"{tag}:")
        if opts:
            self.prompt.combo.clear(); self.prompt.combo.addItems(opts)
            self.prompt.combo.show(); self.prompt.line.hide()
            self.prompt.send_btn.hide(); self.prompt.cancel_btn.show()
        else:
            self.prompt.line.clear(); self.prompt.line.show()
            self.prompt.combo.hide(); self.prompt.send_btn.show(); self.prompt.cancel_btn.show()
        bg = self.trigger_btn.mapToGlobal(QPoint(0,0))
        self.prompt.move(bg.x()+self.trigger_btn.width()+10, bg.y())
        self.prompt.show()

    def _on_prompt_combo(self, i):
        if i<0: return
        self.prompt_vals.append(self.prompt.combo.itemText(i))
        self.prompt_idx+=1
        if self.prompt_idx < len(self.prompt_params): self._next_param()
        else: self._finish()

    def _on_prompt_send(self):
        v = self.prompt.line.text().strip()
        if not v: return
        self.prompt_vals.append(v)
        self.prompt_idx+=1
        if self.prompt_idx < len(self.prompt_params): self._next_param()
        else: self._finish()

    def _reposition_prompt(self):
        if self.prompt.isVisible():
            bg = self.trigger_btn.mapToGlobal(QPoint(0,0))
            self.prompt.move(bg.x()+self.trigger_btn.width()+10, bg.y())

    def _finish(self):
        filled = self.prompt_tmpl
        tmpl   = self.prompt_tmpl
        is_bl  = tmpl.startswith(".bl cst")
        is_wp  = tmpl.startswith(".wep cst")
        for tag, val in zip(self.prompt_params, self.prompt_vals):
            if is_bl and tag=="BloodStat":
                opts = self.prompt_cmd.get("options", {}).get(tag, [])
                rep  = str(opts.index(val)+1) if val in opts else "1"
            elif is_wp and tag=="WeaponStat":
                opts = self.prompt_cmd.get("options", {}).get(tag, [])
                rep  = str(opts.index(val)+1) if val in opts else "1"
            else:
                rep = val
            filled = filled.replace(f"[{tag}]", rep, 1)
        self.prompt.hide()
        self._send(filled)

    def _send(self, cmd):
        # throttle identical commands
        now = time.time()
        if cmd == getattr(self, "last_cmd", None) and now - self.last_time < 0.5:
            return
        self.last_cmd, self.last_time = cmd, now

        # focus V Rising
        hwnd = find_vrising_window()
        if hwnd:
            try:
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(hwnd)
            except:
                pass

        # 1) open chat
        press_sc(VK_RETURN)
        time.sleep(0.05)

        # 2) type the full command
        send_text_sc(cmd)
        time.sleep(0.05)

        # 3) send it
        press_sc(VK_RETURN)

        # update overlay
        self.parent_bar.cmd_panel.reposition()

# ───────── Icon Bar Overlay ────────────────────────────────────────────────────

class IconBarOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons     = {}
        self.current_cat = None
        self.cmd_panel   = CommandPanel(self)
        self._init_ui()

    def _init_ui(self):
        self.setWindowFlags(OVERLAY_FLAGS)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setFocusPolicy(Qt.NoFocus)
        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(1,1,1,1)
        layout.setSpacing(GAP)

        img_dir = resource_path("imgs")
        for cat in COMMANDS:
            btn = QPushButton(self)
            btn.setIcon(QIcon(os.path.join(img_dir, f"{cat}.png")))
            btn.setIconSize(QSize(ICON_SIZE, ICON_SIZE))
            btn.setFixedSize(ICON_SIZE+2, ICON_SIZE+2)
            btn.setFocusPolicy(Qt.NoFocus)
            btn.setStyleSheet("border:none; background:transparent;")
            btn.setToolTip(CATEGORY_DISPLAY.get(cat, cat))
            btn.clicked.connect(lambda _, c=cat: self._toggle_category(c))
            btn.installEventFilter(self)
            layout.addWidget(btn)
            self.buttons[cat] = btn

        close_btn = QPushButton("✕", self)
        close_btn.setStyleSheet("""
            QPushButton {
                border:1px solid rgba(255,255,255,30);
                background: rgba(30,30,30,150);
                color: #bbb;
                font-size: 18pt;
                padding: 8px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background: rgba(200,0,0,150);
                border-color: rgba(255,50,50,200);
            }
        """)
        close_btn.setFixedSize(ICON_SIZE+2, ICON_SIZE+2)
        close_btn.setToolTip("Close Overlay")
        close_btn.clicked.connect(QApplication.instance().quit)
        layout.addWidget(close_btn)

        self.adjustSize()
        self.move(0, 100)

    def eventFilter(self, obj, ev):
        if obj in self.buttons.values():
            if ev.type()==QEvent.MouseButtonPress and ev.button()==Qt.LeftButton:
                self._drag_pos = ev.globalPos() - self.frameGeometry().topLeft()
                return False
            if ev.type()==QEvent.MouseMove and ev.buttons()&Qt.LeftButton and getattr(self,"_drag_pos",None):
                self.move(ev.globalPos() - self._drag_pos)
                if self.cmd_panel.isVisible(): self.cmd_panel.reposition()
                return False
            if ev.type()==QEvent.MouseButtonRelease:
                self._drag_pos=None; return False
            if ev.type()==QEvent.Enter:
                QToolTip.showText(QCursor.pos(), obj.toolTip(), obj)
            if ev.type()==QEvent.Leave:
                QToolTip.hideText()
        return super().eventFilter(obj, ev)

    def _toggle_category(self, cat):
        self.cmd_panel.prompt.hide()
        if self.current_cat==cat:
            self.current_cat=None
            self.cmd_panel.hide()
            self._highlight_icon(None)
        else:
            self.current_cat=cat
            self._highlight_icon(cat)
            self.cmd_panel.show_for_category(cat)

    def _highlight_icon(self, sel):
        for c,btn in self.buttons.items():
            btn.setStyleSheet("border:2px solid rgba(0,200,255,200);" if c==sel else "border:none;")

    def showEvent(self, ev):
        super().showEvent(ev)
        make_window_noactivate(int(self.winId()))

    def mousePressEvent(self, e):
        if e.x()<=ICON_SIZE+2 and e.button()==Qt.LeftButton:
            self._drag_pos=e.globalPos()-self.frameGeometry().topLeft(); e.accept()

    def mouseMoveEvent(self, e):
        if getattr(self,"_drag_pos",None) and e.buttons()==Qt.LeftButton:
            self.move(e.globalPos()-self._drag_pos); e.accept()
            if self.cmd_panel.isVisible(): self.cmd_panel.reposition()

    def mouseReleaseEvent(self, e):
        self._drag_pos=None; e.accept()

# ───────── Entry Point ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = IconBarOverlay()
    overlay.show()
    sys.exit(app.exec_())

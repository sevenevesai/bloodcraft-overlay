# Bloodcraft Overlay

**A lightweight PyQt5 overlay to send chat commands directly into V-Rising with a customizable sidebar and prompt UI.**

![License](https://img.shields.io/badge/license-MIT-blue)

---
## Features

* **Sidebar icons** for quick access to command categories
* **Interactive prompts** for parameterized commands (picklists and free-text)
* **Reliable key injection** into V-Rising chat using Win32 APIs

## Prerequisites

* Windows 10 or later
* V-Rising installed and running
* Python 3.10+ for development

## Getting Started

Clone this repository:

```bash
git clone https://github.com/sevenevesai/bloodcraft-overlay.git
cd bloodcraft-overlay
```

Install dependencies:

```bash
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
```

## Running the Overlay

Launch directly with Python:

```bash
python main.py
```

* **Toggle Command Panel**: click a category icon
* **Send Commands**: click a command, fill any prompts, press **Send**
* **Exit Overlay**: click the ✕ button

## Project Structure

```
bloodcraft-overlay/
├─ imgs/          # icon assets
├─ commands.py    # command definitions
├─ main.py        # application entry point
├─ overlay.spec   # PyInstaller spec (optional)
└─ README.md      # this file
```

## Contributing

Contributions are welcome! Please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Open a Pull Request

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

*For issues or feature requests, please open an issue on GitHub: [https://github.com/sevenevesai/bloodcraft-overlay/issues](https://github.com/sevenevesai/bloodcraft-overlay/issues)*

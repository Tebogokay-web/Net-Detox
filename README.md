# Net Detox 🛡️

A professional, modern Windows GUI utility designed to safely reset network configurations, flush DNS, and clear Winsock catalogs to troubleshoot and resolve stubborn internet connectivity issues.

---

## Features
* **One-Click Network Reset:** Easily execute core Windows networking repair commands without dealing with command-line prompts.
* **DNS Flushing:** Clears the DNS resolver cache to fix website loading errors and stale connections.
* **Winsock Catalog Reset:** Resets the Windows Sockets API catalog to clean up corrupted network stacks.
* **Custom GUI & Branding:** Built with a clean interface and custom application branding for a polished user experience.
* **Administrator Privileges:** Designed to request necessary UAC permissions automatically to execute system-level commands safely.

---

## 📥 How to Download and Use (For End Users)

If you just want to use the application without looking at the code:
1. Head over to the **[Releases](../../releases)** page on the right sidebar of this repository.
2. Download the latest compiled `.exe` or installer file.
3. Right-click the application and select **Run as administrator** to start using it.

---

## 🛠️ Building from Source (For Developers)

If you want to clone the repository and compile the executable yourself using PyInstaller, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/TebogoKay-web/net-detox.git](https://github.com/TebogoKay-web/net-detox.git)
cd net-detox

```

### 2. Install Dependencies

Make sure you have Python 3.13 installed, then install PyInstaller:

```bash
python -m pip install pyinstaller

```

### 3. Build the Executable

Run the following PyInstaller command in your terminal to bundle the script, custom icon, and admin manifest into a single executable:

```bash
python -m PyInstaller --onefile --windowed --uac-admin --icon=net_detox.ico net_detox_gui.py

```

Your finished executable will appear inside the generated `dist/` folder.

---

## Project Structure

* `net_detox_gui.py`: The main Python source code file containing the Tkinter interface and network reset logic.
* `net_detox.ico`: Custom application icon asset.
* `.gitignore`: Configured to ignore local build artifacts and environment caches.

---

## License

This project is open-source and available under the terms of the [MIT License](https://www.google.com/search?q=LICENSE).

```

```

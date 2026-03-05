# Installation

## Graphical Installer (GUI only, no CLI)

If you only need the graphical application and do not need the command line, download the ready-made installer from the releases page:

**[https://github.com/andgineer/ibkr-porez/releases](https://github.com/andgineer/ibkr-porez/releases)**

=== "macOS"
    Download the latest `.dmg` file.
    Because the app is not signed with an Apple certificate, macOS may block it on first open.

    > _"IBKR Porez" is damaged and can't be opened. You should move it to the Bin._

    **Do not move it to the Bin.** Instead:

    1. Open **System Settings -> Privacy & Security**
    2. At the bottom of the Security section, you will see a blocked-app message. Click **Open Anyway**
    3. Confirm opening in the next dialog

    You may need to repeat the same steps **twice**:
    - first when opening the downloaded installer (`.dmg`)
    - and again when launching the installed app from `/Applications` for the first time

    After that, the app should launch without warnings.

=== "Windows"
    Download the latest `.msi` file.
    Because the installer is not code-signed, Windows may show security warnings.

    If your browser blocks the download (for example in Microsoft Edge):
    1. Open the browser downloads panel (`Ctrl+J`)
    2. Find the blocked `.msi` download
    3. Click **Keep** -> **Show more** -> **Keep anyway**

    When launching the installer, Windows may show **Windows protected your PC**:
    1. Click **More info**
    2. Click **Run anyway**

    You may also see a User Account Control dialog with **Unknown publisher**.
    If the file came from the official releases page, click **Yes** to continue.

    After installation, the app should start normally.

---

## Install Python package (CLI + GUI)

If CLI is your native language (AI agents and brave humans), install the Python package.

Install Astral `uv tool`: [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/)

### Install application

```bash
uv tool install ibkr-porez --python 3.12
```

# AstimWavPlayer

English | [Русский](README_RU.md)

Application for playing WAV files on the MCS A-stim R 1.1 device.

## Features

- Selecting and playing WAV files via WASAPI exclusive mode on the MCS A-stim R 1.1 device.
- Automatic device connection check at startup and during operation.
- Waiting for the A-stim connection with the option to exit the application.
- Automatic playback stop when the connection to the device is lost.
- Display of the current position and the total file duration.
- Volume control with quick reset to 50%.
- Blocking the WAV file change during playback.
- Confirmation of playback stop and application exit.
- Russian and English interface, switchable at runtime.

## Option 1: Ready-made installer (recommended for users)

The easiest way is to download the ready-made AstimWavPlayer installer from the Releases page:

1. Open the [Releases](https://github.com/mcsltd/mcs-astim-wav-player/releases) page of this repository
2. Find the latest release (the topmost one)
3. In the Assets section, download the archive with the installer
4. Unpack the archive
5. Run the installer
6. Follow the installer instructions

## Option 2: Running from source code (for developers)

If you want to run the application from source code or make changes:

### Requirements

- Windows 10 or later
- Python 3.12 or higher
- Git (to clone the repository)

### Installation steps

1. Clone the repository:
```
git clone git@github.com:mcsltd/mcs-astim-wav-player.git
```

2. Create a virtual environment:
```
python -m venv venv
venv\Scripts\activate
```

3. Install the dependencies:
```
pip install -r requirements.txt
```

4. Run the application:
```
python main.py
```

## Configuration

The application is configured through the `config.py` file:

| Parameter | Description | Default value |
|---|---|---|
| `DEVICE_NAME` | Name of the A-stim device | `"MCS A-Stim R1.1"` |
| `DEBUG` | Debug mode: shows the output device selector and allows playback without a connected A-stim | `True` |
| `VERSION` | Application version | `"v0.1.1"` |

The interface language is English on the first launch. It can be switched at runtime via the **Help → Language** menu (Russian / English); the selected language and the last opened folder are stored in the system settings (QSettings) and restored on the next launch.

## Device requirements

- MCS A-stim R 1.1 device

## Copyrights

Copyright © 2026, Medical Computer Systems Ltd

## License

This project is licensed under the [MIT License](LICENSE).

### Third-party libraries

- PySide6 (Qt for Python) is used under the LGPL license
- Other libraries are used under MIT, BSD, Apache 2.0

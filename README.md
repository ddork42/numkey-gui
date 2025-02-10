# NumKey GUI

A simple Windows application that allows you to trigger numpad keystrokes with checkboxes. Useful for automation and accessibility purposes.

## Features

- Support for numpad keys 0-9
- Support for Ctrl+Numpad and Alt+Numpad combinations
- Additional support for Numpad decimal (.) and plus (+) keys
- Saves checkbox states between sessions
- Simple and clean interface
- Single executable file

## Installation

1. Download the latest `numkey_gui.exe` from the Releases page
2. Run the executable - no installation needed

## Development Setup

If you want to modify or build from source:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/numkey-gui.git
cd numkey-gui
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python numkey_gui.py
```

### Building the Executable

The executable is automatically built using GitHub Actions. To build locally:

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Build the executable:
```bash
pyinstaller --onefile --windowed numkey_gui.py
```

The executable will be created in the `dist` directory.

## Usage

1. Launch the application
2. Select the desired numpad keys and combinations using checkboxes
3. Click "Apply" to trigger the selected keystrokes in sequence
4. Your selection will be saved automatically when closing the application

## Requirements

- Windows operating system
- No additional requirements for the executable
- For development: Python 3.6+ and the packages listed in requirements.txt

## License

MIT License - See LICENSE file for details

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

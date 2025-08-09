# TERA Toolbox

A comprehensive modding framework for TERA Online, providing both GUI and CLI interfaces with automatic updates and extensive module support.

## Features

- **Dual Interface Support**: Both graphical user interface (GUI) and command-line interface (CLI)
- **Automatic Updates**: Self-updating system with multiple server fallbacks
- **Module Management**: Extensive library of pre-installed and downloadable mods
- **Real-time Game Integration**: Direct connection to game client for live data queries
- **Cross-platform Support**: Windows compatibility with both admin and non-admin versions
- **Developer Friendly**: Comprehensive documentation and module development tools

## Installation

### Quick Setup
1. Download the installer from [GitHub Releases](https://github.com/tera-private-toolbox/tera-toolbox/releases/download/teratoolbox-setup/TeraToolboxSetup.exe)
2. Run the installer and follow the wizard instructions
3. Launch `TeraToolbox.exe` for GUI or `TeraToolboxCLI.exe` for CLI

### Manual Installation
1. Install Node.js (version 11.4.0 or higher)
2. Clone this repository
3. Run `npm install` to install dependencies
4. Launch the appropriate executable

## Usage

### GUI Mode (Recommended)
- Run `TeraToolbox.exe` for the full graphical interface
- Features include:
  - Module management with install/uninstall capabilities
  - Settings configuration
  - Real-time status monitoring
  - Automatic updates

### CLI Mode
- Run `TeraToolboxCLI.exe` for command-line interface
- Suitable for:
  - Server deployments
  - Automated scripts
  - Headless operation

### First Launch
The initial startup may take several minutes as the system downloads and updates all required files. This is normal and only occurs once.

## Available Modules

### Core Modules
- **Essentials**: Basic game enhancements and quality-of-life improvements
- **Auto-Bank**: Automatic banking functionality
- **Auto-Loot**: Streamlined loot collection
- **Auto-Pet**: Pet management automation
- **Camera Control**: Advanced camera manipulation
- **FPS Utils**: Performance optimization tools

### Game Enhancement Modules
- **Skill Prediction**: Advanced skill timing and prediction
- **Endless Crafting**: Automated crafting systems
- **Anti-Bodyblock**: Prevents body blocking issues
- **AFKer**: Away-from-keyboard detection and handling
- **Exit Instantly**: Quick game exit functionality

### Utility Modules
- **Translate Chat**: Real-time chat translation
- **Tera Guide**: In-game guide and information system
- **Settings Saver/Fixer**: Configuration management tools
- **Python Bridge**: Python integration for custom scripts
- **External Interface**: API for external applications

### Developer Tools
- **Library**: Core development libraries
- **Command**: Command system framework
- **Bugfix**: Various game bug fixes
- **UI**: User interface components

## Configuration

### Settings
Access the Settings page in the GUI to configure:
- Update preferences
- Module settings
- Connection parameters
- Performance options

### Module Management
- **My Mods**: View and manage installed modules
- **Get More Mods**: Browse and install additional modules
- Enable/disable modules as needed

## Development

### Module Development
See the [Module Development Documentation](TERA%20Starscape%20Toolbox/doc/mod/main.md) for detailed information on creating custom modules.

### Key Components
- **index-gui.js**: Main GUI entry point with Electron integration
- **index-cli.js**: Command-line interface implementation
- **loader-gui.js**: GUI module loading system
- **loader-cli.js**: CLI module loading system
- **mod-manager.js**: Module management system
- **update-self.js**: Self-update functionality

### Architecture
- **Electron-based GUI**: Modern web-based interface
- **Node.js Backend**: Robust server-side processing
- **Module System**: Extensible plugin architecture
- **Auto-update System**: Multi-server update mechanism

## Support

### Community
- **Discord Server**: https://discord.gg/CZMYNhXwwS
- **GitHub Issues**: Report bugs and request features
- **Documentation**: Comprehensive guides in the `doc/` directory

### Troubleshooting
- **Anti-virus Issues**: Whitelist TERA Toolbox in your anti-virus software
- **Game Client Conflicts**: Ensure no game instances are running during updates
- **Permission Issues**: Use the NoAdmin versions if needed

## Technical Requirements

- **Operating System**: Windows 10/11
- **Node.js**: Version 11.4.0 or higher
- **TERA Client**: Compatible with patches 92.03, 92.04, and 100.02 (x64)
- **Memory**: Minimum 4GB RAM recommended
- **Storage**: 500MB free space for installation

## License

This project is based on the original Tera-Proxy framework and is maintained by the TERA Toolbox community.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

For detailed contribution guidelines, see the documentation in the `doc/` directory.

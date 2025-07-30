# 🚀 Facebook Token Converter | HACKER EDITION

<div align="center">

```
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗     ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
███████║███████║██║     █████╔╝ █████╗  ██████╔╝       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
```

**A sleek, hacker-themed GUI application for converting Facebook short-lived tokens to long-lived tokens**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![ttkbootstrap](https://img.shields.io/badge/GUI-ttkbootstrap-purple.svg)](https://ttkbootstrap.readthedocs.io/)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

</div>

## 🔥 Features

### 🎨 **Hacker-Themed Interface**
- Dark superhero theme with terminal aesthetics
- ASCII art headers and hacker-style typography
- Real-time terminal output with color-coded logs
- Professional gradient effects and modern UI components

### 💻 **Core Functionality**
- **Convert Facebook Tokens**: Transform short-lived tokens (1-2 hours) into long-lived tokens (60 days)
- **Real-time Logging**: Watch the conversion process with live terminal output
- **Clipboard Integration**: Easy paste input and copy output functionality
- **Error Handling**: Comprehensive error messages with troubleshooting tips
- **Multi-threading**: Non-blocking UI with progress indicators

### 🛡️ **Security & UX**
- **Password Masking**: Hide/show App Secret toggle
- **Input Validation**: Prevents empty field submissions
- **Secure API Calls**: Direct communication with Facebook Graph API
- **Clear Function**: Quick reset of all fields and outputs

## 📸 Screenshots

<div align="center">

### Main Interface
![Main Interface](https://via.placeholder.com/800x600/0d1117/58a6ff?text=Main+Interface+Screenshot)

### Terminal Output
![Terminal Output](https://via.placeholder.com/800x400/0d1117/3fb950?text=Terminal+Output+Screenshot)

### Success Conversion
![Success](https://via.placeholder.com/800x300/0d1117/3fb950?text=Successful+Token+Conversion)

</div>

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Internet connection for API calls

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/facebook-token-converter.git
   cd facebook-token-converter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install ttkbootstrap requests pyperclip
   ```

3. **Run the application**
   ```bash
   python FacebookToken.py
   ```

### Auto-Installation
The application will automatically install missing dependencies on first run.

## 📋 Requirements

Create a `requirements.txt` file:
```
ttkbootstrap>=1.10.1
requests>=2.28.0
pyperclip>=1.8.2
```

## 🔧 Usage

### Step 1: Get Facebook App Credentials
1. Visit [Facebook Developers](https://developers.facebook.com/)
2. Create or select your Facebook App
3. Get your **App ID** and **App Secret** from App Settings

### Step 2: Generate Short-lived Token
1. Go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
2. Select your app and required permissions:
   - `ads_read`
   - `ads_management`
   - `business_management`
3. Generate Access Token (this will be short-lived)

### Step 3: Convert Token
1. Launch the Token Converter application
2. Enter your **App ID**
3. Enter your **App Secret**
4. Paste your **Short-lived Token**
5. Click **🚀 INITIATE TOKEN CONVERSION**
6. Copy your new **Long-lived Token** from the terminal output

## 📊 Token Comparison

| Feature | Short-lived Token | Long-lived Token |
|---------|------------------|------------------|
| **Lifespan** | 1-2 hours | 60 days |
| **Use Case** | Testing | Production |
| **Security** | High turnover | Stable access |
| **Renewal** | Manual/Frequent | Less frequent |

## 🎯 Advanced Features

### Terminal Commands
The application provides a rich terminal experience with:
- **Timestamped logs** for all operations
- **Color-coded messages** (Info, Success, Warning, Error)
- **Real-time status updates**
- **Comprehensive error reporting**

### Keyboard Shortcuts
- `Ctrl+V` - Paste token (when token field is focused)
- `Ctrl+C` - Copy from terminal output
- `Ctrl+A` - Select all terminal text

### API Integration
```python
# Example API call structure
url = "https://graph.facebook.com/oauth/access_token"
params = {
    'grant_type': 'fb_exchange_token',
    'client_id': 'YOUR_APP_ID',
    'client_secret': 'YOUR_APP_SECRET',
    'fb_exchange_token': 'YOUR_SHORT_TOKEN'
}
```

## 🐛 Troubleshooting

### Common Issues

#### ❌ "Missing Permission" Error
- **Solution**: Ensure your app has proper permissions
- **Check**: Business Manager admin access
- **Verify**: Token includes required scopes

#### ❌ "Invalid App Credentials" Error
- **Solution**: Verify App ID and App Secret
- **Check**: Copy credentials exactly from Facebook Developer Console
- **Verify**: App is not in development mode restrictions

#### ❌ "Token Expired" Error
- **Solution**: Generate a fresh short-lived token
- **Check**: Token was recently created (within 1-2 hours)
- **Verify**: Token format and completeness

#### ❌ "Connection Timeout" Error
- **Solution**: Check internet connection
- **Check**: Firewall settings
- **Verify**: API endpoint accessibility

### Debug Mode
Enable verbose logging by modifying the log level in the source code:
```python
# Add this for more detailed logs
logging.basicConfig(level=logging.DEBUG)
```

## 🔐 Security Considerations

- **Never share your App Secret** publicly
- **Store tokens securely** and never commit them to version control
- **Use environment variables** for production deployments
- **Regularly rotate tokens** even if they haven't expired
- **Monitor token usage** in Facebook Business Manager

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Setup
```bash
# Clone your fork
git clone https://github.com/yourusername/facebook-token-converter.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt
```

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Include docstrings for functions

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Facebook Token Converter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 👨‍💻 Authors

- **DevTom** - *Initial work* - [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- **Facebook Graph API** for providing the token exchange endpoint
- **ttkbootstrap** for the amazing modern GUI framework
- **Python Community** for excellent libraries and support
- **Open Source Contributors** who make projects like this possible

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/facebook-token-converter/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/facebook-token-converter/discussions)
- **Email**: your.email@example.com

## 🔗 Related Links

- [Facebook for Developers](https://developers.facebook.com/)
- [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
- [Facebook Business Manager](https://business.facebook.com/)
- [TTK Bootstrap Documentation](https://ttkbootstrap.readthedocs.io/)

## 📈 Changelog

### v2.0.0 - Hacker Edition (2024-07-30)
- 🔥 Complete UI redesign with hacker theme
- 💻 Added terminal-style output with real-time logging
- 🚀 Improved error handling and user feedback
- 📋 Enhanced clipboard integration
- 🛡️ Added security features and input validation
- ⚡ Performance optimizations and threading

### v1.0.0 - Initial Release (2024-07-29)
- 🎯 Basic token conversion functionality
- 🖥️ Simple GUI interface
- 📊 Basic error handling
- 🔄 API integration with Facebook Graph

---

<div align="center">

**Made with ❤️ and ☕ by the community**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/facebook-token-converter?style=social)](https://github.com/yourusername/facebook-token-converter/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/facebook-token-converter?style=social)](https://github.com/yourusername/facebook-token-converter/network)

**If this project helped you, please consider giving it a ⭐!**

</div>

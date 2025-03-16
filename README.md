# 🌸 Sakura Obfuscator 🌸

A powerful Python code obfuscator that makes your code harder to reverse engineer. 🔒 This tool transforms your Python source code by applying multiple layers of obfuscation techniques, making it significantly more difficult to understand or decompile. 🛡️

![Obfuscator Banner](https://kukui.ch/wp-content/uploads/2024/05/Z-BP-21SAKURA1-1536x1152-1.jpg)

## ✨ Features ✨

- 🔹 **String Obfuscation**: Transforms string literals into complex encoded expressions
- 🔹 **Builtin Function Obfuscation**: Hides references to built-in Python functions
- 🔹 **Junk Code Injection**: Adds meaningless code to confuse decompilers
- 🔹 **Anti-Decompilation**: Implements techniques to break common decompilers
- 🔹 **Anti-Debugging**: Adds protection against common debugging tools
- 🔹 **Code Compression**: Compresses and encodes final code to add additional protection
- 🔹 **Multiple Obfuscation Levels**: Choose between basic and advanced protection

## ⚙️ Installation ⚙️

```bash
# Clone the repository
git clone https://github.com/nguyenxuantrinhnotpd/Sakura.git
cd Sakura
```

## 📌 Requirements 📌

- 🐍 Python 3.10+
- 📦 Required packages (install with pip):
  ```bash
  pip install colorama pytz pystyle
  ```

## 🚀 Usage 🚀

### 🔹 Basic Usage

```bash
python Sakura.py -f your_script.py
```

This will create an obfuscated version at `obf-your_script.py` 📄

### ⚡ Command Line Options ⚡

```
usage: Sakura.py [-h] [-f FILE] [-o OUTPUT] [-m {1,2}] [-p {true,false,True,False}] [-t TYPE]

Python Code Obfuscator 🛠️

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to the Python file to obfuscate 📜
  -o OUTPUT, --output OUTPUT
                        Output file name ✏️
  -m {1,2}, --mode {1,2}
                        Obfuscation mode (1: basic, 2: advanced) 🔄
  -p {true,false,True,False}, --protect {true,false,True,False}
                        Enable protection 🔐
  -t TYPE, --type TYPE  Execution type ⚙️
```

### 💡 Examples 💡

Basic obfuscation:
```bash
python Sakura.py -f script.py -m 1
```

Advanced obfuscation with custom output name:
```bash
python Sakura.py -f script.py -m 2 -o output.py
```

Disable protection features:
```bash
python Sakura.py -f script.py -p false
```

## 🔍 How It Works 🔍

The obfuscator applies multiple transformations to make your code harder to understand:

1. 🔄 **AST Transformation**: Uses Python's Abstract Syntax Tree to transform code
2. 🔡 **String Encoding**: Converts string literals to encoded expressions
3. 🔁 **Control Flow Obfuscation**: Adds complex control flows with try-except blocks
4. 🎭 **Variable Renaming**: Uses random Chinese characters for variable names
5. 🚧 **Anti-Decompile Traps**: Adds code that specifically breaks decompilers
6. 🔐 **Final Encoding**: Uses multiple layers of compression and encoding

## 🔥 Obfuscation Modes 🔥

- 🟢 **Mode 1 (Basic)**: Applies essential obfuscation techniques suitable for most cases
- 🔴 **Mode 2 (Advanced)**: Applies more aggressive obfuscation with multiple passes of junk code injection and rename variable names

## ⚠️ Limitations ⚠️

- 🐢 Obfuscated code may run slightly slower than the original
- ❌ Some Python features may not be compatible with heavy obfuscation
- 🔓 The protection is not unbreakable - it's designed to discourage casual reverse engineering
- 🛑 Code relying on introspection might break after obfuscation

## 🚨 Warning 🚨

This tool is intended for legitimate purposes such as:
- 🔒 Protecting proprietary algorithms
- 🔄 Preventing unauthorized modification of your code
- 🏛️ Making commercial software harder to pirate

**⚠️ Do not use this tool for malicious purposes. ⚠️**

# 🎖️ Acknowledgments 🎖️

A huge shoutout to [BLueRed](https://github.com/CSM-BlueRed) for the Impostor script, [hngocuyen](https://github.com/hngocuyen) for the enjuly19 script, and [lovmoon3k](https://github.com/lovmoon3k) for the pycloak script—your contributions are truly appreciated! 🚀

## 📞 Contact 📞

For any questions or issues, please open an issue on GitHub or contact me via:
- 📲 Telegram: @CalceIsMe

---

*⚠️ This obfuscator is provided as-is without warranty of any kind. Use at your own risk.*


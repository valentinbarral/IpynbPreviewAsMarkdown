
# Ipynb Preview as Markdown

"Ipynb Preview as Markdown" is a plugin for Sublime Text that enables users to view `.ipynb` (Jupyter Notebook) files as Markdown directly within the editor. This plugin provides a convenient way to preview notebook files without leaving Sublime Text, displaying the Markdown and code cells in a readable format.

## Installation

"Ipynb Preview as Markdown" can be installed either manually or via Package Control, the convenient package manager for Sublime Text.

### Option 1: Install Using Package Control (Recommended)

1. **Install Package Control**: If you haven't already, follow the [installation instructions](https://packagecontrol.io/installation) to install Package Control.
2. **Open Command Palette**: Use `Shift+Ctrl+P` on Windows/Linux or `Cmd+Shift+P` on macOS to open the Command Palette.
3. **Install Package**: Type `Package Control: Install Package` and press Enter.
4. **Find and Install**: Search for "Ipynb Preview as Markdown" in the list, then press Enter to install it.
5. **Restart Sublime Text**: Ensure the plugin is properly loaded.

### Option 2: Manual Installation

1. **Download the Plugin**: Clone this repository or download the ZIP file and extract it.
2. **Locate Sublime Text Packages Directory**:
    - On Windows, the path is usually `C:\Users\<Your Username>\AppData\Roaming\Sublime Text 3\Packages\`
    - On macOS, the path is usually `/Users/<Your Username>/Library/Application Support/Sublime Text 3/Packages/`
    - On Linux, the path is usually `~/.config/sublime-text-3/Packages/`
3. **Install the Plugin**: Copy the plugin directory (containing `ipynb_viewer.py` and `Default.sublime-commands` files) into the Sublime Text Packages directory.
4. **Restart Sublime Text**: This ensures the plugin is loaded and ready to use.

## Usage

To use the "Ipynb Preview as Markdown" plugin:

1. Open a `.ipynb` file in Sublime Text.
2. Open the Command Palette using `Shift+Ctrl+P` (or `Cmd+Shift+P` on macOS).
3. Type "Preview ipynb as Markdown" and select the command when it appears.
4. A split view will open with the original `.ipynb` file on the left and the Markdown preview on the right. The preview is read-only and cannot be edited.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

```text
MIT License

Copyright (c) 2024 Valentin Barral

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
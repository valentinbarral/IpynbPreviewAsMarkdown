
# Ipynb Preview as Markdown

**Ipynb Preview as Markdown** is a plugin for Sublime Text that enables users to view `.ipynb` (Jupyter Notebook) files as Markdown directly within the editor. This plugin provides a convenient way to preview notebook files without leaving Sublime Text, displaying the Markdown, source code, and output cells in a readable format.

## Features

Below is an overview of the capabilities integrated into this plugin:

- **Selective Cell Omission**: Users have the flexibility to exclude specific cells from the final Markdown document. This includes the ability to omit cells containing source code, those that display outputs following execution, or both.

- **Image Handling Enhancements**: To address the limitations of Base64 encoded images within notebooks, this tool automatically converts these images into references to temporary files. This approach not only makes the document more readable but also facilitates easier manipulation and sharing of the generated Markdown files.

- **Absolute Image Paths in Markdown Cells**: For Markdown cells that include references to local images, the tool automatically replaces the original path with an absolute path. This adjustment ensures that images are correctly rendered when using document conversion plugins like [Pandoc](https://packagecontrol.io/packages/Pandoc).

- **Language Preservation for Source Code Cells**: In recognition of the diverse programming languages that can be used within notebooks, this tool maintains the original language specified for code cells in the notebook when converting to Markdown. This commitment to preserving the source language ensures that the syntax highlighting and other language-specific features remain intact in the final document, providing a seamless transition from notebook to Markdown format.


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
3. Type *Preview ipynb as Markdown* and select the command when it appears.
4. A new window will open with the Markdown preview, showing all the types of cell (Markdown, Source code, or Result). The preview is read-only and cannot be edited.
5. Type instead *Preview ipynb as Markdown (No output)* to ommit the cells with results in the preview.
6. Type instead *Preview ipynb as Markdown (No code)* to ommit the cells with source code in the preview.
6. Type instead *Preview ipynb as Markdown (No code, No output)* to show only the Markdown cells in the preview.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

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

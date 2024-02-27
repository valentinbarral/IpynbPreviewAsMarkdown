'''
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
'''


import sublime
import sublime_plugin
import json

class PreviewIpynbAsMarkdownCommand(sublime_plugin.WindowCommand):
    def run(self):

        active_view = self.window.active_view()
        
        if not active_view:
            return
        
        file_name = active_view.file_name()
        if file_name and file_name.endswith('.ipynb'):
            # Load the file's content
            file_content = active_view.substr(sublime.Region(0, active_view.size()))
            
            try:
                nb = json.loads(file_content)
                markdown_content = ""
                
                # Convert cells to Markdown
                for cell in nb['cells']:
                    if cell['cell_type'] == 'markdown':
                        markdown_content += ''.join(cell['source']) + '\n\n'
                    elif cell['cell_type'] == 'code':
                        markdown_content += '```python\n' + ''.join(cell['source']) + '\n```\n\n'
                
                # Ccreate a split view and show Markdown content
                self.show_markdown_in_split_view(markdown_content)
                
            except Exception as e:
                sublime.error_message("Error processing .ipynb file: " + str(e))
        else:
            sublime.error_message("The current file is not an .ipynb file.")

    def show_markdown_in_split_view(self, markdown_content):
        self.window.run_command('set_layout', {
                    "cols": [0, 0.5, 1],
                    "rows": [0, 1],
                    "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
                })
        markdown_view = self.window.new_file()
        markdown_view.set_scratch(True)
        markdown_view.set_name("Ipynb preview as Markdown")
        markdown_view.set_syntax_file('Packages/Markdown/Markdown.sublime-syntax')
        markdown_view.run_command('append', {'characters': markdown_content})
        markdown_view.set_read_only(True)

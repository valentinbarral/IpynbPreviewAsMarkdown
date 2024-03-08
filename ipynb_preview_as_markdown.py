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
import re
import os.path
import base64
import tempfile

class PreviewIpynbAsMarkdownCommand(sublime_plugin.TextCommand):

    def run(self, edit, **args):

        # Options
        show_code = args['show_code']
        show_output = args['show_output']
        
        file_name = self.view.file_name()
        file_content = self.view.substr(sublime.Region(0, self.view.size()))
        
        try:
            nb = json.loads(file_content)
            base_path = self.view.window().extract_variables()["file_path"]
            markdown_content = ""

            # Check metadata to find source code language
            sc_lan = 'python'
            if nb['metadata']['kernelspec']['language']:
                sc_lan = nb['metadata']['kernelspec']['language']

            # Convert cells to Markdown
            for cell in nb['cells']:
                if cell['cell_type'] == 'markdown':
                    cell_content = ''.join(cell['source']) + '\n\n'
                    markdown_content += self.image_relative_paths_to_abs(base_path, cell_content)
                    #markdown_content += cell_content.replace('./', base_path+'/')

                elif cell['cell_type'] == 'code':
                    if show_code=='True':
                        markdown_content += '```' + sc_lan + '\n' + ''.join(cell['source']) + '\n```\n\n'
                    if show_output=='True':
                        for output_node in cell['outputs']:
                            markdown_content += self.parse_output_node(output_node)
            
            self.show_markdown_in_new_window(markdown_content)
            
        except Exception as e:
            sublime.error_message("Error processing .ipynb file: " + str(e))

    def is_enabled(self):
        file_name = self.view.file_name()
        if (file_name):
            return file_name.endswith('.ipynb')
        return False

    def show_markdown_in_new_window(self, markdown_content):
        """
        Creates a new window and shows the markdown code

        """
        new_window = sublime.run_command('new_window')
        new_view = sublime.active_window().new_file()
        new_view.set_scratch(True)
        new_view.set_name("Ipynb preview as Markdown")
        new_view.set_syntax_file('Packages/Markdown/Markdown.sublime-syntax')
        new_view.run_command('append', {'characters': markdown_content})
        new_view.set_read_only(True)


    def get_markdown_from_temp_image(self, base64_image):
        """
        Saves a Base64 encoded image to temporary file and generates Markdown code for it.

        """
        # Decode the Base64 encoded image
        image_data = base64.b64decode(base64_image)

        # Create a temporary file for the image
        image_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png", mode="wb")
        image_file.write(image_data)
        
        # Return Markdown code to display the image
        return "![]({0})".format(image_file.name)


    def image_relative_paths_to_abs(self, base_path, original_text):
        """
        Changes relative references to images to absolute paths

        """
        # Pattern to find markdown image references, e.g., ![caption](image)
        pattern = r'!\[(.*?)\]\((.*?)\)'
        
        # Function to replace the image reference with its full path
        def replace_with_full_path(match):
            image_reference = match.group(2)
            full_path = os.path.join(base_path, image_reference)
            return '![{0}]({1})'.format(match.group(1),full_path)
        
        # Replace all found image references in the markdown text
        modified = re.sub(pattern, replace_with_full_path, original_text)
        
        return modified

    def parse_output_node(self, output_node):
        """
        Parses the output of a source code node (text, image, or stream)

        """
        result = ""
        if output_node['output_type']=='execute_result':
            data = output_node['data']
            text_items = data['text/plain']
            for item in text_items:
                result += ''.join(item) + '\n'
        elif output_node['output_type']=='display_data':
            data = output_node['data']
            image_64 = data['image/png']
            text_items = data['text/plain']
            if image_64:
                result += self.get_markdown_from_temp_image(image_64) + '\n'
        elif output_node['output_type']=='stream':
            text_items = output_node['text']
            for item in text_items:
                result += ''.join(item)+ '\n'

        return result + '\n\n'




 

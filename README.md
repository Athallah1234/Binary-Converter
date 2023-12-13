# Binary Converter

This Python script provides a simple graphical user interface (GUI) for converting between binary and text. You can also load binary or text data from files, choose different encodings, and customize the conversion options.

## Features

- **Convert Binary to Text:** Enter a binary string, select encoding options, and convert it to text.
- **Convert Text to Binary:** Enter a text string, select encoding options, and convert it to binary.
- **Load Data from Files:** Load binary or text data from files to perform conversions.
- **Encoding Options:** Choose from a variety of encodings to support different character sets.
- **Include/Exclude Spaces and Commas:** Customize whether to include spaces or commas in the binary output.
- **Copy to Clipboard:** Easily copy the result to the clipboard for convenient use.

## How to Use

1. **Enter Binary or Text:** Input your binary string or text in the respective entry fields.
2. **Choose Encoding:** Select the desired encoding from the dropdown menu.
3. **Include/Exclude Spaces and Commas:** Toggle the checkboxes to include or exclude spaces and commas.
4. **Convert:**
   - Click "Convert to Text" to convert binary to text.
   - Click "Convert to Binary" to convert text to binary.
5. **View Result:** The result will be displayed in the "Result" entry field.
6. **Copy to Clipboard:** Click "Copy to Clipboard" to copy the result to your clipboard.
7. **Clear Fields:** Click "Clear Fields" to reset all input and output fields.

## Load Data from Files

- **Load Binary from File:** Click "Load Binary from File" to load binary data from a file.
- **Load Text from File:** Click "Load Text from File" to load text data from a file.

## Dependencies

This script uses the following Python libraries:

- **tkinter**: GUI library for creating the graphical interface.
- **encodings**: Standard library for handling character encodings.

## How to Run

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```
Ensure you have Python installed on your system. Run the script by executing the following command in your terminal:
```bash
python run.py
```

## Notes

- The script handles different character encodings, and you can choose the appropriate encoding from the dropdown menu.
- The default encoding is set to UTF-8.
- The script includes options to preserve spaces and commas in the binary output.

## Reporting Issues

If you encounter any bugs, issues, or have suggestions, please open an issue on the [GitHub repository](https://github.com/Athallah1234/Binary-Converter/issues). Provide detailed information about the problem, including steps to reproduce it.

## Frequently Asked Questions (FAQ)

### What is the Binary Converter?
The Binary Converter is a tool that allows users to convert text to binary and vice versa. It supports various encodings and provides options to include spaces and commas in the binary representation.

### How do I use the Binary Converter?
- **Text to Binary:** Enter your text in the "Enter Text" field, choose the desired options, and click the "Convert to Binary" button.
- **Binary to Text:** Enter your binary in the "Enter Binary" field, choose the desired options, and click the "Convert to Text" button.

### What platforms does the Binary Converter support?
The Binary Converter is a Python-based tool with a Tkinter GUI, making it compatible with Windows, macOS, and Linux.

### Is the Binary Converter available as a standalone application?
As of now, the Binary Converter is distributed as a Python script. Users can run it directly, provided they have Python installed on their system.

### Can I include spaces and commas in the binary output?
Yes, you can choose to include spaces and commas in the binary representation by selecting the corresponding options.

### The GUI is not responding. What should I do?
If the GUI becomes unresponsive, try restarting the application. If the issue persists, check your system resources and ensure that your Python environment is set up correctly.

### I'm having trouble with character encoding. How can I fix it?
Ensure that you're using the correct encoding for your text input. If the issue persists, try using a different encoding or check for special characters that might be causing problems.

### I loaded a file, but the content is not displaying correctly. What should I do?
Ensure that the file you loaded contains valid binary or text data. The tool may not display the content correctly if the file format is not supported.

### I encountered an error while converting. What could be the issue?
If you encounter errors during conversion, double-check your input. For text-to-binary conversion, ensure that the text is valid for the chosen encoding. For binary-to-text conversion, make sure the binary input is valid.

### Can I copy the results to the clipboard?
Yes, you can use the "Copy to Clipboard" button to copy the conversion results to the clipboard.

### Is there a way to load binary or text from a file?
Yes, you can use the "Load Binary from File" and "Load Text from File" buttons to load binary or text data from a file.

### What encodings are supported by the Binary Converter?
The Binary Converter supports a variety of encodings. You can choose the desired encoding from the "Encoding" dropdown menu, which includes options such as UTF-8, ASCII, and more.

### What happens if I choose an invalid encoding?
If you choose an invalid encoding, the tool will attempt to handle the conversion using the specified encoding. However, results may vary, and it's recommended to use a valid encoding for accurate conversions.

### Can I contribute to the Binary Converter project?
Yes, contributions are welcome! Feel free to submit issues, pull requests, or contribute to the development of the Binary Converter.

### What programming language and libraries were used to build this tool?
The Binary Converter is built using Python and the Tkinter library for the graphical user interface.

### Is my data secure when using the Binary Converter?
The Binary Converter processes data locally on your machine and doesn't send any information over the internet. However, exercise caution when dealing with sensitive information.

### Can I trust the Binary Converter with confidential data?
While the tool is designed for general use, it's recommended not to use it with sensitive or confidential data. Always exercise caution and consider the nature of your data before using any third-party tool.

### Are there any external libraries or tools used in the Binary Converter?
The Binary Converter uses standard Python libraries for its functionality. No external dependencies are required.

## Contribute

If you wish to contribute to this project, please follow these steps:

1. **Fork the Repository**
   - Fork this repository to your GitHub account.
2. **Clone the Repository**
   - Clone the forked repository to your local machine.
     ```bash
     git clone https://github.com/Athallah1234/Binary-Converter.git
     ```
3. **Create a Branch**
   - Create a new branch for your work.
     ```bash
     git checkout -b branch-name
     ```
4. **Make Changes**
   - Make the necessary changes and ensure to follow the code style guidelines.
5. **Test Changes**
   - Make sure to test your changes before submitting a pull request.
6. **Submit a Pull Request**
   - Submit a pull request to the main repository with a brief description of the changes 

## License

This Binary Converter script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the contributors and the open-source community for their support and contributions to this project.

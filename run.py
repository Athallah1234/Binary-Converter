import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import encodings

def binary_to_text(binary_str, encoding='ascii', include_spaces=True, include_commas=True):
    try:
        binary_values = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        if include_spaces:
            binary_values = [val if val != '00100000' else '00100000' for val in binary_values]  # Preserve space
        if include_commas:
            binary_values = [val if val != '00101100' else '00101100' for val in binary_values]  # Preserve comma
        text = ''.join(chr(int(val, 2)) for val in binary_values)
        return text
    except ValueError:
        return "Invalid binary input"

def text_to_binary(text, encoding='ascii', include_spaces=True, include_commas=True):
    try:
        binary_str = ''.join(format(ord(char), '08b') for char in text)
        if include_spaces:
            binary_str = ' '.join([binary_str[i:i+8] for i in range(0, len(binary_str), 8)])
        if include_commas:
            binary_str = ','.join([binary_str[i:i+8] for i in range(0, len(binary_str), 8)])
        return binary_str
    except UnicodeDecodeError:
        return "Invalid text input"

def load_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as file:
            content = file.read()
            entry.delete(0, tk.END)
            entry.insert(tk.END, content.decode('utf-8', 'replace'))

def convert_binary():
    binary_str = binary_entry.get()
    encoding = encoding_var.get()
    include_spaces = include_spaces_var.get()
    include_commas = include_commas_var.get()

    if not include_spaces:
        binary_str = binary_str.replace(' ', '')
    if not include_commas:
        binary_str = binary_str.replace(',', '')

    result_text.set(binary_to_text(binary_str, encoding, include_spaces, include_commas))

def convert_text():
    text_input = text_entry.get()
    encoding = encoding_var.get()
    include_spaces = include_spaces_var.get()
    include_commas = include_commas_var.get()

    result_text.set(text_to_binary(text_input, encoding, include_spaces, include_commas))

def clear_fields():
    binary_entry.delete(0, tk.END)
    text_entry.delete(0, tk.END)
    result_text.set("")

def copy_to_clipboard():
    result = result_text.get()
    if result:
        app.clipboard_clear()
        app.clipboard_append(result)
        app.update()  # required for macOS
        tkinter.messagebox.showinfo("Copied", "Result copied to clipboard!")

# Get a list of available encodings
available_encodings = sorted([enc for enc in encodings.aliases.aliases.keys()])

# Create the main window
app = tk.Tk()
app.title("Binary Converter")

# Disable window resizing
app.resizable(False, False)

# Create and configure widgets
binary_label = tk.Label(app, text="Enter Binary:")
binary_entry = tk.Entry(app, width=40)
convert_binary_button = tk.Button(app, text="Convert to Text", command=convert_binary)

text_label = tk.Label(app, text="Enter Text:")
text_entry = tk.Entry(app, width=40)
convert_text_button = tk.Button(app, text="Convert to Binary", command=convert_text)

result_label = tk.Label(app, text="Result:")
result_text = tk.StringVar()
result_entry = tk.Entry(app, textvariable=result_text, state="readonly", width=40)

encoding_var = tk.StringVar(value='utf-8')  # Default encoding is set to utf-8
encoding_label = tk.Label(app, text="Encoding:")
encoding_menu = tk.OptionMenu(app, encoding_var, *available_encodings)

include_spaces_var = tk.BooleanVar(value=True)
include_spaces_checkbutton = tk.Checkbutton(app, text="Include Spaces", variable=include_spaces_var)

include_commas_var = tk.BooleanVar(value=True)
include_commas_checkbutton = tk.Checkbutton(app, text="Include Commas", variable=include_commas_var)

copy_button = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
clear_button = tk.Button(app, text="Clear Fields", command=clear_fields)

load_binary_button = tk.Button(app, text="Load Binary from File", command=lambda: load_file(binary_entry))
load_text_button = tk.Button(app, text="Load Text from File", command=lambda: load_file(text_entry))

# Organize widgets using grid layout
binary_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
binary_entry.grid(row=0, column=1, padx=10, pady=10)
convert_binary_button.grid(row=1, column=0, columnspan=2, pady=10)

text_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
text_entry.grid(row=2, column=1, padx=10, pady=10)
convert_text_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
result_entry.grid(row=4, column=1, padx=10, pady=10)

encoding_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
encoding_menu.grid(row=5, column=1, padx=10, pady=10, sticky="w")

include_spaces_checkbutton.grid(row=6, column=0, columnspan=2, pady=10)
include_commas_checkbutton.grid(row=7, column=0, columnspan=2, pady=10)

copy_button.grid(row=8, column=0, pady=10)
clear_button.grid(row=8, column=1, pady=10)

load_binary_button.grid(row=9, column=0, pady=10)
load_text_button.grid(row=9, column=1, pady=10)

# Start the main event loop
app.mainloop()


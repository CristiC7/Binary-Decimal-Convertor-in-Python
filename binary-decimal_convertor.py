import tkinter as tk  # Import the Tkinter module for GUI

# Function to convert a decimal number to binary
def decimal_to_binary():
    try:
        decimal_num = int(input_field.get())  # Get the input from the user and convert it to an integer
        binary_num = bin(decimal_num).replace("0b", "")  # Convert to binary and remove the "0b" prefix
        output_label.config(text=f"Binary: {binary_num}")  # Display the binary result
    except ValueError:
        output_label.config(text="Invalid input. Please enter a decimal number.")  # Handle invalid input

# Function to convert a binary number to decimal
def binary_to_decimal():
    try:
        binary_num = input_field.get()  # Get the input from the user
        decimal_num = int(binary_num, 2)  # Convert binary to decimal
        output_label.config(text=f"Decimal: {decimal_num}")  # Display the decimal result
    except ValueError:
        output_label.config(text="Invalid input. Please enter a valid binary number.")  # Handle invalid input

# Function to clear the output label
def clear_output():
    output_label.config(text="")  # Reset the output label text

# Create the main window
root = tk.Tk()
root.title("Binary-Decimal Converter")  # Set window title

# Create a frame to hold the buttons
menu_frame = tk.Frame(root)
menu_frame.pack()

# Create a button to convert decimal to binary
decimal_to_binary_button = tk.Button(menu_frame, text="Decimal to Binary", command=decimal_to_binary)
decimal_to_binary_button.pack(side=tk.LEFT)  # Align button to the left

# Create a button to convert binary to decimal
binary_to_decimal_button = tk.Button(menu_frame, text="Binary to Decimal", command=binary_to_decimal)
binary_to_decimal_button.pack(side=tk.LEFT)  # Align button to the left

# Create a button to clear the output
clear_button = tk.Button(root, text="Clear", command=clear_output)
clear_button.pack()

# Create an input field for the user to enter numbers
input_field = tk.Entry(root)
input_field.pack()

# Placeholder for a convert button (currently not functional)
convert_button = tk.Button(root, text="Convert", command=lambda: None)
convert_button.pack()

# Label to display conversion results
output_label = tk.Label(root, text="", pady=10)
output_label.pack()

# Run the Tkinter event loop
root.mainloop()

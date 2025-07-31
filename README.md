# 🔁 Binary–Decimal Converter in Python (Tkinter GUI)

This Python application provides a simple graphical interface using **Tkinter** that allows users to convert numbers between **decimal** and **binary** systems.

It is designed to be beginner-friendly, efficient, and lightweight.

---

## 🧠 Features

### 🔹 Decimal to Binary
✅ Enter a **decimal number** in the input field

✅ Click **"Decimal to Binary"**

✅ The app converts the value to binary and displays the result

### 🔹 Binary to Decimal
✅ Enter a **binary number** (e.g., `1010`)

✅ Click **"Binary to Decimal"**

✅ The app converts it to decimal and displays the result

### 🔹 Clear Output
- Click the **"Clear"** button to remove any displayed results

### 🔹 GUI Layout
- Input field (`Entry`) for user input
- Result label (`Label`) for showing conversions
- Three buttons:
  - **Decimal to Binary**
  - **Binary to Decimal**
  - **Clear**
- An additional **"Convert"** button is present but currently inactive

---

## ⚙️ How It Works

- `decimal_to_binary()`  
  Converts decimal input to binary using Python's built-in `bin()` function

- `binary_to_decimal()`  
  Converts binary input to decimal using `int(binary, 2)`

- `clear_output()`  
  Resets the result label to an empty string

- **Error Handling**  
  Displays an appropriate error message if the input is invalid (e.g., contains letters)

---

## ▶️ How to Run

1. Make sure you have **Python 3** installed
2. Save the file as `binary-decimal_convertor.py`
3. Run it using:

```bash
python binary-decimal_convertor.py
```

---
## 💡 Future Improvements
Enable the Convert button to detect input type automatically

Add better input validation (only digits, max length, etc.)

Enhance the GUI design (colors, layout, fonts)

Add conversion history

---

👨‍💻 Author
Created by CristiC7
A beginner-friendly utility tool built with love for Python and user-friendly design.

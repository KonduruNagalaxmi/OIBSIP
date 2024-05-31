import string
import random
import tkinter as tk
import pyperclip

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("500x400")

        # Create input fields and options
        self.length_label = tk.Label(self, text="Password Length:")
        self.length_label.pack()
        self.length_entry = tk.Entry(self)
        self.length_entry.pack()

        self.complexity_label = tk.Label(self, text="Password Complexity:")
        self.complexity_label.pack()
        self.complexity_var = tk.StringVar()
        self.complexity_options = ["Low", "Medium", "High"]
        self.complexity_dropdown = tk.OptionMenu(self, self.complexity_var, *self.complexity_options)
        self.complexity_dropdown.pack()

        self.include_uppercase = tk.BooleanVar()
        self.uppercase_checkbox = tk.Checkbutton(self, text="Include Uppercase", variable=self.include_uppercase)
        self.uppercase_checkbox.pack()

        self.include_lowercase = tk.BooleanVar()
        self.lowercase_checkbox = tk.Checkbutton(self, text="Include Lowercase", variable=self.include_lowercase)
        self.lowercase_checkbox.pack()

        self.include_digits = tk.BooleanVar()
        self.digits_checkbox = tk.Checkbutton(self, text="Include Digits", variable=self.include_digits)
        self.digits_checkbox.pack()

        self.include_special = tk.BooleanVar()
        self.special_checkbox = tk.Checkbutton(self, text="Include Special Characters", variable=self.include_special)
        self.special_checkbox.pack()

        self.generate_button = tk.Button(self, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(self, text="")
        self.password_label.pack()

        self.copy_button = tk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()

    def generate_password(self):
        # Get user input
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()

        # Define character sets
        characters = string.ascii_letters + string.digits + string.punctuation
        if complexity == "Low":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits

        # Generate password
        password = ''.join(random.choice(characters) for i in range(length))

        # Display the password
        self.password_label.config(text=f"Your password is: {password}")

    def copy_to_clipboard(self):
        pyperclip.copy(self.password_label.cget("text").split(": ")[1])
        self.password_label.config(text="Password copied to clipboard!")

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
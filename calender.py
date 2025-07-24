import tkinter as tk
from tkinter import messagebox
import calendar

# Function to display calendar in the same window
def show_calendar():
    try:
        year = int(year_entry.get())
        cal_output = calendar.TextCalendar(calendar.SUNDAY).formatyear(year, 2, 1, 1, 3)
        calendar_text.config(state='normal')  # Enable editing to update text
        calendar_text.delete('1.0', tk.END)   # Clear previous content
        calendar_text.insert(tk.END, cal_output)
        calendar_text.config(state='disabled')  # Make it read-only again
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid year (e.g., 2025)")

# GUI setup
root = tk.Tk()
root.title("📅 Calendar Viewer")
root.geometry("600x600")
root.configure(bg="#f0f0f0")

# Title
title_label = tk.Label(root, text="📅 Yearly Calendar", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Frame for user input
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

year_label = tk.Label(input_frame, text="Enter Year:", font=("Arial", 14), bg="#f0f0f0")
year_label.grid(row=0, column=0, padx=5)

year_entry = tk.Entry(input_frame, font=("Arial", 14), width=10)
year_entry.grid(row=0, column=1, padx=5)

show_button = tk.Button(input_frame, text="Show Calendar", font=("Arial", 12, "bold"),
                        bg="#4CAF50", fg="white", command=show_calendar)
show_button.grid(row=0, column=2, padx=10)

# Calendar display area
calendar_text = tk.Text(root, width=70, height=25, font=("Consolas", 10), bg="#fff", fg="#000")
calendar_text.pack(pady=10)
calendar_text.config(state='disabled')  # Initially read-only

# Exit button
exit_button = tk.Button(root, text="Exit", font=("Arial", 12, "bold"), bg="#f44336", fg="white", command=root.destroy)
exit_button.pack(pady=10)

# Run the GUI loop
root.mainloop()

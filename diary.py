import tkinter as tk
from datetime import datetime

def write_entry():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = text_entry.get("1.0", "end").strip()

    if entry:
        with open("diary.txt", "a") as diary_file:
            diary_file.write(f"{date}: {entry}\n")
        text_entry.delete("1.0", "end")
        status_label.config(text="Entry added successfully!")
    else:
        status_label.config(text="Please write an entry.")

def read_entries():
    with open("diary.txt", "r") as diary_file:
        entries = diary_file.readlines()
    if entries:
        text_entry.delete("1.0", "end")
        for entry in entries:
            text_entry.insert("end", entry)
    else:
        status_label.config(text="No entries found.")

# Create the main application window
window = tk.Tk()
window.title("Diary App")

# Create a text entry widget
text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

# Create a button to write an entry
write_button = tk.Button(window, text="Write Entry", command=write_entry)
write_button.pack()

# Create a button to read entries
read_button = tk.Button(window, text="Read Entries", command=read_entries)
read_button.pack()

# Create a label for status messages
status_label = tk.Label(window, text="")
status_label.pack()

# Start the Tkinter event loop
window.mainloop()

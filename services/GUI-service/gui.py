import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def open_file(entry_widget):
	file_path = filedialog.askopenfilename()
	if file_path:
		entry_widget.config(state="normal")
		entry_widget.delete(0, tk.END)
		entry_widget.insert(0, file_path)
		entry_widget.config(state="readonly")

root = tk.Tk()
root.title("Matrix Multiplier")

root.geometry("600x600+100+100")   # Set window size and position
root.resizable(False, False)  # Disable window resizing


frame = ttk.Frame(root, padding=(20, 20))
frame.pack()


# First file input
label1 = ttk.Label(frame, text="Input your first matrix:", font=("Arial", 12, "bold"))
label1.grid(row=0, column=0, sticky="w")

file_entry1 = ttk.Entry(frame, width=40, state="readonly")
file_entry1.grid(row=1, column=0, padx=(0,10))

browse_button1 = ttk.Button(frame, text="Browse", command=lambda: open_file(file_entry1))
browse_button1.grid(row=1, column=1)

# Second file input
label2 = ttk.Label(frame, text="Input your second matrix:", font=("Arial", 12, "bold"))
label2.grid(row=2, column=0, sticky="w", pady=(15,0))

file_entry2 = ttk.Entry(frame, width=40, state="readonly")
file_entry2.grid(row=3, column=0, padx=(0,10))

browse_button2 = ttk.Button(frame, text="Browse", command=lambda: open_file(file_entry2))
browse_button2.grid(row=3, column=1)

label3 = ttk.Label(frame, text="Calculate Matrix", font=("Arial", 14, "bold"), justify="right")
label3.grid(row=4, column=0, sticky="ew", pady=(15,0))

calculate_button = ttk.Button(frame, text="Calculate", width=20)
calculate_button.grid(row=5, column=0, columnspan=2, pady=(5,0), ipadx=10, ipady=10)

root.mainloop()
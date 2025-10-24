import socket
import json
import os
import sys
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

shared_path = os.path.join(os.path.dirname(__file__), '..', '..', 'shared')
sys.path.insert(0, shared_path)
from message_types import create_gui_message

def open_file(entry_widget):
	file_path = filedialog.askopenfilename()
	if file_path:
		entry_widget.config(state="normal")
		entry_widget.delete(0, tk.END)
		entry_widget.insert(0, file_path)
		entry_widget.config(state="readonly")

def on_calculate():
	# Gather matrices/connect to division service 
	try:
		mat_file1 = file_entry1.get()
		mat_file2 = file_entry2.get()
		if not mat_file1 or not mat_file2:
			matrix1 = np.random.randint(1, 1000, size=(100, 100)).tolist()
			matrix2 = np.random.randint(1, 1000, size=(100, 100)).tolist()
			connect_to_division_service(matrix1, matrix2)
	except Exception as e:
		print(f"Error: {e}")

def connect_to_division_service(mat1, mat2):
	host = 'localhost'
	port = 5001
	message = create_gui_message(mat1, mat2)

	# Create TCP socket
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client_socket.connect((host, port))
		client_socket.sendall(json.dumps(message).encode('utf-8'))

	except Exception as e:
		print(f"Error connecting to Division Service: {e}")

	finally:
	
		client_socket.close()



root = tk.Tk()
root.title("Matrix Multiplier")

root.geometry("600x600+100+100")
root.resizable(False, False)


frame = ttk.Frame(root, padding=(20, 20))
frame.pack()

generate_label = ttk.Label(frame, text="Leave files empty to generate random matrices", font=("Helvetica", 12, "bold"), justify="right")
generate_label.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0,15))

# First file input
label1 = ttk.Label(frame, text="Input your first matrix:", font=("Helvetica", 12, "bold"))
label1.grid(row=1, column=0, sticky="w")

file_entry1 = ttk.Entry(frame, width=40, state="readonly")
file_entry1.grid(row=2, column=0, padx=(0,10))

browse_button1 = ttk.Button(frame, text="Browse", command=lambda: open_file(file_entry1))
browse_button1.grid(row=2, column=1)

# Second file input
label2 = ttk.Label(frame, text="Input your second matrix:", font=("Helvetica", 12, "bold"))
label2.grid(row=3, column=0, sticky="w", pady=(15,0))

file_entry2 = ttk.Entry(frame, width=40, state="readonly")
file_entry2.grid(row=4, column=0, padx=(0,10))

browse_button2 = ttk.Button(frame, text="Browse", command=lambda: open_file(file_entry2))
browse_button2.grid(row=4, column=1)

calc_label = ttk.Label(frame, text="Calculate Matrix", font=("Helvetica", 14, "bold"), justify="right")
calc_label.grid(row=5, column=0, sticky="ew", pady=(15,0))

calculate_button = ttk.Button(frame, text="Calculate", width=20, command=on_calculate)
calculate_button.grid(row=6, column=0, columnspan=2, pady=(5,0), ipadx=10, ipady=10)

root.mainloop()





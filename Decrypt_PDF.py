#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

def decrypt_pdfs(files, password):
    success_count = 0
    for input_pdf in files:
        try:
            # Open the encrypted PDF
            with open(input_pdf, 'rb') as file:
                reader = PyPDF2.PdfReader(file)

                # If the file is encrypted, try to decrypt it with the password
                if reader.is_encrypted:
                    if reader.decrypt(password) == 0:
                        messagebox.showerror("Decryption Failed",
                                             f"Failed to decrypt {input_pdf}: Wrong password!")
                        continue
                
                # Prepare the output filename
                output_pdf = os.path.splitext(input_pdf)[0] + '_decrypted.pdf'
                
                # Create a PdfWriter object to write the decrypted file
                writer = PyPDF2.PdfWriter()
                
                # Add all pages to the writer
                for page_num in range(len(reader.pages)):
                    writer.add_page(reader.pages[page_num])

                # Write the decrypted PDF to a new file
                with open(output_pdf, 'wb') as output_file:
                    writer.write(output_file)

                success_count += 1
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while processing {input_pdf}: {e}")

    messagebox.showinfo("Decryption Complete",
                        f"Successfully decrypted {success_count} out of {len(files)} file(s).")

def select_files():
    # Allow the user to select multiple PDF files
    files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")])
    if files:
        file_list.delete(0, tk.END)  # Clear the listbox
        for file in files:
            file_list.insert(tk.END, file)  # Add the selected files to the listbox

def start_decryption():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter the password.")
        return

    files = file_list.get(0, tk.END)
    if not files:
        messagebox.showwarning("Input Error", "Please select one or more PDF files.")
        return

    decrypt_pdfs(files, password)

# Tkinter App
root = tk.Tk()
root.title("Bulk PDF Decryptor")

# Password label and entry
password_label = tk.Label(root, text="Enter Password:")
password_label.grid(row=0, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=0, column=1, padx=10, pady=10)

# File selection button
file_select_button = tk.Button(root, text="Select PDF Files", command=select_files)
file_select_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Listbox to show selected files
file_list = tk.Listbox(root, width=60, height=10)
file_list.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start decryption button
start_button = tk.Button(root, text="Start Decryption", command=start_decryption)
start_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()


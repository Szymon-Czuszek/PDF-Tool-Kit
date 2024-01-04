#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger
import os

def merge_pdfs():
    # Open a file dialog for the user to select PDF files
    file_paths = filedialog.askopenfilenames(title = "Select PDF files",
                                             filetypes = [("PDF files", "*.pdf")]
                                            )

    if not file_paths:
        return

    # Open a file dialog for the user to choose the destination folder
    dest_folder = filedialog.askdirectory(title = "Select Destination Folder")

    if not dest_folder:
        return

    # Get the desired output PDF file name from the user
    output_name = output_name_entry.get()
    if not output_name:
        output_name = 'merged.pdf'

    # Construct the full path for the output PDF
    output_pdf = os.path.join(dest_folder, output_name)

    # Initialize a PDF merger object
    pdf_merger = PdfMerger()

    try:
        # Append each selected PDF file to the merger object
        for pdf_file in file_paths:
            pdf_merger.append(pdf_file)

        # Write the merged PDF to the output file
        pdf_merger.write(output_pdf)

        # Close the merger object
        pdf_merger.close()

        result_label.config(text = f'Merged PDF saved as {output_pdf}', fg = 'green')
    
    except Exception as e:
        result_label.config(text = f'An error occurred: {str(e)}', fg = 'red')


# In[2]:


if __name__ == "__main__":
    # Create a GUI window
    root = tk.Tk()
    root.title("PDF Merger")

    # Set the window size
    root.geometry("400x300")

    # Create a frame for better organization
    frame = tk.Frame(root)
    frame.pack(pady=20, padx=20, fill='both', expand=True)

    # Create a "Merge PDFs" button with custom styling
    merge_button = tk.Button(frame,
                             text = "Merge PDFs",
                             command=merge_pdfs,
                             bg = 'blue',
                             fg = 'white',
                             font = ('Arial', 12)
                            )
    merge_button.pack(pady=10, padx=10, fill='both')

    # Create a label to display the result with custom styling
    result_label = tk.Label(frame, text="", font=('Arial', 12))
    result_label.pack(pady=10)

    # Create an entry field for specifying the output PDF name with custom styling
    output_name_label = tk.Label(frame, text="Output PDF Name:", font=('Arial', 12))
    output_name_label.pack()
    output_name_entry = tk.Entry(frame, font=('Arial', 12))
    output_name_entry.pack()

    # Start the GUI application
    root.mainloop()


from PyPDF2 import PdfReader, PdfWriter
import os

# Change the path where your pdfs saved
folder_path = r"C:\pdfs" 
pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]

merger = PdfWriter()

for file in pdf_files:
    file_path = os.path.join(folder_path, file)
    reader = PdfReader(file_path)
    for page in reader.pages:
        merger.add_page(page)

# Change output name to your desire name
with open("merged_output.pdf", "wb") as f: 
    merger.write(f)

print("Process succesful")

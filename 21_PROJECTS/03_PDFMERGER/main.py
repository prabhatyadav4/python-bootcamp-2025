from PyPDF2 import PdfWriter  # Import PdfWriter from PyPDF2 to handle PDF merging

merger = PdfWriter()  # Create an instance of PdfWriter
pdfs = []  # Initialize an empty list to store PDF file names
n = int(input("Enter the number of PDFs you want to merge: "))  # Get the number of PDFs to merge from the user

# Loop to collect the names of the PDF files
for i in range(0, n):
    name = input(f"Enter the name of PDF {i+1}: ")  # Prompt user for each PDF file name
    pdfs.append(name)  # Add the file name to the list

# Loop to append each PDF to the merger
for pdf in pdfs:
    merger.append(pdf)  # Append the current PDF to the merger

merger.write("merged-pdf.pdf")  # Write the merged PDF to a new file
merger.close()  # Close the PdfWriter instance
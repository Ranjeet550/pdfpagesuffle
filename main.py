import PyPDF2
import random

# Open the PDF file
pdf_file = open("input.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Create a writer object to save the shuffled pages
pdf_writer = PyPDF2.PdfWriter()

# Get the list of page numbers in random order
page_numbers = list(range(len(pdf_reader.pages)))
random.shuffle(page_numbers)

# Add pages in shuffled order to the new PDF
for page_num in page_numbers:
    page = pdf_reader.pages[page_num]
    pdf_writer.add_page(page)

# Save the shuffled PDF to a new file
with open("shuffled.pdf", "wb") as output_file:
    pdf_writer.write(output_file)

pdf_file.close()

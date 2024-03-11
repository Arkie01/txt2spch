import pyttsx3
import fitz  # PyMuPDF
from tkinter.filedialog import askopenfilename

# Ask user to select a PDF file
book = askopenfilename()

# Open the PDF file using PyMuPDF
pdf_document = fitz.open(book)
pages = pdf_document.page_count

# Initialize the text-to-speech engine
player = pyttsx3.init()

# Iterate through each page and extract text
for page_num in range(pages):
    page = pdf_document[page_num]
    text = page.get_text("text")
    player.say(text)

# Wait for the speech to finish
player.runAndWait()

# Close the PDF document
pdf_document.close()

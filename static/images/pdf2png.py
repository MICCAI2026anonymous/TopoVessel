import fitz  # PyMuPDF is imported as fitz for backward compatibility
import os

for file in os.listdir("."):
    if file.endswith(".pdf"):
        file_path = file
        doc = fitz.open(file_path) # Open the document
        for i, page in enumerate(doc):
            pix = page.get_pixmap() # Render page to an image
            output_filename = f"{file.replace('.pdf', '')}.png"
            pix.save(output_filename) # Save the image to a PNG file
        doc.close() # Close the document
        # print(f"Converted {len(doc)} pages to PNG images.")

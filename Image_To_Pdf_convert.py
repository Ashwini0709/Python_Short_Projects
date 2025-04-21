#!/usr/bin/env python


#Using img2pdf library
#Importing neccessary libraries
#pip install pillow and pip install img2pdf


import img2pdf
from PIL import Image
import os


#Storing image path
img_path = "image.png"

#Storing pdf path
pdf_path = "file_pdf.pdf"

#opening image
image = Image.open(img_path)

#Converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)


#opening and creating pdf file
file = open(pdf_path, "wb")

file.write(pdf_bytes)

image.close()

print("Successfully made pdf file")






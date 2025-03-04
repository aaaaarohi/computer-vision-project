import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Read text from the image
#image_path = "path/to/your/image.jpg"  
# Replace with your image path
results = reader.readtext(img)

# Extract text and store it in a variable
extracted_text = " ".join([text[1] for text in results])


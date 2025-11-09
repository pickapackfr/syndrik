from pypdf import PdfReader

reader = PdfReader('data/AlexandrePerez.pdf')

# printing number of pages in pdf file
print(len(reader.pages))

text = ""

# getting a specific page from the pdf file
for page in reader.pages:
    text += page.extract_text()

print(text)
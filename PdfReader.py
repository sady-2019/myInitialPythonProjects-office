import pdfplumber
from gtts import gTTS

language="bn"
pdf_path=  "sapiens.pdf"
pdf= pdfplumber.open(pdf_path)
page= pdf.pages[150]
text= page.extract_text()
print(text)
pdf.close()


gtts_transformer= gTTS(text=text,lang=language)
gtts_transformer.save("ab.mp3")
print("Done")
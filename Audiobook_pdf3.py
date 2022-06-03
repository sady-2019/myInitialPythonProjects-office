import pyttsx3
import PyPDF2

book= open("poyla.pdf","rb")
pdfReader= PyPDF2.PdfFileReader(book)
total_pages=pdfReader.numPages
print(total_pages)


speaker= pyttsx3.init()
for num in range (14,total_pages):
    page= pdfReader.getPage ()
    text= page.extractText()

    speaker.say(text)
    speaker.runAndWait()
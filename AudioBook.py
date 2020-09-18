import pyttsx3
import PyPDF2

pdf = open('pcm.pdf','rb') # initializing pdf
pdfReader = PyPDF2.PdfFileReader(pdf) # pdf is ready to read
pages = pdfReader.numPages # counting pages

speak = pyttsx3.init() # initializing to speaking
for i in range(0,pages):
    page = pdfReader.getPage(i) # opening ith page
    text = page.extractText() # extracting text from the pdf
    speak.say(text) # text are ready to speak
    speak.runAndWait() # starting speaking


# ========== just read a text ========== 
# speak = pyttsx3.init()
# speak.say('read this text')
# speak.runAndWait() 
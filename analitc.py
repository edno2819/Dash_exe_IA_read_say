import pytesseract
import pyttsx3
from PIL import Image
from urllib.request import urlopen
from utils import consult_csv
import time


configs = consult_csv()

teller = pyttsx3.init()
pytesseract.pytesseract.tesseract_cmd = configs['PATH_TE'][0]

class Analytics:

    LANG = 'eng'
    VOICE={}
    VOICE['eng'] = configs['PATH_EN'][0]
    VOICE['por'] = configs['PATH_PT'][0]
    def read(self, path):
        #img = Image.open(path)
        img = Image.open(urlopen(path))
        text = pytesseract.image_to_string(img, lang=None)
        return text

    def say(self, text):
        teller.setProperty('voice', self.VOICE[self.LANG])
        teller.setProperty('rate', 150)
        teller.setProperty('volume', 1)

        path = f'assets/audio{time.time()}.wav'
        #teller.say(text)
        teller.save_to_file(text, path)
        teller.runAndWait()
        return path




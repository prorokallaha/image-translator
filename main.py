import cv2
import pytesseract
import googletrans
from art import tprint
from fpdf import FPDF 


def translate_image():
    image = input('''[+] Hello. If you first enter the name of the file and extension (.jpg, .png)
    That you want to translate (be sure that it is in the same directory as the script) - ''')
    try:
        img = cv2.imread(image)
    except:
        print('[-] Incorrectly entered data.')
    text = pytesseract.image_to_string(img)
    text = text.split('\n')
    text = ' '.join(text)
    print("[+] Processing...") 
    
    translator = googletrans.Translator()
    text_language = translator.detect(text)
    print(f'[+] {text_language}')
    language = input('[+] Choose the language you want to translate into (pl - polish, uk - ukrainian, de - german, en - english, ru - russian) - ')
    # pl - polish, uk - ukrainian, de - german, en - english, rus - russian, th
    trans_text = None
    try:
        trans_text = translator.translate(text, dest=language)
        trans_text = trans_text.text
    except:
        print('[-] Wrong language entered.')
    
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("Noto", "Light", "NotoSans-Light.ttf", uni=True)
    pdf.set_font('Noto','Light',14)
    pdf.write(h=10 ,txt=trans_text)
    pdf.output('translate.pdf', 'F')
    print('[+] The script has completed its work. A file named "translator.pdf" appeared in this directory.')



def main():
    tprint('<< IMAGE - TRANSLATOR >>',  font='bulbhead')
    translate_image()

if __name__ == "__main__":
    main()



__author__ = " Shubham Kumar "

'''To read text from images, install tesseract and pytesseract.'''
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

'''Setting tesseract location manually in Windows.'''


# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename), lang='eng')
    if text == "":
        return None
    return text


if __name__ == "__main__":
    print(ocr_core('./test.png'))

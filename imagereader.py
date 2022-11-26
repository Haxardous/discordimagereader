from PIL import Image
from pytesseract import pytesseract
import requests
from messages import *

# path where tesseract is installed in.
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def read_image_text(link):
    img_path = "cache.jpg"
    img_data = requests.get(link).content
    with open(img_path, 'wb') as handler:
        handler.write(img_data)

    pytesseract.tesseract_cmd = path_to_tesseract
    img = Image.open(img_path)
    text = pytesseract.image_to_string(img)
    print("found text: " + text)
    return check_message_content(text)


def check_message_content(text):
    messages_agenda = get_messages_agenda_dict()
    for message in messages_agenda:
        for keyword in messages_agenda[message]["keywords"]:
            if keyword in text:
                # check if the keywords has an alt
                if not messages_agenda[message]["alt_message"] == "":
                    alt_message = messages_agenda[message]["alt_message"]
                    for alt_keyword in messages_agenda[alt_message]["keywords"]:
                        if alt_keyword in text:
                            return alt_message
                        else:
                            return message
                else:
                    return message

    return "Nothing"

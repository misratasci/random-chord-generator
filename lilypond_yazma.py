import os
from PIL import Image

def prepare_note_img(notes):
    ly_file = open("test.ly","r")
    lines = ly_file.readlines()
    
    note_str = ""
    for note in notes:
        note_str += note
        note_str += " "
    note_line = "   <" + note_str + ">\n"
    lines[2] = note_line
    ly_file.close()

    ly_file = open("test.ly", "w")
    text = "".join(lines)
    ly_file.write(text)
    ly_file.close()
    os.system("lilypond -dmidi-extension=mid -fpng test.ly") 
    im = Image.open("test.png")
    croppedimg = im.crop((80,10,220,100))
    croppedimg.save("cropped.png")
    


from tkinter import *
from tkinter import ttk
from note import aralık_dict, Note, Notes
from random import choice
from lilypond_yazma import prepare_note_img
from PIL import ImageTk, Image
import pygame
from itertools import combinations

root = Tk()
root.title("Rastgele Akor Yapıcı")

entryframe = ttk.Frame(root, padding="3 3 12 12")
entryframe.grid(column=0, row=0)

yönerge = ttk.Label(entryframe, text="Hangi aralıktan kaç tane olsun?")
yönerge.grid(column=1, columnspan=2, row=2)

aralıklar_ve_no = {"sharp_diss": 0, "mild_diss": 0, "soft_cons": 0, "open_cons": 0, "T4": 0, "aug4": 0}
i=3
entries = []
for aralık in aralıklar_ve_no:
    ttk.Label(entryframe, text=aralık).grid(column=1, row=i)
    entry = ttk.Entry(entryframe, width=5)
    entries.append(entry)
    entry.grid(column=2, row=i)
    i += 1

def go():
    i = 0
    for aralık in aralıklar_ve_no:
        aralıklar_ve_no[aralık] = entries[i].get()
        i += 1
    kök = choice(Notes().list)
    aralık_değerleri = []
    for aralık in aralıklar_ve_no:
        if aralıklar_ve_no[aralık] == "": continue
        for i in range(int(aralıklar_ve_no[aralık])):
            aralık_değerleri.append(choice(aralık_dict[aralık]))
    notalar = [kök.str]
    for değer in aralık_değerleri:
        notalar.append((kök+değer).str)
    prepare_note_img(notalar)
    root.photo = ImageTk.PhotoImage(Image.open("cropped.png"))
    img_label = ttk.Label(outputframe, image=root.photo)
    img_label.grid(row=0)

    yeni_gelen_değerler = []
    for ikili in combinations(aralık_değerleri, 2):
        yeni_gelen_değerler.append(abs(ikili[1]-ikili[0]))
    print(yeni_gelen_değerler)
    for değer in yeni_gelen_değerler:
        for key in aralık_dict:
            if değer in aralık_dict[key]:
                if aralıklar_ve_no[key] == "": aralıklar_ve_no[key] = "1"
                else: aralıklar_ve_no[key] = str(int(aralıklar_ve_no[key])+1)
    print(aralıklar_ve_no)
    for i in range(len(entries)):
        entries[i].delete(0)
        entries[i].insert(0, list(aralıklar_ve_no.values())[i])
    print(list(aralıklar_ve_no.values()))



go_button = ttk.Button(entryframe, text="Go", width=5, command=go)
go_button.grid(column=2, row=len(aralıklar_ve_no)+3)


outputframe = ttk.Frame(root, padding="3 3 12 12")
outputframe.grid(column=1, row=0)

def play():
    pygame.init()
    pygame.mixer.music.load("test.mid")
    pygame.mixer.music.play(0)

play_button = ttk.Button(outputframe, text="Play", width=5, command=play)
play_button.grid(row=1)

for child in entryframe.winfo_children(): child.grid_configure(padx=3, pady=3, sticky=W)
go_button.grid_configure(sticky=E)
play_button.grid_configure(sticky=(E))
root.mainloop()

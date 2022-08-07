from random import choice
class Note():
    def __init__(self, note):
        self.str = note
        self.is_diyez = False
        self.oktav = self.str.count("'")
        #do0, re1, mi2, fa3, sol4, la5, si6 (inş)
        self.index = ord(self.str[0]) - 99
        while self.index < 0: self.index += 7
    def __repr__(self):
        return self.str
    def raise_note_harf(self):
        strlist = list(self.str)
        char_int = ord(self.str[0]) + 1
        #g olduktan sonra a ya geri dönsün diye:
        while char_int >= 104:
            char_int -= 7
        strlist[0] = chr(char_int)
        newnote = Note("".join(strlist))
        return newnote
    def go_to_next_octave(self):
        strlist = list(self.str)
        strlist.append("'")
        newnote = Note("".join(strlist))
        return newnote
    def raise_note_by_half(self):
        if self.is_diyez == False:
            if self.str[0] == "e" or self.str[0] == "b":
                newnote = self.raise_note_harf()
                if self.str[0] == "b":
                    newnote = newnote.go_to_next_octave()
            else:
                newnote = self.diyez()
        else:
            newnote = self.raise_note_harf()
            newnote = newnote.bekar()
        return newnote
    def diyez(self):
        strlist = list(self.str)
        strlist.insert(1, "is")
        newstr = "".join(strlist)
        newnote = Note(newstr)
        newnote.is_diyez = True
        return newnote
    def bekar(self):
        strlist = list(self.str)
        strlist.remove("i")
        strlist.remove("s")
        newstr = "".join(strlist)
        newnote = Note(newstr)
        newnote.is_diyez = False
        return newnote
    """
    def bemol(self):
        strlist = list(self.str)
        strlist.insert(1, "es")
        newstr = "".join(strlist)
        return Note(newstr)
    """
    def __add__(self, aralık):
        newnote = self
        for i in range(int(aralık*2)):
            newnote = newnote.raise_note_by_half()
        return newnote
    def __gt__(self, other):
        if self.oktav != other.oktav:
            return self.oktav > other.oktav
        elif self.str[0] != other.str[0]:
            return self.index > other.index
        else:
            return self.is_diyez


class Notes():
    def __init__(self, aralık = ("c'", "b'")):
        self.aralık = aralık
        self.min = Note(self.aralık[0])
        self.max = Note(self.aralık[1]) 
        current_note = Note(self.aralık[0])
        self.list = [current_note]
        while current_note.str != self.aralık[1]:
            current_note = current_note.raise_note_by_half()
            self.list.append(current_note)
    def __str__(self):
        string = ""
        for note in self.list:
            string += note.str
            string += " "
        return string


#aralıklar arasında kaç ses olduğu
aralık_dict = {
    "sharp_diss": [0.5, 5.5],
    "mild_diss": [1, 5],
    "soft_cons": [1.5, 2, 4, 4.5],
    "open_cons": [3.5, 6],
    "T4": [2.5],
    "aug4": [3]
}


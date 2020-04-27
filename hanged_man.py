from random import *
from tkinter import *
table = open("liste_mots.txt", "rt").read().split()

def nombre_mots():
    return len(table)

def mot_choisi():
    return table[randint(1, nombre_mots())]

class game:
    label = ""
    current = ""
    def __init__(self):
        main_canvas.config()
        word.replace = word.star()

class main_canvas:
    title = "Le pendu"
    internal = 0
    int_text = ""
    def config():
        PENDU=Tk()
        PENDU.title(main_canvas.title)
        PENDU.configure(bg="grey",width=600,heigh=450)
        dessin=Canvas(PENDU,bg="white",width=200,height=350)
        dessin.place(x=50,y=50)
        def ne_xt():
            if main_canvas.internal == 0:
                dessin.create_line(30,320,30,25,fill="brown",width="2")
                dessin.create_line(10,320,50,320,fill="brown",width="2")
                dessin.create_line(28,25,120,25,fill="brown",width="2")
                dessin.create_line(30,70,80,25,fill="brown",width="2")
                dessin.create_line(118,94,118,25,fill="grey",width="2")
                dessin.update()
            elif main_canvas.internal == 1:
                dessin.create_oval(105,120,130,92,width="2")
                dessin.update()
            elif main_canvas.internal == 2:
                dessin.create_line(119,120,118,200,width="2")
                dessin.update()
            elif main_canvas.internal == 3:
                dessin.create_line(120,130,150,110,width="2")
                dessin.update()
            elif main_canvas.internal == 4:
                dessin.create_line(120,130,81,110,width="2")
                dessin.update()
            elif main_canvas.internal == 5:
                dessin.create_line(90,230,118,200,width="2")
                dessin.update()
            elif main_canvas.internal == 6:
                dessin.create_line(150,230,118,200,width="2")
                dessin.update()
                main_canvas.int_text="PERDU"
                Label(PENDU,text=main_canvas.int_text).place(x=130,y=400)
                print(word().mot)
            main_canvas.internal += 1
        if "-" in word().mot:
            stat = "contient"
        else:
            stat = "ne contient pas de"
            forma_t = "Ce mot "+stat+" caractère spécial"
            Label(PENDU,text=forma_t).place(x=300,y=400)
        def valid():
            if word.replace.count("*")>0:
               if word.demande(Lettre.get()) == False:
                    ne_xt()
               else:
                    game.label = game.current
                    label.config(text = game.label)
            else:
                main_canvas.int_text="Gagné"
                Label(PENDU,text=main_canvas.int_text).place(x=130,y=400)
        label = Label(PENDU,text=game.label)
        label.place(x=400,y=100)
        Lettre=Entry(PENDU) #au secour je suis fatigué
        Lettre.place(x=0,y=425)
        Button(PENDU,text="Valider",command=valid).place(x=200,y=425)
        PENDU.mainloop
  
class word:
    choice = mot_choisi()
    fail = 0
    f_max = 6
    replace = ""
    def __init__(self):
        self.mot = word.choice
        self.len = len(self.mot)
    def star():
        mot = "*"
        for a in range(word().len-1):
            mot += "*"
        return mot
    def demande(letter):
        if letter == "":
            print("Entrez une lettre !")
        elif letter.upper() in word().mot:
            other = list(word().mot)
            word.replace = list(word.replace)
            for i in range(len(word.replace)):
                if other[i] == letter.upper():
                    word.replace[i] = letter
            word.replace = "".join(word.replace)
            game.current = word.replace
            return True
        else:
              return False
    #def result():
        #if word.fail == 6:
            #print("Vous avez perdu! Le mot était: ",word().mot)
        #else:
            #print("Vous avez gagné !")
game()

from tkinter import *

class main_canvas:
    title = "Le pendu"
    internal = 0
    int_text = ""
    def config():
        PENDU=Tk()
        PENDU.title(main_canvas.title)
        PENDU.configure(bg="grey",width=300,heigh=450)
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
            main_canvas.internal += 1
        Button(PENDU,text="SUIVANT",command=ne_xt).place(x=125,y=425)
        PENDU.mainloop
        
main_canvas.config()  


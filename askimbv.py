from tkinter import *
import webbrowser
import Pmw


class MyWindow:

    def __init__(self, win):
        self.ok =False
        self.betale = False
        self.Test = False
        self.oljetest_ = False
        self.lagrebool = False
        self.v = IntVar()
        self.v.set(1)

        self.navn = Label(win, text='NAVN :', font='Helvetica 14 bold')
        self.bilnr = Label(win, text='BIL NR :', font='Helvetica 14 bold')
        self.kommentartxt = Label(win, text='KOMMENTAR', font='Helvetica 14 bold')
        self.guide = Label(
            win, text='SKRIV IN KUNDE INFO OG VELG BETALT ELLER IKKE BETALT!', fg="red", pady=5, font='Helvetica 14 bold')
        self.guide2 = Label(
            win, text='TRYKK IKKE-BETALT FOR Å ENDRE TIL BETALT!', fg="red", pady=5, font='Helvetica 14 bold')
        self.guide3 = Label(
            win, text='SØK PÅ FOLK ( NAVN, BIL NR., BETALT ELLER IKKE, ALT)!', fg="red", pady=5, font='Helvetica 14 bold')
        self.guide4 = Label(
            win, text='SJEKK HVOR MYE OLJE!!!!', fg="red", pady=5, font='Helvetica 14 bold')
        self.kommentar = Text(win, height=6, width=30, bd=3,  font='Helvetica 16 bold')

        self.navnbox = Entry(bd=3,  font='Helvetica 16 bold')
        self.bilnrbox = Entry(bd=3,  font='Helvetica 16 bold')
        self.sokbilbox = Entry(bd=3,  font='Helvetica 16 bold')
        self.oljeboks = Entry(bd=3,  font='Helvetica 16 bold')

        self.rbBetalt = Radiobutton(win, text='BETALT', variable=self.v,
                                    value='1', font='Helvetica 14 bold')
        self.rbUBetalt = Radiobutton(win, text='IKKE-BETALT',
                                     variable=self.v, value='0', font='Helvetica 14 bold')
        self.lagreBtn = Button(win, text='LAGRE', command=lambda: [
            self.writeFile(), self.lagrettilfil(win)], height=5, width=10, font='Helvetica 16 bold')
        self.nullstillBtn = Button(win, text='NULLSTILL',
                                   command=lambda: self.nullstill(), height=5, width=10, font='Helvetica 16 bold')
        self.hist = Button(win, text='HISTORIE', command=lambda: self.historie())
        self.soker = Button(win, text='SØK', command=lambda: self.sokbil(win),
                            font='Helvetica 16 bold')
        self.ub = Button(win, text='IKKE-BETALT', command=lambda: self.ikkebetaltliste(
            win),  font='Helvetica 16 bold')
        self.bt = Button(win, text='BETALT', command=lambda: self.betaltliste(win),
                         font='Helvetica 16 bold')
        self.olj = Button(win, text='OLJE', command=lambda: self.oljesjekk(),
                          font='Helvetica 16 bold')

        self.navn.place(x=10, y=50)
        self.navnbox.place(x=135, y=50)
        self.bilnr.place(x=10, y=100)
        self.bilnrbox.place(x=135, y=100)
        self.kommentartxt.place(x=10, y=200)
        self.kommentar.place(x=135, y=200)
        self.guide.place(x=10, y=10)
        self.guide2.place(x=820, y=50)
        self.guide3.place(x=555, y=365)
        self.guide4.place(x=890, y=600)

        self.rbBetalt.place(x=135, y=150)
        self.rbUBetalt.place(x=235, y=150)

        self.lagreBtn.place(x=135, y=365)
        self.nullstillBtn.place(x=285, y=365)
        self.hist.place(x=10, y=510)
        self.sokbilbox.place(x=640, y=410)
        self.soker.place(x=555, y=408)
        self.ub.place(x=650, y=50)
        self.bt.place(x=550, y=50)
        self.olj.place(x=550, y=598)
        self.oljeboks.place(x=640, y=600)

    def writeFile(self):
        file = open('historie.html', 'a+')
        file.write(""" <p style="color: red; font-family: 'Liberation Sans',sans-serif"> NAVN: </p>  """ + self.navnbox.get()
                   + """ <p style="color: red; font-family: 'Liberation Sans',sans-serif"> BIL NR: </p> """ + self.bilnrbox.get()
                   + """ <p style="color: red; font-family: 'Liberation Sans',sans-serif"> PRIS: </p> """ +
                   "{}".format(self.v.get())
                   + """ <p style="color: red; font-family: 'Liberation Sans',sans-serif"> KOMMENTAR </p> """ + self.kommentar.get('1.0', END))
        file.close()
        file = open('liste.txt', 'a+')
        file.write("- " + self.navnbox.get() + " " + self.bilnrbox.get() + " " + "betalt:" + "{}".format("JA" if (self.v.get() == 1) else "NEI") +
                   " " + self.kommentar.get('1.0', END))
        file.close()

    def lagrettilfil(self, win):
        if self.ok:
            self.lagret.destroy()

        self.lagret = Label(win, text='LAGRET', bg="GREEN", bd=3, font='Helvetica 16 bold')
        self.lagret.place(x=30, y=365)
        self.ok = True

    def lagrebetalt(self):
        if self.lagrebool:
            self.lagreb.destroy()
            self.lagrebool = False
        with open("liste.txt", "w") as f:
            f.write(self.text.get('1.0', 'end-1c'))
        if self.betale:
            self.text.destroy()
            self.betale = False

    def ikkebetaltliste(self, win):
        if self.betale:
            self.text.destroy()
        if self.lagrebool:
            self.lagreb.destroy()
        self.betale = True
        self.lagrebool = True
        self.lagreb = Button(
            win, text='LAGRE', command=lambda: self.lagrebetalt(), font='Helvetica 16 bold')
        self.text = Pmw.ScrolledText(win,
                                     borderframe=5,
                                     vscrollmode='dynamic',
                                     hscrollmode='dynamic',
                                     labelpos='n',
                                     label_text='ALLE:',
                                     text_width=50,
                                     text_height=9,
                                     text_wrap='none',
                                     text_font='Helvetica 16 bold')
        self.text.tag_config('warning', background="yellow", foreground="red")
        with open('liste.txt') as my_file:
            for line in my_file:
                if "betalt:NEI" in line:
                    print(line)
                    self.text.insert('end', line, 'warning')
                else:
                    self.text.insert('end', line)

        self.text.place(x=580, y=100)
        self.lagreb.place(x=480, y=150)

    def betaltliste(self, win):
        if self.betale:
            self.text.destroy()
        if self.lagrebool:
            self.lagreb.destroy()
            self.lagrebool = False
        self.betale = True
        self.text = Pmw.ScrolledText(win,
                                     borderframe=5,
                                     vscrollmode='dynamic',
                                     hscrollmode='dynamic',
                                     labelpos='n',
                                     label_text='IKKE BETALT:',
                                     text_width=50,
                                     text_height=9,
                                     text_wrap='none',
                                     text_font='Helvetica 16 bold')
        with open('liste.txt') as my_file:
            for line in my_file:
                if "betalt:JA" in line:
                    self.text.insert('end', line)
        self.text.place(x=580, y=100)

    def nullstill(self):
        self.navnbox.delete(0, END)
        self.bilnrbox.delete(0, END)
        self.sokbilbox.delete(0, END)
        self.kommentar.delete('1.0', END)
        if self.Test:
            self.vis.destroy()
            self.Test = False
        self.sokbilbox.delete(0, END)
        if self.betale:
            self.text.destroy()
            self.betale = False
        if self.oljetest_:
            self.oljeboks.delete(0, END)
            self.oljetest_ = False
        if self.lagrebool:
            self.lagreb.destroy()
            self.lagrebool = False
        if self.ok:
            self.lagret.destroy()
            self.ok = False

    def historie(self):
        webbrowser.open('file:///home/pi/Downloads/historie.html', new=2)

    def oljesjekk(self):
        self.oljetest_ = True
        webbrowser.open(
            'https://valvoline-eu.lubricantadvisor.com/nor/CountryLicenseplateSearch?licenseplate={}'.format(self.oljeboks.get()), new=2)

    def sokbil(self, win):
        if self.Test:
            self.vis.destroy()
        self.Test = True
        self.vis = Pmw.ScrolledText(win,
                                    borderframe=5,
                                    vscrollmode='dynamic',
                                    hscrollmode='dynamic',
                                    labelpos='n',
                                    text_width=50,
                                    text_height=5,
                                    text_wrap='none',
                                    text_font='Helvetica 16 bold')
        self.vis.tag_config('warning', background="yellow", foreground="red")
        with open('liste.txt') as my_file:
            for line in my_file:
                if self.sokbilbox.get().casefold() in line.casefold():
                    if "betalt:NEI" in line:
                        self.vis.insert('end', line, 'warning')
                    else:
                        self.vis.insert('end', line)
        self.vis.place(x=550, y=440)


window = Tk()
mywin = MyWindow(window)
window.title('Askim bilverksted')
window.geometry("1280x800")
window.mainloop()

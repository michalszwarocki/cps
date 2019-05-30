try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import Gui.FormSupport as fs
import Gui.FormManager as FormManager


class SignalFrame:


    def __init__(self, which, relx, rely, top=None):

        self.possibleRelY = [
        [0.0750, False],
        [0.1605, False],
        [0.2460, False],
        [0.3315, False],
        [0.4170, False],
        [0.5025, False],
        [0.5880, False],
        [0.6735, False],
        [0.7590, False],
        [0.8445, False],
        [0.9300, False]
    ]

        self.actualType = getattr(fs, which + 'TypeCombobox').get()
        self.actualNoise = getattr(fs, which + 'NoiseCombobox').get()
        # ---------------------------------------FRAME----------------------------------------------

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=relx, rely=rely, relheight=0.558, relwidth=0.45)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=625)

        # ----------------------------------------LABELS FRAME-------------------------------------

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.45, rely=0.0, height=21, width=50)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''SYGNAŁ''')


        self.Button2 = tk.Button(top)
        self.Button2.place(relx=relx+0.37, rely=rely+0.559, relheight=0.05, relwidth=0.07)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Rysuj''')
        self.Button2.configure(width=77)
        self.Button2.configure(command=lambda: FormManager.FormManager().onSignalDrawClicked(which))

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=relx+0.29, rely=rely+0.559, relheight=0.05, relwidth=0.07)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Zapisz''')
        self.Button3.configure(width=77)
        self.Button3.configure(command=lambda: FormManager.FormManager().onSignalSaveClicked(which))

        self.Button8 = tk.Button(top)
        self.Button8.place(relx=relx+0.21, rely=rely+0.559, relheight=0.05, relwidth=0.07)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''Odczytaj''')
        self.Button8.configure(width=77)
        self.Button8.configure(command=lambda: FormManager.FormManager().onSignalReadClicked(which))

        self.createSignalTypeLabel(which, self.getFirstPossibleRelY())
        self.createNoiseLabel(which, self.getFirstPossibleRelY())

        self.Label2 = tk.Label(self.Frame1)
        self.Label3 = tk.Label(self.Frame1)
        self.Label4 = tk.Label(self.Frame1)
        self.Label5 = tk.Label(self.Frame1)
        self.Label6 = tk.Label(self.Frame1)
        self.Label7 = tk.Label(self.Frame1)
        self.Label8 = tk.Label(self.Frame1)
        self.Label9 = tk.Label(self.Frame1)
        self.Label10 = tk.Label(self.Frame1)
        self.Label11 = tk.Label(self.Frame1)
        self.Label12 = tk.Label(self.Frame1)
        self.Label13 = tk.Label(self.Frame1)
        self.Label14 = tk.Label(self.Frame1)
        self.Label15 = tk.Label(self.Frame1)
        self.Label16 = tk.Label(self.Frame1)
        self.Label17 = tk.Label(self.Frame1)
        self.Label18 = tk.Label(self.Frame1)

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry4 = tk.Entry(self.Frame1)
        self.Entry5 = tk.Entry(self.Frame1)
        self.Entry6 = tk.Entry(self.Frame1)
        self.Entry7 = tk.Entry(self.Frame1)
        self.Entry8 = tk.Entry(self.Frame1)
        self.Entry9 = tk.Entry(self.Frame1)
        self.Entry10 = tk.Entry(self.Frame1)
        self.Entry11 = tk.Entry(self.Frame1)

        type = getattr(fs, which + 'TypeCombobox')
        type.trace("w", lambda name, index, mode, type=type: self.typeCallback(type, which))

        noise = getattr(fs, which + 'NoiseCombobox')
        noise.trace("w", lambda name, index, mode, noise=noise: self.noiseCallback(noise, which))

    def typeCallback(self, sv, which):
        self.setAllPossibleRelYAsFalse()
        self.disableAllEntries()
        self.disableAllLabels()

        if sv.get() != 'brak':
            getattr(fs, which + 'NoiseCombobox').set('brak')
            self.createTime0Label(which, self.getFirstPossibleRelY(), self.Label2, self.Entry1, self.Label3)
            self.createTimeLabel(which, self.getFirstPossibleRelY(), self.Label4, self.Entry2, self.Label5)
            self.createFrequencyLabel(which, self.getFirstPossibleRelY(), self.Label6, self.Entry3, self.Label7)
            self.createAmplitudeLabel(which, self.getFirstPossibleRelY(), self.Label8, self.Entry4)
            self.createSamplingFrequencyLabel(which, self.getFirstPossibleRelY(), self.Label9, self.Entry5, self.Label10)

        if sv.get() == 'prostokatny' or sv.get() == 'prostokatny symetryczny' or sv.get() == 'trojkatny':
            self.createInfiltratorLabel(which, self.getFirstPossibleRelY(), self.Label11, self.Entry6)

        if sv.get() == 'skok jednostkowy':
            self.createJumpMomentLabel(which, self.getFirstPossibleRelY(), self.Label12, self.Entry7)

        if sv.get() == 'impuls jednostkowy':
            self.createJumpSampleLabel(which, self.getFirstPossibleRelY(), self.Label13, self.Entry8)

        if sv.get() == 'o zmiennej czestotliwosci':
            self.createTime1Label(which, self.getFirstPossibleRelY(), self.Label15, self.Entry10, self.Label16)
            self.createFrequency1Label(which, self.getFirstPossibleRelY(), self.Label17, self.Entry11, self.Label18)

    def noiseCallback(self, sv, which):
        self.setAllPossibleRelYAsFalse()
        self.disableAllEntries()
        self.disableAllLabels()

        if sv.get() != 'brak':
            getattr(fs, which + 'TypeCombobox').set('brak')
            self.createTime0Label(which, self.getFirstPossibleRelY(), self.Label2, self.Entry1, self.Label3)
            self.createTimeLabel(which, self.getFirstPossibleRelY(), self.Label4, self.Entry2, self.Label5)
            self.createFrequencyLabel(which, self.getFirstPossibleRelY(), self.Label6, self.Entry3, self.Label7)
            self.createAmplitudeLabel(which, self.getFirstPossibleRelY(), self.Label8, self.Entry4)
            self.createSamplingFrequencyLabel(which, self.getFirstPossibleRelY(), self.Label9, self.Entry5, self.Label10)

        if sv.get() == 'impulsowy':
            self.createPossibilityLabel(which, self.getFirstPossibleRelY(), self.Label14, self.Entry9)

    def getFirstPossibleRelY(self):
        for x in range(len(self.possibleRelY)):
            if not self.possibleRelY[x][1]:
                self.possibleRelY[x][1] = True
                return self.possibleRelY[x][0]
        return 0

    def setAllPossibleRelYAsFalse(self):
        for x in range(len(self.possibleRelY)):
            if x != 0 and x != 1:
                self.possibleRelY[x][1] = False

    def disableAllEntries(self):
        self.Entry1.place_forget()
        self.Entry2.place_forget()
        self.Entry3.place_forget()
        self.Entry4.place_forget()
        self.Entry5.place_forget()
        self.Entry6.place_forget()
        self.Entry7.place_forget()
        self.Entry8.place_forget()
        self.Entry9.place_forget()
        self.Entry10.place_forget()
        self.Entry11.place_forget()

    def disableAllLabels(self):
        self.Label2.configure(text='')
        self.Label3.place_forget()
        self.Label4.place_forget()
        self.Label5.place_forget()
        self.Label6.place_forget()
        self.Label7.place_forget()
        self.Label8.place_forget()
        self.Label9.place_forget()
        self.Label10.place_forget()
        self.Label11.place_forget()
        self.Label12.place_forget()
        self.Label13.place_forget()
        self.Label14.place_forget()
        self.Label15.place_forget()
        self.Label16.place_forget()
        self.Label17.place_forget()
        self.Label18.place_forget()



    def createTime0Label(self, which, rely, Label, Entry, Label1):
        Label.place(relx=0.192, rely=rely, height=21, width=144)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''CZAS POCZĄTKOWY''')
        Label.configure(width=144)

        Entry.place(relx=0.528, rely=rely, height=20, relwidth=0.262)
        Entry.configure(background="#ffffff")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=getattr(fs, which + 'Time0Entry'))

        Label1.place(relx=0.816, rely=rely, height=21, width=11)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(foreground="#000000")
        Label1.configure(text='''s''')

    def createTimeLabel(self, which, rely, Label, Entry, Label1):
        Label.place(relx=0.224, rely=rely, height=21, width=114)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''CZAS TRWANIA''')
        Label.configure(width=114)

        Entry.place(relx=0.528, rely=rely, height=20, relwidth=0.262)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=getattr(fs, which + 'TimeEntry'))

        Label1.place(relx=0.816, rely=rely, height=21, width=11)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(foreground="#000000")
        Label1.configure(text='''s''')
        Label1.configure(width=11)

    def createFrequencyLabel(self, which, rely, Label, Entry, Label1):
        Label.place(relx=0.182, rely=rely, height=21, width=164)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''CZĘSTOTLIWOŚĆ SYGNAŁU''')

        Entry.place(relx=0.528, rely=rely, height=20, relwidth=0.262)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=getattr(fs, which + 'FrequencyEntry'))

        Label1.place(relx=0.816, rely=rely, height=21, width=20)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(foreground="#000000")
        Label1.configure(text='''Hz''')

    def createAmplitudeLabel(self, which, rely, Label, Entry):
        Label.place(relx=0.256, rely=rely, height=21, width=72)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''AMPLITUDA''')

        Entry.place(relx=0.528, rely=rely, height=20, relwidth=0.262)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=getattr(fs, which + 'AmplitudeEntry'))

    def createSamplingFrequencyLabel(self, which, rely, Label, Entry, Label1):
        Label.place(relx=0.16, rely=rely, height=21, width=198)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''CZĘSTOTLIWOŚĆ PRÓBKOWANIA''')

        Entry.place(relx=0.528, rely=rely, height=20, relwidth=0.262)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=getattr(fs, which + 'NOSamplesEntry'))

        Label1.place(relx=0.816, rely=rely, height=21, width=20)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(foreground="#000000")
        Label1.configure(text='''Hz''')

    def createSignalTypeLabel(self, which, rely):
        Label = tk.Label(self.Frame1)
        Label.place(relx=0.288, rely=rely, height=21, width=27)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''TYP''')

        TCombobox = ttk.Combobox(self.Frame1)
        TCombobox.place(relx=0.528, rely=rely, height=21, relwidth=0.261)
        TCombobox.configure(width=163)
        TCombobox.configure(takefocus="")
        TCombobox.configure(textvariable=getattr(fs, which + 'TypeCombobox'))
        TCombobox.configure(
            values=["brak", "sinus", "sinus wyprostowany jednopolowkowo", "sinus wyprostowany dwupolowkowo",
                    "prostokatny", "prostokatny symetryczny", "trojkatny", "skok jednostkowy", "impuls jednostkowy",
                    "o zmiennej czestotliwosci"])
        TCombobox.current(0)

    def createNoiseLabel(self, which, rely):
        Label = tk.Label(self.Frame1)
        Label.place(relx=0.288, rely=rely, height=21, width=35)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''SZUM''')

        TCombobox = ttk.Combobox(self.Frame1)
        TCombobox.place(relx=0.528, rely=rely, height=21, relwidth=0.261)
        TCombobox.configure(width=163)
        TCombobox.configure(takefocus="")
        TCombobox.configure(textvariable=getattr(fs, which + 'NoiseCombobox'))
        TCombobox.configure(
            values=["brak", "gaussowski", "o rozkladzie jednostajnym", "impulsowy"])
        TCombobox.current(0)

    def createInfiltratorLabel(self, which, rely, Label, Entry):
        Label.place(relx=0.16, rely=rely, height=21, width=187)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''WSPÓŁCZYNNIK WYPEŁNIENIA''')

        Entry.place(relx=0.528, rely=rely, height=20, relwidth=0.262)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=getattr(fs, which + 'InfiltratorEntry'))

    def createJumpMomentLabel(self, which, rely, Label, Entry):
        Label.place(relx=0.16, rely=rely, height=21, width=187)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''MOMENT SKOKU''')

        Entry.place(relx=0.528, rely=rely, height=20, relwidth=0.262)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=getattr(fs, which + 'JumpMomentEntry'))

    def createPossibilityLabel(self, which, rely, Label, Entry):
        Label.place(relx=0.16, rely=rely, height=21, width=187)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''PRAWDOPODOBIEŃSTWO''')

        Entry.place(relx=0.528, rely=rely, height=20, relwidth=0.262)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=getattr(fs, which + 'PossibilityEntry'))

    def createJumpSampleLabel(self, which, rely, Label, Entry):
        Label.place(relx=0.16, rely=rely, height=21, width=187)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''NUMER PRÓBKI SKOKU''')

        Entry.place(relx=0.528, rely=rely, height=20, relwidth=0.262)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=getattr(fs, which + 'JumpSampleEntry'))

    def createTime1Label(self, which, rely, Label, Entry, Label1):
        Label.place(relx=0.192, rely=rely, height=21, width=144)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''CZAS 1''')
        Label.configure(width=144)

        Entry.place(relx=0.528, rely=rely, height=20, relwidth=0.262)
        Entry.configure(background="#ffffff")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=getattr(fs, which + 'Time1Entry'))

        Label1.place(relx=0.816, rely=rely, height=21, width=11)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(foreground="#000000")
        Label1.configure(text='''s''')

    def createFrequency1Label(self, which, rely, Label, Entry, Label1):
        Label.place(relx=0.165, rely=rely, height=21, width=180)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''CZĘSTOTLIWOŚĆ W CZASIE 1''')

        Entry.place(relx=0.528, rely=rely, height=20, relwidth=0.262)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=getattr(fs, which + 'Freq1Entry'))

        Label1.place(relx=0.816, rely=rely, height=21, width=20)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(foreground="#000000")
        Label1.configure(text='''Hz''')
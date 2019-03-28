import sys

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

import Gui.FormSupport as Form_support
import Gui.FormManager as FormManager


def start_Gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, draw
    root = tk.Tk()
    Form_support.set_Tk_var()
    top = Toplevel1(root)
    Form_support.init(root, top)
    root.mainloop()


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    Form_support.set_Tk_var()
    top = Toplevel1(w)
    Form_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


def destroy_Window():
    root.destroy()


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("661x649+411+24")
        top.title("Generowanie sygnałów")
        top.configure(background="#d9d9d9")

        #---------------------------------------FRAME 1----------------------------------------------

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.03, rely=0.031, relheight=0.558, relwidth=0.45)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=625)

        #----------------------------------------LABELS FRAME 1-------------------------------------

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.23, rely=0.0, height=21, width=50)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''SYGNAŁ 1''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.192, rely=0.075, height=21, width=144)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''CZAS POCZĄTKOWY''')
        self.Label2.configure(width=144)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.224, rely=0.1605, height=21, width=114)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''CZAS TRWANIA''')
        self.Label3.configure(width=114)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.192, rely=0.246, height=21, width=154)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''CZĘSTOTLIWOŚĆ SYGNAŁU''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.256, rely=0.3315, height=21, width=72)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''AMPLITUDA''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.16, rely=0.417, height=21, width=187)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''CZĘSTOTLIWOŚĆ PRÓBKOWANIA''')

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.816, rely=0.246, height=21, width=20)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Hz''')

        self.Label9 = tk.Label(self.Frame1)
        self.Label9.place(relx=0.816, rely=0.417, height=21, width=20)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Hz''')

        self.Label10 = tk.Label(self.Frame1)
        self.Label10.place(relx=0.816, rely=0.1605, height=21, width=11)
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''s''')
        self.Label10.configure(width=11)

        self.Label11 = tk.Label(self.Frame1)
        self.Label11.place(relx=0.816, rely=0.075, height=21, width=11)
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''s''')

        self.Label12 = tk.Label(self.Frame1)
        self.Label12.place(relx=0.288, rely=0.8445, height=21, width=27)
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''TYP''')

        self.Label13 = tk.Label(self.Frame1)
        self.Label13.place(relx=0.16, rely=0.5025, height=21, width=187)
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''WSPÓŁCZYNNIK WYPEŁNIENIA''')

        self.Label14 = tk.Label(self.Frame1)
        self.Label14.place(relx=0.288, rely=0.930, height=21, width=30)
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''SZUM''')

        self.Label15 = tk.Label(self.Frame1)
        self.Label15.place(relx=0.16, rely=0.588, height=21, width=187)
        self.Label15.configure(background="#d9d9d9")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''MOMENT SKOKU''')

        self.Label32 = tk.Label(self.Frame1)
        self.Label32.place(relx=0.16, rely=0.6735, height=21, width=187)
        self.Label32.configure(background="#d9d9d9")
        self.Label32.configure(disabledforeground="#a3a3a3")
        self.Label32.configure(foreground="#000000")
        self.Label32.configure(text='''PRAWDOPODOBIEŃSTWO''')

        self.Label33 = tk.Label(self.Frame1)
        self.Label33.place(relx=0.16, rely=0.759, height=21, width=187)
        self.Label33.configure(background="#d9d9d9")
        self.Label33.configure(disabledforeground="#a3a3a3")
        self.Label33.configure(foreground="#000000")
        self.Label33.configure(text='''NUMER PRÓBKI SKOKU''')

        #----------------------------ENTRIES FRAME 1-------------------------------

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.528, rely=0.075, height=20, relwidth=0.262)
        self.Entry1.configure(background="#ffffff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=Form_support.firstTime0Entry)

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.528, rely=0.1605, height=20, relwidth=0.262)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable=Form_support.firstTimeEntry)

        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry3.place(relx=0.528, rely=0.246, height=20, relwidth=0.262)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable=Form_support.firstFrequencyEntry)

        self.Entry4 = tk.Entry(self.Frame1)
        self.Entry4.place(relx=0.528, rely=0.3315, height=20, relwidth=0.262)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(textvariable=Form_support.firstAmplitudeEntry)

        self.Entry5 = tk.Entry(self.Frame1)
        self.Entry5.place(relx=0.528, rely=0.417, height=20, relwidth=0.262)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(textvariable=Form_support.firstNOSamplesEntry)

        self.Entry6 = tk.Entry(self.Frame1)
        self.Entry6.place(relx=0.528, rely=0.5025, height=20, relwidth=0.262)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(textvariable=Form_support.firstInfiltratorEntry)

        self.Entry7 = tk.Entry(self.Frame1)
        self.Entry7.place(relx=0.528, rely=0.588, height=20, relwidth=0.262)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(textvariable=Form_support.firstJumpMomentEntry)

        self.Entry15 = tk.Entry(self.Frame1)
        self.Entry15.place(relx=0.528, rely=0.6735, height=20, relwidth=0.262)
        self.Entry15.configure(background="white")
        self.Entry15.configure(disabledforeground="#a3a3a3")
        self.Entry15.configure(font="TkFixedFont")
        self.Entry15.configure(foreground="#000000")
        self.Entry15.configure(insertbackground="black")
        self.Entry15.configure(textvariable=Form_support.firstPossibilityEntry)

        self.Entry16 = tk.Entry(self.Frame1)
        self.Entry16.place(relx=0.528, rely=0.759, height=20, relwidth=0.262)
        self.Entry16.configure(background="white")
        self.Entry16.configure(disabledforeground="#a3a3a3")
        self.Entry16.configure(font="TkFixedFont")
        self.Entry16.configure(foreground="#000000")
        self.Entry16.configure(insertbackground="black")
        self.Entry16.configure(textvariable=Form_support.firstJumpSampleEntry)

        #-----------------------------------------COMBOBOXES FRAME 1------------------------------------------

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.528, rely=0.8445, height=21
                              , relwidth=0.261)
        self.TCombobox1.configure(width=163)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(textvariable=Form_support.firstTypeCombobox)
        self.TCombobox1.configure(
            values=["brak", "sinus", "sinus wyprostowany jednopołówkowo", "sinus wyprostowany dwupołówkowo",
                    "prostokątny", "prostokatny symetryczny", "trójkątny", "skok jednostkowy", "impuls jednostkowy"])
        self.TCombobox1.current(0)

        self.TCombobox2 = ttk.Combobox(self.Frame1)
        self.TCombobox2.place(relx=0.528, rely=0.930, height=21
                              , relwidth=0.261)
        self.TCombobox2.configure(width=163)
        self.TCombobox2.configure(takefocus="")
        self.TCombobox2.configure(textvariable=Form_support.firstNoiseCombobox)
        self.TCombobox2.configure(
            values=["brak", "gaussowski", "o rozkładzie jednostajnym", "impulsowy"])
        self.TCombobox2.current(0)

        # -----------------------------------------BUTTONS FRAME 1------------------------------------------

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.40, rely=0.590, relheight=0.05, relwidth=0.07)
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
        self.Button2.configure(command=lambda: FormManager.FormManager().onFirstSignalDrawClicked())

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.32, rely=0.590, relheight=0.05, relwidth=0.07)
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
        self.Button3.configure(command=lambda: FormManager.FormManager().onFirstSignalSaveClicked())

        self.Button8 = tk.Button(top)
        self.Button8.place(relx=0.24, rely=0.590, relheight=0.05, relwidth=0.07)
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
        self.Button8.configure(command=lambda: FormManager.FormManager().onFirstSignalReadClicked())

        #----------------------------------------------FRAME 2---------------------------------------------

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.52, rely=0.031, relheight=0.558, relwidth=0.45)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=625)

        #------------------------------------------LABELS FRAME 2-------------------------------------------

        self.Label16 = tk.Label(top)
        self.Label16.place(relx=0.73, rely=0.0, height=21, width=60)
        self.Label16.configure(background="#d9d9d9")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(text='''SYGNAŁ 2''')

        self.Label17 = tk.Label(self.Frame2)
        self.Label17.place(relx=0.192, rely=0.075, height=21, width=144)
        self.Label17.configure(background="#d9d9d9")
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(text='''CZAS POCZĄTKOWY''')
        self.Label17.configure(width=144)

        self.Label18 = tk.Label(self.Frame2)
        self.Label18.place(relx=0.224, rely=0.1605, height=21, width=114)
        self.Label18.configure(background="#d9d9d9")
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(text='''CZAS TRWANIA''')
        self.Label18.configure(width=114)

        self.Label19 = tk.Label(self.Frame2)
        self.Label19.place(relx=0.192, rely=0.246, height=21, width=154)
        self.Label19.configure(background="#d9d9d9")
        self.Label19.configure(disabledforeground="#a3a3a3")
        self.Label19.configure(foreground="#000000")
        self.Label19.configure(text='''CZĘSTOTLIWOŚĆ SYGNAŁU''')

        self.Label20 = tk.Label(self.Frame2)
        self.Label20.place(relx=0.256, rely=0.3315, height=21, width=72)
        self.Label20.configure(background="#d9d9d9")
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(foreground="#000000")
        self.Label20.configure(text='''AMPLITUDA''')

        self.Label21 = tk.Label(self.Frame2)
        self.Label21.place(relx=0.16, rely=0.417, height=21, width=187)
        self.Label21.configure(background="#d9d9d9")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(text='''CZĘSTOTLIWOŚĆ PRÓBKOWANIA''')

        self.Label22 = tk.Label(self.Frame2)
        self.Label22.place(relx=0.816, rely=0.246, height=21, width=20)
        self.Label22.configure(background="#d9d9d9")
        self.Label22.configure(disabledforeground="#a3a3a3")
        self.Label22.configure(foreground="#000000")
        self.Label22.configure(text='''Hz''')

        self.Label23 = tk.Label(self.Frame2)
        self.Label23.place(relx=0.816, rely=0.417, height=21, width=20)
        self.Label23.configure(background="#d9d9d9")
        self.Label23.configure(disabledforeground="#a3a3a3")
        self.Label23.configure(foreground="#000000")
        self.Label23.configure(text='''Hz''')

        self.Label24 = tk.Label(self.Frame2)
        self.Label24.place(relx=0.816, rely=0.1605, height=21, width=11)
        self.Label24.configure(background="#d9d9d9")
        self.Label24.configure(disabledforeground="#a3a3a3")
        self.Label24.configure(foreground="#000000")
        self.Label24.configure(text='''s''')
        self.Label24.configure(width=11)

        self.Label25 = tk.Label(self.Frame2)
        self.Label25.place(relx=0.816, rely=0.075, height=21, width=11)
        self.Label25.configure(background="#d9d9d9")
        self.Label25.configure(disabledforeground="#a3a3a3")
        self.Label25.configure(foreground="#000000")
        self.Label25.configure(text='''s''')

        self.Label26 = tk.Label(self.Frame2)
        self.Label26.place(relx=0.288, rely=0.8445, height=21, width=27)
        self.Label26.configure(background="#d9d9d9")
        self.Label26.configure(disabledforeground="#a3a3a3")
        self.Label26.configure(foreground="#000000")
        self.Label26.configure(text='''TYP''')

        self.Label27 = tk.Label(self.Frame2)
        self.Label27.place(relx=0.16, rely=0.5025, height=21, width=187)
        self.Label27.configure(background="#d9d9d9")
        self.Label27.configure(disabledforeground="#a3a3a3")
        self.Label27.configure(foreground="#000000")
        self.Label27.configure(text='''WSPÓŁCZYNNIK WYPEŁNIENIA''')

        self.Label28 = tk.Label(self.Frame2)
        self.Label28.place(relx=0.288, rely=0.930, height=21, width=30)
        self.Label28.configure(background="#d9d9d9")
        self.Label28.configure(disabledforeground="#a3a3a3")
        self.Label28.configure(foreground="#000000")
        self.Label28.configure(text='''SZUM''')

        self.Label29 = tk.Label(self.Frame2)
        self.Label29.place(relx=0.16, rely=0.588, height=21, width=187)
        self.Label29.configure(background="#d9d9d9")
        self.Label29.configure(disabledforeground="#a3a3a3")
        self.Label29.configure(foreground="#000000")
        self.Label29.configure(text='''MOMENT SKOKU''')

        self.Label34 = tk.Label(self.Frame2)
        self.Label34.place(relx=0.16, rely=0.6735, height=21, width=187)
        self.Label34.configure(background="#d9d9d9")
        self.Label34.configure(disabledforeground="#a3a3a3")
        self.Label34.configure(foreground="#000000")
        self.Label34.configure(text='''PRAWDOPODOBIEŃSTWO''')

        self.Label35 = tk.Label(self.Frame2)
        self.Label35.place(relx=0.16, rely=0.759, height=21, width=187)
        self.Label35.configure(background="#d9d9d9")
        self.Label35.configure(disabledforeground="#a3a3a3")
        self.Label35.configure(foreground="#000000")
        self.Label35.configure(text='''NUMER PRÓBKI SKOKU''')

        #-----------------------------------------ENTRIES FRAME 2--------------------------------------

        self.Entry8 = tk.Entry(self.Frame2)
        self.Entry8.place(relx=0.528, rely=0.075, height=20, relwidth=0.262)
        self.Entry8.configure(background="#ffffff")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(textvariable=Form_support.secondTime0Entry)

        self.Entry9 = tk.Entry(self.Frame2)
        self.Entry9.place(relx=0.528, rely=0.1605, height=20, relwidth=0.262)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(insertbackground="black")
        self.Entry9.configure(textvariable=Form_support.secondTimeEntry)

        self.Entry10 = tk.Entry(self.Frame2)
        self.Entry10.place(relx=0.528, rely=0.246, height=20, relwidth=0.262)
        self.Entry10.configure(background="white")
        self.Entry10.configure(disabledforeground="#a3a3a3")
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.configure(foreground="#000000")
        self.Entry10.configure(insertbackground="black")
        self.Entry10.configure(textvariable=Form_support.secondFrequencyEntry)

        self.Entry11 = tk.Entry(self.Frame2)
        self.Entry11.place(relx=0.528, rely=0.3315, height=20, relwidth=0.262)
        self.Entry11.configure(background="white")
        self.Entry11.configure(disabledforeground="#a3a3a3")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(foreground="#000000")
        self.Entry11.configure(insertbackground="black")
        self.Entry11.configure(textvariable=Form_support.secondAmplitudeEntry)

        self.Entry12 = tk.Entry(self.Frame2)
        self.Entry12.place(relx=0.528, rely=0.417, height=20, relwidth=0.262)
        self.Entry12.configure(background="white")
        self.Entry12.configure(disabledforeground="#a3a3a3")
        self.Entry12.configure(font="TkFixedFont")
        self.Entry12.configure(foreground="#000000")
        self.Entry12.configure(insertbackground="black")
        self.Entry12.configure(textvariable=Form_support.secondNOSamplesEntry)

        self.Entry13 = tk.Entry(self.Frame2)
        self.Entry13.place(relx=0.528, rely=0.5025, height=20, relwidth=0.262)
        self.Entry13.configure(background="white")
        self.Entry13.configure(disabledforeground="#a3a3a3")
        self.Entry13.configure(font="TkFixedFont")
        self.Entry13.configure(foreground="#000000")
        self.Entry13.configure(insertbackground="black")
        self.Entry13.configure(textvariable=Form_support.secondInfiltratorEntry)

        self.Entry14 = tk.Entry(self.Frame2)
        self.Entry14.place(relx=0.528, rely=0.588, height=20, relwidth=0.262)
        self.Entry14.configure(background="white")
        self.Entry14.configure(disabledforeground="#a3a3a3")
        self.Entry14.configure(font="TkFixedFont")
        self.Entry14.configure(foreground="#000000")
        self.Entry14.configure(insertbackground="black")
        self.Entry14.configure(textvariable=Form_support.secondJumpMomentEntry)

        self.Entry17 = tk.Entry(self.Frame2)
        self.Entry17.place(relx=0.528, rely=0.6735, height=20, relwidth=0.262)
        self.Entry17.configure(background="white")
        self.Entry17.configure(disabledforeground="#a3a3a3")
        self.Entry17.configure(font="TkFixedFont")
        self.Entry17.configure(foreground="#000000")
        self.Entry17.configure(insertbackground="black")
        self.Entry17.configure(textvariable=Form_support.secondPossibilityEntry)

        self.Entry18 = tk.Entry(self.Frame2)
        self.Entry18.place(relx=0.528, rely=0.759, height=20, relwidth=0.262)
        self.Entry18.configure(background="white")
        self.Entry18.configure(disabledforeground="#a3a3a3")
        self.Entry18.configure(font="TkFixedFont")
        self.Entry18.configure(foreground="#000000")
        self.Entry18.configure(insertbackground="black")
        self.Entry18.configure(textvariable=Form_support.secondJumpSampleEntry)

        # -----------------------------------------COMBOBOXES FRAME 2------------------------------------------

        self.TCombobox3 = ttk.Combobox(self.Frame2)
        self.TCombobox3.place(relx=0.528, rely=0.8445, height=21
                              , relwidth=0.261)
        self.TCombobox3.configure(width=163)
        self.TCombobox3.configure(takefocus="")
        self.TCombobox3.configure(textvariable=Form_support.secondTypeCombobox)
        self.TCombobox3.configure(
            values=["brak", "sinus", "sinus wyprostowany jednopołówkowo", "sinus wyprostowany dwupołówkowo",
                    "prostokątny", "prostokatny symetryczny", "trójkątny", "skok jednostkowy", "impuls jednostkowy"])
        self.TCombobox3.current(0)

        self.TCombobox4 = ttk.Combobox(self.Frame2)
        self.TCombobox4.place(relx=0.528, rely=0.930, height=21
                              , relwidth=0.261)
        self.TCombobox4.configure(width=163)
        self.TCombobox4.configure(takefocus="")
        self.TCombobox4.configure(textvariable=Form_support.secondNoiseCombobox)
        self.TCombobox4.configure(
            values=["brak", "gaussowski", "o rozkładzie jednostajnym", "impulsowy"])
        self.TCombobox4.current(0)

        # -----------------------------------------BUTTONS FRAME 2------------------------------------------

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.89, rely=0.590, relheight=0.05, relwidth=0.07)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Rysuj''')
        self.Button4.configure(width=77)
        self.Button4.configure(command=lambda: FormManager.FormManager().onSecondSignalDrawClicked())

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.81, rely=0.590, relheight=0.05, relwidth=0.07)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Zapisz''')
        self.Button5.configure(width=77)
        self.Button5.configure(command=lambda: FormManager.FormManager().onSecondSignalSaveClicked())

        self.Button9 = tk.Button(top)
        self.Button9.place(relx=0.73, rely=0.590, relheight=0.05, relwidth=0.07)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''Odczytaj''')
        self.Button9.configure(width=77)
        self.Button9.configure(command=lambda: FormManager.FormManager().onSecondSignalReadClicked())

        #----------------------------------------------FRAME 3---------------------------------------------

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.55, rely=0.68, relheight=0.24, relwidth=0.4)

        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(width=625)

        #------------------------------------------LABELS FRAME 3-------------------------------------------

        self.Label30 = tk.Label(top)
        self.Label30.place(relx=0.73, rely=0.65, height=21, width=60)
        self.Label30.configure(background="#d9d9d9")
        self.Label30.configure(disabledforeground="#a3a3a3")
        self.Label30.configure(foreground="#000000")
        self.Label30.configure(text='''OPERACJE''')

        self.Label31 = tk.Label(self.Frame3)
        self.Label31.place(relx=0.1, rely=0.35, height=21, width=144)
        self.Label31.configure(background="#d9d9d9")
        self.Label31.configure(disabledforeground="#a3a3a3")
        self.Label31.configure(foreground="#000000")
        self.Label31.configure(text='''WYBIERZ OPERACJE''')
        self.Label31.configure(width=144)

        # -----------------------------------------COMBOBOXES FRAME 3------------------------------------------

        self.TCombobox5 = ttk.Combobox(self.Frame3)
        self.TCombobox5.place(relx=0.5, rely=0.33, relheight=0.2
                              , relwidth=0.261)
        self.TCombobox5.configure(width=163)
        self.TCombobox5.configure(takefocus="")
        self.TCombobox5.configure(textvariable=Form_support.operationCombobox)
        self.TCombobox5.configure(
            values=["dodawanie", "odejmowanie", "mnożenie", "dzielenie"])
        self.TCombobox5.current(0)

        # -----------------------------------------BUTTONS FRAME 3------------------------------------------

        self.Button6 = tk.Button(self.Frame3)
        self.Button6.place(relx=0.38, rely=0.78, relheight=0.2, relwidth=0.14)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Rysuj''')
        self.Button6.configure(width=77)
        self.Button6.configure(command=lambda: FormManager.FormManager().onOperationDrawClicked())

        self.Button7 = tk.Button(self.Frame3)
        self.Button7.place(relx=0.54, rely=0.78, relheight=0.2, relwidth=0.14)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Zapisz''')
        self.Button7.configure(width=77)
        self.Button7.configure(command=lambda: FormManager.FormManager().onOperationSaveClicked())

        #----------------------------------------------FRAME 4---------------------------------------------

        self.Frame4 = tk.Frame(top)
        self.Frame4.place(relx=0.05, rely=0.68, relheight=0.24, relwidth=0.4)

        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(background="#d9d9d9")
        self.Frame4.configure(width=625)

        #------------------------------------------LABELS FRAME 3-------------------------------------------

        self.Label36 = tk.Label(self.Frame4)
        self.Label36.place(relx=0.1, rely=0.05, height=21, width=144)
        self.Label36.configure(background="#d9d9d9")
        self.Label36.configure(disabledforeground="#a3a3a3")
        self.Label36.configure(foreground="#000000")
        self.Label36.configure(text='''WARTOŚĆ ŚREDNIA''')

        self.Label37 = tk.Label(self.Frame4)
        self.Label37.place(relx=0.04, rely=0.25, height=21, width=200)
        self.Label37.configure(background="#d9d9d9")
        self.Label37.configure(disabledforeground="#a3a3a3")
        self.Label37.configure(foreground="#000000")
        self.Label37.configure(text='''WARTOŚĆ ŚREDNIA BEZWZGLĘDNA''')
        self.Label37.configure(width=144)

        self.Label38 = tk.Label(self.Frame4)
        self.Label38.place(relx=0.1, rely=0.45, height=21, width=144)
        self.Label38.configure(background="#d9d9d9")
        self.Label38.configure(disabledforeground="#a3a3a3")
        self.Label38.configure(foreground="#000000")
        self.Label38.configure(text='''MOC ŚREDNIA''')
        self.Label38.configure(width=144)

        self.Label39 = tk.Label(self.Frame4)
        self.Label39.place(relx=0.1, rely=0.65, height=21, width=144)
        self.Label39.configure(background="#d9d9d9")
        self.Label39.configure(disabledforeground="#a3a3a3")
        self.Label39.configure(foreground="#000000")
        self.Label39.configure(text='''WARIANCJA''')
        self.Label39.configure(width=144)

        self.Label40 = tk.Label(self.Frame4)
        self.Label40.place(relx=0.1, rely=0.85, height=21, width=144)
        self.Label40.configure(background="#d9d9d9")
        self.Label40.configure(disabledforeground="#a3a3a3")
        self.Label40.configure(foreground="#000000")
        self.Label40.configure(text='''WARTOŚĆ SKUTECZNA''')
        self.Label40.configure(width=144)

        self.Label41 = tk.Label(self.Frame4)
        self.Label41.place(relx=0.6, rely=0.05, height=21, width=120)
        self.Label41.configure(background="#d9d9d9")
        self.Label41.configure(disabledforeground="#a3a3a3")
        self.Label41.configure(foreground="#000000")
        self.Label41.configure(textvariable=Form_support.text1Label)

        self.Label42 = tk.Label(self.Frame4)
        self.Label42.place(relx=0.6, rely=0.25, height=21, width=120)
        self.Label42.configure(background="#d9d9d9")
        self.Label42.configure(disabledforeground="#a3a3a3")
        self.Label42.configure(foreground="#000000")
        self.Label42.configure(textvariable=Form_support.text2Label)
        self.Label42.configure(width=144)

        self.Label43 = tk.Label(self.Frame4)
        self.Label43.place(relx=0.6, rely=0.45, height=21, width=120)
        self.Label43.configure(background="#d9d9d9")
        self.Label43.configure(disabledforeground="#a3a3a3")
        self.Label43.configure(foreground="#000000")
        self.Label43.configure(textvariable=Form_support.text3Label)
        self.Label43.configure(width=144)

        self.Label44 = tk.Label(self.Frame4)
        self.Label44.place(relx=0.6, rely=0.65, height=21, width=120)
        self.Label44.configure(background="#d9d9d9")
        self.Label44.configure(disabledforeground="#a3a3a3")
        self.Label44.configure(foreground="#000000")
        self.Label44.configure(textvariable=Form_support.text4Label)
        self.Label44.configure(width=144)

        self.Label45 = tk.Label(self.Frame4)
        self.Label45.place(relx=0.6, rely=0.85, height=21, width=120)
        self.Label45.configure(background="#d9d9d9")
        self.Label45.configure(disabledforeground="#a3a3a3")
        self.Label45.configure(foreground="#000000")
        self.Label45.configure(textvariable=Form_support.text5Label)
        self.Label45.configure(width=144)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.9, rely=0.94, relheight=0.05, relwidth=0.07)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Wyjdź''')
        self.Button1.configure(width=77)
        self.Button1.configure(command=lambda: destroy_Window())
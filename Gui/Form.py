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
import Gui.Frames.OperationFrame as operFrame
import Gui.Frames.SignalFrame as sigFrame
import Gui.Frames.SignalMetricFrame as sigMetFrame
import Gui.Frames.MetricsFrame as metFrame
import Gui.Frames.SamplingFrame as sampFrame


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

        self.TabControl1 = ttk.Notebook(top)

        self.Frame1 = ttk.Frame(self.TabControl1)
        self.Frame2 = sigFrame.SignalFrame('first', 0.03, 0.031, self.Frame1)
        self.Frame3 = sigFrame.SignalFrame('second', 0.52, 0.031, self.Frame1)
        self.Frame4 = operFrame.OperationFrame(0.55, 0.68, self.Frame1)
        self.Frame5 = sigMetFrame.SignalMetricFrame(0.05, 0.68, self.Frame1)

        self.Frame6 = ttk.Frame(self.TabControl1)
        self.Frame7 = sigFrame.SignalFrame('first', 0.03, 0.031, self.Frame6)
        self.Frame8 = sigMetFrame.SignalMetricFrame(0.05, 0.68, self.Frame6)
        self.Frame9 = metFrame.MetricsFrame(0.55, 0.68, self.Frame6)
        self.Frame10 = sampFrame.SamplingFrame(0.52, 0.031, self.Frame6)

        self.Frame11 = ttk.Frame(self.TabControl1)

        self.TabControl1.add(self.Frame1, text="SYGNAŁY I OPERACJE")
        self.TabControl1.add(self.Frame6, text="PRÓBKOWANIE I KWANTYZACJA")
        self.TabControl1.add(self.Frame11, text="ZADANIE 3")
        self.TabControl1.pack(expan=1, fill="both")


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

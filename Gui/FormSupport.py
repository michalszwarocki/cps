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


def set_Tk_var():
    global firstTime0Entry, firstTimeEntry, firstFrequencyEntry, firstAmplitudeEntry, firstNOSamplesEntry, \
        firstInfiltratorEntry, firstJumpMomentEntry, firstPossibilityEntry, firstJumpSampleEntry
    global secondTime0Entry, secondTimeEntry, secondFrequencyEntry, secondAmplitudeEntry, secondNOSamplesEntry, \
        secondInfiltratorEntry, secondJumpMomentEntry, secondPossibilityEntry, secondJumpSampleEntry
    global firstTypeCombobox, firstNoiseCombobox, secondTypeCombobox, secondNoiseCombobox, operationCombobox
    global text1Label, text2Label, text3Label, text4Label, text5Label

    firstTime0Entry = tk.StringVar()
    firstTimeEntry = tk.StringVar()
    firstFrequencyEntry = tk.StringVar()
    firstAmplitudeEntry = tk.StringVar()
    firstNOSamplesEntry = tk.StringVar()
    firstInfiltratorEntry = tk.StringVar()
    firstJumpMomentEntry = tk.StringVar()
    firstPossibilityEntry = tk.StringVar()
    firstJumpSampleEntry = tk.StringVar()

    secondTime0Entry = tk.StringVar()
    secondTimeEntry = tk.StringVar()
    secondFrequencyEntry = tk.StringVar()
    secondAmplitudeEntry = tk.StringVar()
    secondNOSamplesEntry = tk.StringVar()
    secondInfiltratorEntry = tk.StringVar()
    secondJumpMomentEntry = tk.StringVar()
    secondPossibilityEntry = tk.StringVar()
    secondJumpSampleEntry = tk.StringVar()

    firstTypeCombobox = tk.StringVar()
    firstNoiseCombobox = tk.StringVar()
    secondTypeCombobox = tk.StringVar()
    secondNoiseCombobox = tk.StringVar()
    operationCombobox = tk.StringVar()

    text1Label = tk.StringVar()
    text2Label = tk.StringVar()
    text3Label = tk.StringVar()
    text4Label = tk.StringVar()
    text5Label = tk.StringVar()

    firstTime0Entry.set('0')
    firstTimeEntry.set('3')
    firstFrequencyEntry.set('2')
    firstAmplitudeEntry.set('1')
    firstNOSamplesEntry.set('200')
    firstInfiltratorEntry.set('0.5')
    firstJumpMomentEntry.set('1')
    firstPossibilityEntry.set('0.5')
    firstJumpSampleEntry.set('0')

    secondTime0Entry.set('0')
    secondTimeEntry.set('3')
    secondFrequencyEntry.set('2')
    secondAmplitudeEntry.set('1')
    secondNOSamplesEntry.set('200')
    secondInfiltratorEntry.set('0.5')
    secondJumpMomentEntry.set('1')
    secondPossibilityEntry.set('0.5')
    secondJumpSampleEntry.set('0')

    text1Label.set('')
    text2Label.set('')
    text3Label.set('')
    text4Label.set('')
    text5Label.set('')


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import Form

    Form.vp_start_gui()

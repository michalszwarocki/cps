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

import numpy as np

def set_Tk_var():
    global firstTime0Entry, firstTimeEntry, firstFrequencyEntry, firstAmplitudeEntry, firstNOSamplesEntry, \
        firstInfiltratorEntry, firstJumpMomentEntry, firstPossibilityEntry, firstJumpSampleEntry, firstTime1Entry, \
        firstFreq1Entry
    global secondTime0Entry, secondTimeEntry, secondFrequencyEntry, secondAmplitudeEntry, secondNOSamplesEntry, \
        secondInfiltratorEntry, secondJumpMomentEntry, secondPossibilityEntry, secondJumpSampleEntry, secondTime1Entry, \
        secondFreq1Entry
    global firstTypeCombobox, firstNoiseCombobox, secondTypeCombobox, secondNoiseCombobox, operationCombobox, \
        filterOperationCombobox, filterTypeCombobox, windowCombobox
    global text1Label, text2Label, text3Label, text4Label, text5Label
    global firstPoints, secondPoints, imagPoints

    global mseLabel, snrLabel, psnrLabel, mdLabel, enobLabel
    global samplingPeriodEntry, quantizationBitsEntry, nOSamplesEntry, actionCombobox

    global mValueEntry, foEntry, distanceValueEntry, speedEntry, realDistance, achievedDistance

    global transformationCombobox, plotCombobox, durationTimeTrans, samplingFrequencyTrans

    firstTime0Entry = tk.StringVar()
    firstTimeEntry = tk.StringVar()
    firstFrequencyEntry = tk.StringVar()
    firstAmplitudeEntry = tk.StringVar()
    firstNOSamplesEntry = tk.StringVar()
    firstInfiltratorEntry = tk.StringVar()
    firstJumpMomentEntry = tk.StringVar()
    firstPossibilityEntry = tk.StringVar()
    firstJumpSampleEntry = tk.StringVar()
    firstTime1Entry = tk.StringVar()
    firstFreq1Entry = tk.StringVar()

    secondTime0Entry = tk.StringVar()
    secondTimeEntry = tk.StringVar()
    secondFrequencyEntry = tk.StringVar()
    secondAmplitudeEntry = tk.StringVar()
    secondNOSamplesEntry = tk.StringVar()
    secondInfiltratorEntry = tk.StringVar()
    secondJumpMomentEntry = tk.StringVar()
    secondPossibilityEntry = tk.StringVar()
    secondJumpSampleEntry = tk.StringVar()
    secondTime1Entry = tk.StringVar()
    secondFreq1Entry = tk.StringVar()

    firstTypeCombobox = tk.StringVar()
    firstNoiseCombobox = tk.StringVar()
    secondTypeCombobox = tk.StringVar()
    secondNoiseCombobox = tk.StringVar()
    operationCombobox = tk.StringVar()
    filterOperationCombobox = tk.StringVar()
    filterTypeCombobox = tk.StringVar()
    windowCombobox = tk.StringVar()

    firstPoints = np.array
    secondPoints = np.array
    imagPoints = np.array

    text1Label = tk.StringVar()
    text2Label = tk.StringVar()
    text3Label = tk.StringVar()
    text4Label = tk.StringVar()
    text5Label = tk.StringVar()

    mseLabel = tk.StringVar()
    snrLabel = tk.StringVar()
    psnrLabel = tk.StringVar()
    mdLabel = tk.StringVar()
    enobLabel = tk.StringVar()

    samplingPeriodEntry = tk.StringVar()
    quantizationBitsEntry = tk.StringVar()
    nOSamplesEntry = tk.StringVar()
    actionCombobox = tk.StringVar()

    mValueEntry = tk.StringVar()
    foEntry = tk.StringVar()
    distanceValueEntry = tk.StringVar()
    speedEntry = tk.StringVar()
    realDistance = tk.StringVar()
    achievedDistance = tk.StringVar()

    transformationCombobox = tk.StringVar()
    plotCombobox = tk.StringVar()
    durationTimeTrans = tk.StringVar()
    samplingFrequencyTrans = tk.StringVar()

    firstTime0Entry.set('0')
    firstTimeEntry.set('1')
    firstFrequencyEntry.set('2')
    firstAmplitudeEntry.set('3')
    firstNOSamplesEntry.set('200')
    firstInfiltratorEntry.set('0.5')
    firstJumpMomentEntry.set('0.5')
    firstPossibilityEntry.set('0.5')
    firstJumpSampleEntry.set('50')
    firstTime1Entry.set('0.5')
    firstFreq1Entry.set('5')

    secondTime0Entry.set('0')
    secondTimeEntry.set('1')
    secondFrequencyEntry.set('1')
    secondAmplitudeEntry.set('1')
    secondNOSamplesEntry.set('200')
    secondInfiltratorEntry.set('0.5')
    secondJumpMomentEntry.set('1')
    secondPossibilityEntry.set('0.5')
    secondJumpSampleEntry.set('0')
    secondTime1Entry.set('0.5')
    secondFreq1Entry.set('5')

    text1Label.set('')
    text2Label.set('')
    text3Label.set('')
    text4Label.set('')
    text5Label.set('')

    mseLabel.set('')
    snrLabel.set('')
    psnrLabel.set('')
    mdLabel.set('')
    enobLabel.set('')

    samplingPeriodEntry.set('0.1')
    quantizationBitsEntry.set('4')
    nOSamplesEntry.set('10')

    mValueEntry.set('65')
    foEntry.set('5')
    distanceValueEntry.set('1000')
    speedEntry.set('20')
    realDistance.set('0')
    achievedDistance.set('0')

    durationTimeTrans.set('0')
    samplingFrequencyTrans.set('16')


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

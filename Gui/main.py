from Gui import Form

Form.start_Gui()

# # RYSOWANIE SYGNAŁU
# plt.subplot(4, 1, 1)
# x = signal.getTime()
# y = signal.getSignal(x)
# plt.plot(x, y, '-', markersize=0.9)
#
# # RYSOWANIE PRÓBKOWANIA
# plt.subplot(4, 1, 2)
# x1 = signal.samplingTime(0.05)
# y1 = signal.sampling(0.05)
# plt.plot(x1, y1, 'o', markersize=0.9)
#
# #RYSOWANIE KWANTYZACJI Z OBCIĘCIEM
# plt.subplot(4, 1, 3)
# x2 = x1
# y2 = Operations.Operations().quantizate(signal, 5, y1)
# plt.plot(x,y)
# plt.step(x1, y2, where='post')
#
# #RYSOWANIE KWANTYZACJI Z ZAOKRĄGLENIEM
# plt.subplot(4, 1, 4)
# x3 = x1
# y3 = Operations.Operations().quantizate(signal, 2, y1)
# plt.plot(x,y)
# plt.plot(x3,y3,'o')
# plt.step(x3, y3, where='mid')
# print(y3)
#
# plt.show()
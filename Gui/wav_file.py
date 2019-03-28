import scipy.io.wavfile


def save(signal, sample_rate, t0):
    scipy.io.wavfile.write(t0, sample_rate, signal)


def read(filename):
    x, y = scipy.io.wavfile.read(filename)
    return x, y

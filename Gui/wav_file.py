import scipy.io.wavfile


def save(signal, sample_rate, fileName):
    scipy.io.wavfile.write(fileName, sample_rate, signal)


def read(filename):
    x, y = scipy.io.wavfile.read(filename)
    return x, y

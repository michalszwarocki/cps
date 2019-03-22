import numpy as np


class Operations:

    def quantizate(self, signal, bits, samples):
        Q = signal.alt * 2.0 / pow(2, bits)
        return Q * (np.floor(samples / Q) + 0.5)

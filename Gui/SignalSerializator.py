import struct
import Logic.SignalConfiguration as config


def save(fileName, configuration, signal, imagPoints):

    newFile = open(fileName, "wb")
    t0Bytes = struct.pack('f', configuration.time0)
    timeBytes = struct.pack('f', configuration.time)
    frequencyBytes = struct.pack('f', configuration.frequency)
    amplitudeBytes = struct.pack('f', configuration.amplitude)
    numberOfSamplesBytes = struct.pack('i', configuration.numberOfSamples)
    infiltratorBytes = struct.pack('f', configuration.infiltrator)
    jumpMomentBytes = struct.pack('f', configuration.jumpMoment)
    possibilityBytes = struct.pack('f', configuration.possibility)
    jumpSampleBytes = struct.pack('i', configuration.jumpSample)
    signalTypeLengthBytes = struct.pack('i', len(configuration.signalType))
    signalTypeBytes = struct.pack('%ds' % len(configuration.signalType), bytes(configuration.signalType, 'utf-8'))
    noiseLengthBytes = struct.pack('i', len(configuration.noise))
    noiseBytes = struct.pack('%ds' % len(configuration.noise), bytes(configuration.noise, 'utf-8'))
    t1Bytes = struct.pack('f', configuration.time1)
    f1Bytes = struct.pack('f', configuration.freq1)
    signalLength = struct.pack('f', len(signal))
    signalBytes = struct.pack('%sf' % len(signal), *signal)
    imagPointsLength = struct.pack('f', len(imagPoints))
    imagPointsBytes = struct.pack('%sf' % len(imagPoints), *imagPoints)
    newFile.write(t0Bytes)
    newFile.write(timeBytes)
    newFile.write(frequencyBytes)
    newFile.write(amplitudeBytes)
    newFile.write(numberOfSamplesBytes)
    newFile.write(infiltratorBytes)
    newFile.write(jumpMomentBytes)
    newFile.write(possibilityBytes)
    newFile.write(jumpSampleBytes)
    newFile.write(signalTypeLengthBytes)
    newFile.write(signalTypeBytes)
    newFile.write(noiseLengthBytes)
    newFile.write(noiseBytes)
    newFile.write(t1Bytes)
    newFile.write(f1Bytes)
    newFile.write(signalLength)
    newFile.write(signalBytes)
    newFile.write(imagPointsLength)
    newFile.write(imagPointsBytes)


def read(filename):
    newFile = open(filename, "rb")
    time0 = struct.unpack('f', newFile.read(4))[0]
    time = struct.unpack('f', newFile.read(4))[0]
    frequency = struct.unpack('f', newFile.read(4))[0]
    amplitude = struct.unpack('f', newFile.read(4))[0]
    numberOfSamples = struct.unpack('i', newFile.read(4))[0]
    infiltrator = struct.unpack('f', newFile.read(4))[0]
    jumpMoment = struct.unpack('f', newFile.read(4))[0]
    possibility = struct.unpack('f', newFile.read(4))[0]
    jumpSample = struct.unpack('i', newFile.read(4))[0]
    signalTypeLength = struct.unpack('i', newFile.read(4))[0]
    signalType = bytes.decode(struct.unpack('%ds' % signalTypeLength, newFile.read(signalTypeLength))[0])
    noiseLength = struct.unpack('i', newFile.read(4))[0]
    noise = bytes.decode(struct.unpack('%ds' % noiseLength, newFile.read(noiseLength))[0])
    time1 = struct.unpack('f', newFile.read(4))[0]
    freq1 = struct.unpack('f', newFile.read(4))[0]
    signalLength = struct.unpack('f', newFile.read(4))[0]
    signal = struct.unpack('f'*int(signalLength), newFile.read(4*int(signalLength)))
    imagPointsLength = struct.unpack('f', newFile.read(4))[0]
    imagPoints = struct.unpack('f' * int(imagPointsLength), newFile.read(4 * int(imagPointsLength)))

    configuration = config.Configuration(time0, time, frequency, amplitude, numberOfSamples, infiltrator, jumpMoment, possibility, jumpSample, signalType, noise, time1, freq1)
    configuration.setPoints(signal)
    configuration.setImagPoints(imagPoints)
    return configuration

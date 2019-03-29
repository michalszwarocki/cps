import struct
import Logic.Configuration as config


def save(fileName, configuration, signal):

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
    signalBytes = struct.pack('%sf' % len(signal), *signal)
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
    newFile.write(signalBytes)


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
    signal = struct.unpack('f'*numberOfSamples*int(time), newFile.read(4*numberOfSamples*int(time)))

    configuration = config.Configuration(time0, time, frequency, amplitude, numberOfSamples, infiltrator, jumpMoment, possibility, jumpSample, signalType, noise)
    configuration.setPoints(signal)
    return configuration

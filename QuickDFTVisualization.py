# @Author: ibanrohazz
# This program will take an array of data points and return the Discrete Fourier Transform of the data
# It will also plot the real, imaginary, magnitude, and phase of the DFT

import numpy as np
import matplotlib.pyplot as plt

def DFT(data):
    return np.fft.fft(data)

def plotDFT(data):
    dft = DFT(data)
    real = dft.real
    imag = dft.imag
    mag = np.abs(dft)
    phase = np.angle(dft)
    
    plt.figure()
    plt.subplot(221)
    plt.plot(real)
    plt.title('Real')
    plt.subplot(222)
    plt.plot(imag)
    plt.title('Imaginary')
    plt.subplot(223)
    plt.plot(mag)
    plt.title('Magnitude')
    plt.subplot(224)
    plt.plot(phase)
    plt.title('Phase')
    plt.show()
    
# data = np.array([1/3, 1/3, 0, 0, 0, 0, 0, 1/3]) #2a
# data = np.array([1/3, 1/3, 1/3, 0, 0, 0, 0, 0]) #2b
# data = np.array([1, 1/(2**.5), 0, -1/(2**.5), -1, -1/(2**.5), 0, 1/(2**.5)]) #2c
# data = np.array([1, -1, 1, -1, 1, -1, 1, -1]) #2d
data = np.array([1, 1, 1, 1, -1, -1, -1, -1]) #2e

dft = DFT(data)
plotDFT(data)
print(dft)

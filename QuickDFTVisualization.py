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

def plotData(data):
    plt.plot(data)
    plt.show()

# Question 2 Data 
def question2():
    data = np.array([1/3, 1/3, 0, 0, 0, 0, 0, 1/3]) #2a
    # data = np.array([1/3, 1/3, 1/3, 0, 0, 0, 0, 0]) #2b
    # data = np.array([1, 1/(2**.5), 0, -1/(2**.5), -1, -1/(2**.5), 0, 1/(2**.5)]) #2c
    # data = np.array([1, -1, 1, -1, 1, -1, 1, -1]) #2d
    # data = np.array([1, 1, 1, 1, -1, -1, -1, -1]) #2e
    
    plotDFT(data)
    print(DFT(data))

# Question 3 Data
def question3():
    # a 256 samples array ie one cycle of the cosine in the array 
    # data = np.cos(np.linspace(0, 2*np.pi, 256))
    # a 64 samples array ie four cycles of the cosine in the array
    data = np.cos(np.linspace(0, 8*np.pi, 64))
    # a sine with period equal to 64 
    # data = np.sin(np.linspace(0, 2*np.pi, 64))
    # a 64 samples cos array with a phase shift of pi/4
    # data = np.cos(np.linspace(0, 8*np.pi, 64) + np.pi/4)
    # a cosine with a period of 16 samples  
    # data = np.cos(np.linspace(0, 2*np.pi, 16))
    
    plotData(data)
    plotDFT(data)
    print(DFT(data))

def run():
    data = input("Enter data: ")
    data = np.array(data)
    plotDFT(data)
    print(DFT(data))
    
if  __name__ == '__main__':
    # run()
    # question2()
    question3()

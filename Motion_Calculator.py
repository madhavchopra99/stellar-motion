import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    path = Path('./spectra_data.npy')
    spectra = np.load(path)
    spectra = spectra * 1.0e-11
    # print(spectra[0])
    nObs = np.size(spectra, 0)
    lambdaStart = 630.02
    lambdaDelta = 0.14
    lambdaEnd = lambdaStart + (nObs - 1) * lambdaDelta
    lambdaa = np.arange(lambdaStart, lambdaEnd, lambdaDelta)
    # lambdaa = lambdaa.transpose()  #optional
    # print(np.shape(spectra))
    s = spectra[:, 5]
    plt.figure('Stellar Motion')
    plt.loglog(lambdaa, s, '.-')
    plt.xlabel('Wavelength')
    plt.ylabel('Intensity')
    # plt.show()
    # print(s)
    sHa = np.min(s)
    idx = np.where(s == np.min(s))
    lambdaHa = lambdaa[idx]
    # print(lambdaHa, idx[0], sHa)
    plt.plot(lambdaHa, sHa, 'rs', markersize=4)
    plt.show()
    z = (lambdaHa / 656.28) - 1
    speed = z * 299792.458
    print(f"Redshift factor 'z' is {z[0]}\nSpeed is {speed[0]} Km/s")


if __name__ == '__main__':
    main()

import numpy as np
import os

def noisy(noise_typ,image, monochanel = False):

    if monochanel:
        row, col = image.shape
    else:
        row, col, ch= image.shape

    if noise_typ == "gauss":
        mean = 0
        var = 0.1
        sigma = var**0.5
        if monochanel:
            gauss = np.random.normal(mean,sigma,(row,col))
            gauss = gauss.reshape(row,col)
        else:
            gauss = np.random.normal(mean, sigma, (row, col, ch))
            gauss = gauss.reshape(row, col, ch)
        noisy = image + gauss
        return noisy

    elif noise_typ =="speckle":
        if monochanel:
            gauss = np.random.randn(row,col)
            gauss = gauss.reshape(row,col)
        else:
            gauss = np.random.randn(row, col, ch)
            gauss = gauss.reshape(row, col, ch)        
        noisy = image + image * gauss
        return noisy
  else:
        print('Bad boy...')
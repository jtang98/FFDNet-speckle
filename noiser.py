import numpy as np

def noisy(image):
    row, col = image.shape
    mean = 0
    var = 100
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma,(row, col))
    gauss = gauss.reshape(row, col)
    noisy = image + gauss
    return noisy

import skimage.io

lena = skimage.io.imread('testsets/set_gaussian/goldhill.bmp')
lena = noisy(lena)
print(lena[0:10, 0:10])
skimage.io.imsave('testsets/set_gaussian/goldhill.bmp', lena)
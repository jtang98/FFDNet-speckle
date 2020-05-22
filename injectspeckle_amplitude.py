#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 13:12:23 2018

@author: emasasso
"""
import numpy as np
import skimage.io

def injectspeckle_amplitude(img,L):
    rows = img.shape[0]
    columns = img.shape[1]
    s = np.zeros((rows, columns))
    for k in range(0,L):
        gamma = np.abs( np.random.randn(rows,columns) + np.random.randn(rows,columns)*1j )**2/2
        s = s + gamma
    s_amplitude = np.sqrt(s/L)
    ima_speckle_amplitude = np.multiply(img,s_amplitude)
    return ima_speckle_amplitude

im = skimage.io.imread('testsets/set5/woman.bmp')
im = 0.2125 * im[:,:,0] + 0.7154 * im[:,:,1] + 0.0721 * im[:,:,2]
speckled_image = injectspeckle_amplitude(im, 5)
speckled_image = speckled_image.astype('uint8')
skimage.io.imsave('testsets/set_speckle/woman.bmp',speckled_image)

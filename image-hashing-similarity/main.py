# https://github.com/JohannesBuchner/imagehash
#   -> https://github.com/JohannesBuchner/imagehash/blob/master/imagehash.py

from PIL import Image
from imagehash import average_hash, phash, dhash, whash

img1_p ='empty-checkbox.jpg'
img2_p ='ticked-checkbox.jpg'
img1 = Image.open(img1_p)
img2 = Image.open(img2_p)

avgHashDiff = average_hash(img1) - average_hash(img2) 
pHashDiff   = phash(img1) - phash(img2) 
dHashDiff   = dhash(img1) - dhash(img2) 
wHashDiff   = whash(img1) - whash(img2) 

cutoff = 5

print ('image-1:', img1_p)
print ('image-2:', img2_p)

print ('\nResult: ')
print ('----------------------------')
print (f'Average    hash diff: {avgHashDiff}')
print (f'Perceptual hash diff: {pHashDiff}')
print (f'Difference hash diff: {dHashDiff}')
print (f'Wavelet    hash diff: {wHashDiff}')
print ('----------------------------')

if avgHashDiff < cutoff:
  print('Images are similar')
else:
  print('Images are not similar')
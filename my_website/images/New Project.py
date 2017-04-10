'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              

directory = os.path.dirname(os.path.abspath(__file__)) 
instagram_logo = os.path.join(directory, 'instagram_logo.png')
instagram_logo = PIL.Image.open(instagram_logo)

batmans_face = os.path.join(directory, 'batmans_face.png')
batmans_face = PIL.Image.open(batmans_face)
batmans_face = batmans_face.resize((600,600))


instagram_logo.paste(batmans_face, (275, 225), mask=batmans_face)

fig, axes = plt.subplots(1, 1)
axes.imshow(instagram_logo, interpolation='none')

fig.show()

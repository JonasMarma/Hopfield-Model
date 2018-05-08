# Hopfield-Model
The Hopfield Model is a neural associative memory model in wich every pixel in an image is considered as a neuron that may have and activations of 1 or -1. Each neuron interacts with all other neurons to decide it's new value in order to minimize the total energy, converging to a pre-memorized pattern.
In this repository, I created a module named "hopfield.py", where all the calculations that belong to the Hopfield Model are done, and a "main.py" class, where the module is applied to store information about any image the user inputs and then try to orrect a corrupted version of an image the user has stored.
I made this based on the video lectures given by Wulfram Gerstner, avaliable at:
http://lcn.epfl.ch/~gerstner/VideoLecturesGerstner.html
The Hopfield Model is explained at week 5.

# Hopfield-Model
The Hopfield Model is a neural associative memory model in wich every pixel in an image is considered as a neuron that may have and activations of 1 or -1. Each neuron interacts with all other neurons to decide it's new value in order to minimize the total energy, converging to a pre-memorized pattern.

In this repository, I created a module named "hopfield.py", where all the calculations that belong to the Hopfield Model are done, and a "main.py" class, where the module is applied to store information about any image the user inputs and then try to correct a corrupted version of an image the user has stored.

I made this based on the video lectures given by Wulfram Gerstner, avaliable at:
http://lcn.epfl.ch/~gerstner/VideoLecturesGerstner.html
The Hopfield Model is explained at week 5.
I also uploaded some images showing results from a simulation using the four given images.




O Modelo de Hopfield é um modelo de rede neural de memória associativa onde cada pixel em uma imagem é considerado como um neurônio que pode ter e ativações de 1 ou -1. Cada neurônio interage com todos os outros neurônios para decidir seu novo valor a cada iteração, a fim de minimizar a energia total, convergindo para um padrão pré-memorizado.

Neste repositório, eu criei um módulo chamado "hopfield.py", onde são feitos todos os cálculos que pertencem ao modelo de Hopfield, e uma classe "main.py", onde o módulo é aplicado para armazenar informações sobre imagens que o usuário deseje. Em seguida, o módulo tenta corrigir uma versão corrompida de uma imagem que o usuário armazenou.

Fiz isso com base nas vídeo-aulas dadas por Wulfram Gerstner, disponíveis em:
http://lcn.epfl.ch/~gerstner/VideoLecturesGerstner.html
O modelo de Hopfield é abordado na semana 5.
Eu também incluí aqui algumas imagens mostrando resultados de execuções usando as imagens dadas como exmeplo.

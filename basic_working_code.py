import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

colors = {count:(a,a,a) for count,a in enumerate(range(0,257,  int(259/9)))}
len(colors)

def integer_to_matrix(integer, height=3,width=3):
    length = height * width
    integer_string = f'{integer}'.rjust(length, '0')
    encoded_integer = '1'+ integer_string
    matrix = []
    slices = []
    for i in range(0, len(integer_string), width):
        slices.append(i)
    slices.append(len(integer_string))
    start = [a for a in slices[:-1]]
    end = [a for a in slices[1:]]
    for count, i in enumerate(start):
        row = integer_string[i:end[count]]
        print(row)
        matrix.append(row)
    return matrix
  
  #example
  my_num = integer_to_matrix(1, 5,5)
  
# results in ---->
# 00000
# 00000
# 00000
# 00000
# 00001

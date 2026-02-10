import numpy as np

A= np.arange(0,24)
B= A.reshape(4,3,2)
C=np.array(B)
Tr= (C.transpose(0,2,1))
print("Final Shape:",Tr.shape)
print("The Array:\n",Tr)
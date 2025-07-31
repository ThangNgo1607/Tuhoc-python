import numpy as np
a=np.ones((5,5))
b=np.zeros((5,5))
"""print(a)
print(b)
a[0,:]=0
a[-1,:]=0 # b[4,:]
a[:,0]=0
a[:,-1]=0   #a[:,4]
print(a)
b[0,:]=1
b[-1,:]=1 # b[4,:]
b[:,0]=1
b[:,-1]=1  #b[:,4] 
print(b)"""
#Cách 2:
a[1:-1,1:-1]=0
print(a)
b[1:-1,1:-1]=1
print(b)
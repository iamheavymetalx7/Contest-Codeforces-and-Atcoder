import numpy as np
 
a,b,d=map(int,input().split())
 
 
cos=np.cos(d*np.pi/180)
sin=np.sin(d*np.pi/180)
 
x=(a*cos-b*sin)
y=(a*sin+b*cos)
 
print(str(x)+' '+str(y))
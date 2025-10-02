import matplotlib.pyplot as pl 
import numpy as np 

#setting up 3d 
fig = pl.figure()
ax = fig.add_subplot(111, projection = '3d')

#values 
x = np.arange(0,50)
y = np.arange(0,100)

X,Y = np.meshgrid(x,y)

Z = X**2 + Y**2

ax.plot_surface(X,Y,Z)
ax.set_title('Plane')


pl.show()
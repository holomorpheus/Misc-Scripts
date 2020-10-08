"""
Created by: Gabriel Martins
Modified from an earlier script by: Raibatak Das
Date: Oct 7 2020

"""

# Importing Libraries.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.constants import golden

# Naming trig functions, pi and phi.
cos, sin = np.cos, np.sin;
pi = np.pi; 
phi = golden;


#------------------------------------
# Chossing between Archimedean or Golde spiral

Archimedes = False;

Golden = True;

#------------------------------------
# Aesthetic choices

# How many spirals?
N = 6;

# How many gridpoints?
anglegridsize = 4*128;

# Which colormap?
colormapname = 'viridis'

# Plot diagonals?
diagonals = True;

#------------------------------------
# Defining the radial function

if Archimedes and Golden:
    print("You can't have both at once silly.")
    quit()
else:
    if Archimedes:
        # Archimedes
        def f(theta,a):
            return a*theta
    elif Golden:
        def f(theta,a):
            return a*phi**(2*theta/pi)
    else:
        print("No spirals today?")
        quit() 

#------------------------------------
# Defining spirals

# List of spiral indices
index = np.array([i for i in range(1,N+1)]);

# Colors for the spirals.
colormap = cm.get_cmap(colormapname, len(index));
colors = colormap(np.linspace(1,0,len(index)));

# Define array of angles
if Archimedes:
    theta = np.linspace(0, 3*pi, anglegridsize);
else:
    theta = np.linspace(-6*pi, 6*pi, anglegridsize);

# Define different spirals.
spirals = np.zeros((len(index),2,anglegridsize));
for i in range(len(index)):
    rtheta = f(theta,i+1)
    spirals[i,:,:] =np.matrix([rtheta*cos(theta),rtheta*sin(theta)]);

#------------------------------------
# Plotting

# Scope
scope  = rtheta[int(2*anglegridsize/3)]+.5;

# Define figure and axes objects.
fig, ax = plt.subplots(figsize=(5, 5))

# Plot axes
ax.axhline(y=0, color='k', alpha=0.5)
ax.axvline(x=0, color='k',alpha=0.5)

# Plot diagonals.
if diagonals:
    ax.plot([-scope, scope], [-scope, scope], color='k',alpha=0.5)
    ax.plot([-scope, scope], [scope, -scope], color='k',alpha=0.5)

# Plot spirals.
for i in range(len(index)):
    ax.plot(spirals[i,0,:], spirals[i,1,:], color=colors[i], alpha=0.8)
ax.grid(True)
ax.axis("equal")
ax.set_xlim([-scope, scope])
ax.set_ylim([-scope, scope])
ax.set_title("Uzumaki")


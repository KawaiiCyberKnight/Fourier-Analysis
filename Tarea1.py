# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:26:20 2020

@author: Christian Quintanar
"""

from matplotlib import pyplot as plt
from matplotlib import rc
import numpy as np

plt.rc('text', usetex=True)
plt.rcParams.update({'font.size': 14})

A = 1
a = np.pi/2

def f1(x):
    return A*np.float_power(a, x)

def f2(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        return 1/x

def f3(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.float_power(x, -2)

def f4(x):
    res = np.tan(x)
    pos = np.where(np.abs(np.diff(res)) >= 0.5)[0]
    res[pos]=np.nan
    return res

def f5(x):
    res = np.cos(x)/np.sin(x)
    pos = np.where(np.abs(np.diff(res)) >= 0.5)[0]
    res[pos]=np.nan
    return res

def f6(x):
    return np.power(x,2) + a

def f7(x):
    return np.power(x+a,2)

def f8(x):
    return np.log(x)

def f9(x):
    return np.log(3+np.float_power(x,2))

def f10(x):
    return np.tan(x/(8*np.float_power(x,2)+3))

def f11(x):
    res = np.sign(x)
    pos = np.where(np.abs(np.diff(res)) >= 0.5)[0]
    res[pos]=np.nan
    return res

def f12(x):
    return np.sin(x+a)

t = np.linspace(-7,7,7001)


fig, ax = plt.subplots(3,4)

for x in range(3):
    for y in range(4):
        ax[x][y].xaxis.set_major_locator(plt.MultipleLocator(2))
        ax[x][y].xaxis.set_minor_locator(plt.MultipleLocator(1))
        ax[x][y].yaxis.set_major_locator(plt.MultipleLocator(2))
        ax[x][y].yaxis.set_minor_locator(plt.MultipleLocator(1))
        ax[x][y].grid(True, which='major', linestyle='--', linewidth=1)
        ax[x][y].grid(True, which='minor', linestyle=':', linewidth=0.8)
        ax[x][y].spines['left'].set_position('zero')
        ax[x][y].spines['right'].set_color('none')
        ax[x][y].yaxis.tick_left()
        ax[x][y].spines['bottom'].set_position('zero')
        ax[x][y].spines['top'].set_color('none')
        ax[x][y].xaxis.tick_bottom()
        ax[x][y].set_ylim(-7,7)

ax[0][0].plot(t, f1(t), linewidth=3.0)
ax[0][0].title.set_text(r'$f_1(x)=Aa^x$')

ax[0][1].plot(t, f2(t), linewidth=3.0)
ax[0][1].title.set_text(r'$f_2(x)=\frac{1}{x}$')

ax[0][2].plot(t, f3(t), linewidth=3.0)
ax[0][2].title.set_text(r'$f_3(x)=\frac{1}{x^2}$')

ax[0][3].plot(t, f4(t), linewidth=3.0)
ax[0][3].title.set_text(r'$f_4(x)=tan(x)$')

ax[1][0].plot(t, f5(t), linewidth=3.0)
ax[1][0].title.set_text(r'$f_5(x)=ctg(x)$')

ax[1][1].plot(t, f6(t), linewidth=3.0)
ax[1][1].title.set_text(r'$f_6(x)=(x^2+a)$')

ax[1][2].plot(t, f7(t), linewidth=3.0)
ax[1][2].title.set_text(r'$f_7(x)=(x+a)^2$')

ax[1][3].plot(t, f8(t), linewidth=3.0)
ax[1][3].title.set_text(r'$f_8(x)=lnx$')

ax[2][0].plot(t, f9(t), linewidth=3.0)
ax[2][0].title.set_text(r'$f_9(x)=ln(3+x^2)$')

ax[2][1].plot(t, f10(t), linewidth=3.0)
ax[2][1].set_ylim(-0.2,0.2)
ax[2][1].yaxis.set_major_locator(plt.MultipleLocator(0.1))
ax[2][1].yaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax[2][1].title.set_text(r'$f_{10}(x)=tan(\frac{x}{8x^2+3})$')

ax[2][2].plot(t, f11(t), linewidth=3.0)
ax[2][2].set_ylim(-2,2)
ax[2][2].yaxis.set_major_locator(plt.MultipleLocator(1))
ax[2][2].yaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax[2][2].title.set_text(r'$f_{11}(x)=sign(x)$')

ax[2][3].plot(t, f12(t), linewidth=3.0)
ax[2][3].title.set_text(r'$f_{12}(x)=sin(x+a)$')

plt.show()
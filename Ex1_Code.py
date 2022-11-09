# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:42:14 2022

Projectile Motion Under Air Resistance

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

B = 1.6*10-4
C = 0.25

def Res(D,V,linear,quadratic):
    
    DV = D*V
    res = 0
    b = B*D
    c = C*D**2
    lin = 0
    quad = 0
    
    if linear == True:
        lin += b*V
        
    if quadratic == True:
        quad += c*V**2
    
    return(D,V,DV,lin+quad,lin,quad)

DVs = []
for i in np.arange(-3,5,0.1):
    DVs.append(10**i)

Vs = []
Ds = []
for i in range(len(DVs)):
    Ds.append(DVs[i]**0.5)
    Vs.append(DVs[i]**0.5)

Ress = []
for i in range(len(DVs)):
    Ress.append(Res(Ds[i],Vs[i], True, True)[3])
    
lin_Ress = []
for i in range(len(DVs)):
    lin_Ress.append(Res(Ds[i],Vs[i], True, True)[4])

quad_Ress = []
for i in range(len(DVs)):
    quad_Ress.append(Res(Ds[i],Vs[i], True, True)[5])



lin_frac = [lin_Ress[i]/Ress[i] for i in range(len(Ress))]
quad_frac = [quad_Ress[i]/Ress[i] for i in range(len(Ress))]

plt.plot(np.log(DVs), np.log(Ress))
plt.xlabel(r'$\log(DV)$')
plt.ylabel(r'$\log(R)$')
plt.title("Log Plot Of Resistance Vs DV")
plt.savefig("Ex1_Log_Plot.png", dpi = 300)
plt.show()
"""
This demonstrates the phase transition from linear to quadratic phase
"""
plt.plot(np.log(DVs),lin_frac)
plt.plot(np.log(DVs), quad_frac)
plt.xlabel(r'$\log(DV)$')
plt.ylabel("Proportion of R generated")
plt.title("Contribution Of Linear and Quadratic Terms Around Transition Point")
plt.legend(["Linear Contribution", "Quadratic Contribution"])
plt.savefig("Ex1_Contributions.png",dpi = 300)
plt.show()
        


B = 1.6E-4
##analytic solution of given equation
g = 9.81
m= 10E-8
D = 10E-4
b = B*D
gamma = b/m

t=0
dt = 10**-3
t_max = 2

V_0 = 10
theta = np.pi/3
Vx = V_0*np.cos(theta)
Vy = V_0*np.sin(theta)
VxR = V_0*np.cos(theta)
VyR = V_0*np.sin(theta)

ts = np.arange(0,t_max,dt)

VyRs = []
VxRs = []
Vys = []
Vxs = []



while len(Vxs) < t_max/dt:
    VyRs.append(VyR)
    dVR = -g*dt - (b/m)*VyR*dt
    VyR += dVR
    
    Vys.append(Vy)
    dV = -g*dt
    Vy += dV
    
    Vxs.append(Vx)
    dV = 0
    Vx+=dV

    VxRs.append(VxR)
    dVR = (-b/m)*VxR*dt
    VxR+=dVR
    
    t += dt

plt.plot(ts,VxRs)
plt.plot(ts,VyRs)
plt.legend([r'V_x',r'V_y'])
plt.title('Components Of The Velocity Under Air Resiatnce')
plt.show()

plt.plot(ts,Vxs)
plt.plot(ts,Vys)
plt.legend([r'V_x',r'V_y'])
plt.title('Components Of The Velocity Without Air Resiatnce')
plt.show()

Y = 0
X = 0    
Ys = []
Xs= []

YR = 0
XR = 0    
YRs = []
XRs= []

t = 0

while 0 <= Y:
    dt = 10**-3
    step = int(t/dt)
    t = t + dt
    
    Ys.append(Y)
    dY = Vys[step]*dt
    Y += dY
    
    Xs.append(X)
    dX = Vxs[step]*dt
    X += dX

    
print(len(Xs), len(Ys))
t = 0

while 0 <= YR:
    
    step = int(t/dt)
    YRs.append(YR)
    dYR = VyRs[step]*dt
    YR += dYR
    
    XRs.append(XR)
    dXR = VxRs[step]*dt
    XR += dXR
     
    t += dt


plt.plot(Xs, Ys)
plt.plot(XRs,YRs)
plt.legend(['Without Resistance', 'With Resistance'])
plt.title(r'Ballistic Trajectories, $\theta_0 = \pi/3$')

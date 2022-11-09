C = 0.25
##analytic solution of given equation
g = 9.81
c = C*D**2
b = B*D
gamma = b/m

t=0
dt = 10**-3
t_max = 100

VxR = V_0*np.cos(theta)
VyR = V_0*np.sin(theta)

ts = np.arange(0,t_max,dt)

VyRs = []
VxRs = []

t = 0

while len(VxRs) < t_max/dt:
    VyRs.append(VyR)
    VxRs.append(VxR)
    
    dVRx = -(c/m)*np.sqrt(VyR**2+VxR**2)*VxR*dt
    dVRy = -g*dt -(c/m)*np.sqrt(VyR**2+VxR**2)*VyR*dt
    VyR += dVRy
    VxR += dVRx
    
    t += dt


YR = 0
XR = 0    
YRs = []
XRs= []

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

plt.plot(XRs,YRs)
plt.title("Comparison of linear, quadratic, and no air resistance")
plt.legend(['No Resistance', 'Resistance Linear With Velocity', 'Resistance quadratic With Velocity'], loc = 'lower right')
plt.text(0,1.5,"m = " + str(m)  + "\n theta_0 = pi/5"  + "\n V_0 = " + str(V_0), fontdict=None)
plt.xlabel("X Posistion (m)")
plt.ylabel('Y Posistion (m)')
plt.savefig("Ex4_3.png",dpi=300)
plt.show()

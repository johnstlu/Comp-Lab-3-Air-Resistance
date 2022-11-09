B = 1.6E-4
##analytic solution of given equation
g = 9.81
m= 10E-8
D = 10E-4
b = B*D
gamma = b/m

t=0
dt = 10**-3
t_max = 5

range_theta_pair = [0,0]
ms = []
for i in np.arange(-10,2,0.1):
    ms.append(10**i)

thetas = []
ranges = []
for m in ms:
    for theta in np.arange(0,np.pi/2,10**-1):
        V_0 = 10
        theta = np.pi/3
        VxR = V_0*np.cos(theta)
        VyR = V_0*np.sin(theta)
        
        ts = np.arange(0,t_max,dt)
        
        VyRs = []
        VxRs = []
        
        while len(VxRs) < t_max/dt:
            VyRs.append(VyR)
            dVR = -g*dt - (b/m)*VyR*dt
            VyR += dVR
            
            VxRs.append(VxR)
            dVR = (-b/m)*VxR*dt
            VxR+=dVR
            
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
        
        if XRs[-1] > range_theta_pair[0]:
            range_theta_pair = [XRs[-1],theta]
        else:
            break
    
        print(range_theta_pair)
    ranges.append(range_theta_pair[0])
    thetas.append(range_theta_pair[1])
    
plt.plot(np.log(ms),ranges)
plt.xlabel("log(mass) (kg)")
plt.ylabel("Range (m)")
plt.title("Range Of Projectile at Optimum Launch Angle")
plt.savefig('Ex3b_Range.png',dpi = 300)
plt.show()

plt.plot(np.log(ms),thetas)
plt.xlabel("log(mass) (kg)")
plt.ylabel("Optimum Angle (Radians)")
plt.title("Optimum Launch Angle vs Mass")
plt.savefig('Ex3b_Angle.png',dpi = 300)
plt.show()

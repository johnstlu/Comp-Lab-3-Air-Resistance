B = 1.6E-4
##analytic solution of given equation
g = 9.81
rho = (2*10**3)
D = 10**(-4)
V = (4/3)*np.pi*((D/2)**3)
m = rho*V
b = B*D
gamma = b/m

def v_anal(t):
    return (g/gamma)*(np.exp(-gamma*t)-1)

t_0 = 0
t_1 = 1
dt = 10**-3

V_0 = 0

ts = np.arange(t_0,t_1,dt)
anal_Vs = [v_anal(t) for t in ts]

Vs = []

t = t_0
V = V_0

while t <= t_1:
    Vs.append(V)
    V += -g*dt -gamma*V*dt
    t += dt

print(Vs)
plt.plot(ts,Vs)
plt.legend(['Numerical Solution'])
plt.xlabel("time(s)")
plt.ylabel("speed(m/s")
plt.title("Numerical Solution To Falling Dust Under Air Resistance")
plt.savefig("Ex2_numerical_sol.png", dpi = 300)
plt.show()


def error():
    errors = []
    for i in range(len(Vs)):
        error = (-anal_Vs[i]+Vs[i])/anal_Vs[i]
        errors.append(error)
    return errors

errors = error()

plt.plot(ts,errors)
plt.title("Error in the numerical Solution")
plt.xlabel('time(s)')
plt.ylabel('error')
plt.savefig("Ex2_error", dpi = 300)
plt.show()

#time to hit ground vs time
def h_anal(t,m):
    return -(g*m/b)*(t+ (m/b)*(np.exp(-b*t/m)-1))

ms = []
for i in np.arange(-10,-7,0.5):
    ms.append(10**i)
    
print(ms)
for m in ms:    
    plt.plot(ts,h_anal(ts,m))
    
plt.legend(["m = 1e-10 kg", "m =  3.16e-10 kg","m = 1e-09 kg","m = 3.16e-09 kg","m = 1e-8 kg","m = 3.16e-10 kg",])
plt.xlabel('time(s)')
plt.ylabel('height(m)')
plt.savefig("Ex2_height_vs_mass.png", dpi = 300)

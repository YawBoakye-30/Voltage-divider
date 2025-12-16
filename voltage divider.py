import numpy as np
import matplotlib.pyplot as plt
print('Welcome to the Voltage Divider program')
Vs=input('The supply voltage in volts is: ')
print(Vs +' volts')
R1=input('The first resistance in ohms is: ')
print(R1 +' ohms')
R3=input('The third resistance in ohms is: ')
print(R3+' ohms')
R2=input('The second resistance in ohms is: ')
print(R2+' ohms')
Rtotal=int(R1)+int(R2)+int(R3) # calculates the total resistance
print(Rtotal,'ohms')
I=int(Vs)/Rtotal
print(I,'A')
V1=int(Vs)*int(R1)/Rtotal
print(V1,'V')
V2=I*int(R2)
print(V2,'V')
V3=I*int(R3)
print(V3,'V')
P1=I*V1
print(P1,'W')
P2=I*V2
print(P2,'W')
P3=I*V3
print(P3,'W')
Ra=int(R1)+int(R3)
R2=np.linspace(1,100,1000) # uniform difference betwwen the resistance values
R_total=Ra+R2
print(R_total)
I=int(Vs)/R_total
print(I)
V2=I*R2
print(V2)
P2=I*V2
plt.figure()
plt.plot(R2,V2,'r')
plt.title('V2 against R2 for different resistance')
plt.xlabel('Resistance in ohms')
plt.ylabel('Voltage in Volts')
plt.grid(True)
plt.figure()
plt.plot(R2,P2,'r')
plt.title('P2 against R2 for different resistance')
plt.xlabel('Resistance in ohms')
plt.ylabel('Power in Watts')
plt.grid(True)
plt.show()



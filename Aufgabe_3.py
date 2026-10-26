import matplotlib.pyplot as plt
import numpy as np
#rom Aufgabe_1
import Aufgabe_1 as A1
# Definitionen


# Ausführung


print(A1.x_i)

y_i = A1.f_1(A1.x_i)
y_i = A1.f_2(A1.x_i)
y_i = A1.f_3(A1.x_i) 
y_i = A1.f_4(A1.x_i) 
y_i = A1.f_5(A1.b_i)


x=np.linspace(-20, 20)
y=A1.f_5(x)

fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()

x=np.linspace(-20, 20)
y=A1.f_3(x)

fig, ay = plt.subplots()
ay.plot(x,y)
plt.show()
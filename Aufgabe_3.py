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


x=np.linspace(-20, 20, 41)
y=A1.f_5(x)
fig = plt.figure
fig,ax = plt.subplots(figsize=(10, 10), layout='constrained')
ax.plot(x,y, color= "red", linewidth =3, label = "linear")
y=A1.f_3(x)
ax.plot(x,y, color= "lime", linewidth =2, label = "parabel")
y=A1.f_4(x)
ax.plot(x, y, color = "black", linewidth = 2, linestyle = '--', label= "linear")
ax.set_title("Three functions")
ax.yaxis
ax.xaxis
# ax.yaxis.set_major_locator
ax.legend()
ax.grid()
ax.set_xlabel("X Koordinate")
ax.set_ylabel("Y Koordinate")
ax.yaxis.set_minor_locator
ax.xaxis.set_minor_locator
ax.yaxis.set_major_formatter
ax.xaxis.set_major_formatter
ax.spines




plt.show()

# x=np.linspace(-20, 20, 41)
# y=A1.f_3(x)


# fig, ay = plt.subplots()
# ay.plot(x,y)
# plt.show()
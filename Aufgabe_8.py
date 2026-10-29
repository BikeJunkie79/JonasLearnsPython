import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(projection='3d')





x= []
y= []
X, Y = np.meshgrid(x,y)
z= []
Z= X**2 + Y**2



with open("Data/skateboard.obj")as datei:
    for zeile in datei:
        if zeile.startswith("v"):
            teile = zeile.split()
            if float(teile[3]) != -2.0 and float(teile[1]) != -1.0:
                x.append(float(teile[1]))
                y.append(float(teile[2]))
                z.append(float(teile[3]))

print("Punkte eingelesen:", len(x))
# Unterabtastung: Nur jeden 10. Punkt nehmen
x_downsampled = x[::10]
y_downsampled = y[::10]
z_downsampled = z[::10]
print("Unterabtsatung:", len(x_downsampled))
ax.scatter(x_downsampled, y_downsampled, z_downsampled, s=1, c=z_downsampled)
ax.yaxis
ax.set_xlabel ("X Koordinate", fontsize= 15, color= "darkblue")
ax.xaxis
ax.set_ylabel ("Y Koordinate", fontsize= 15, color= "darkblue")
ax.zaxis
ax.set_zlabel ("Z Koordinate", fontsize= 15, color= "darkblue")
ax.plot_surface(X, Y, Z, cmap= 'viridis')
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=10, azim= -90)


plt.show()
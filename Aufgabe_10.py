import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_subplot()
x=[]
y=[]
z=[]


with open("Data/skateboard.obj")as datei:
    for zeile in datei:
        if zeile.startswith("v "):
            teile = zeile.split()
            x.append(float(teile[1]))
            y.append(float(teile[2]))
            z.append(float(teile[3]))

spalten = len(np.unique(x))
zeilen = len(np.unique(y))
print(spalten, "x", zeilen, "=", spalten * zeilen, "| Punkte:", len(z))

bild = np.array(z).reshape(spalten, zeilen).T
bild[bild == -2.0] = np.nan

im = ax.imshow(bild, cmap="viridis")
fig.colorbar(im, ax=ax, label= "Höhe z")
plt.show()
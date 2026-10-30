import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
# ax=fig.add_subplot()
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
zeile, spalte = np.unravel_index(np.nanargmax(bild),bild.shape)
print("höchster Punkt:", bild[zeile, spalte])
ax1.plot(spalte, zeile, "ro", markersize=10)
ax1.annotate("höchster Punkt", xy=(spalte, zeile), xytext=(spalte + 60, zeile - 30),color="red", arrowprops={"arrowstyle": "->", "color": "red"})

im = ax1.imshow(bild, cmap="viridis")

profil = bild[zeilen // 2, :]
im = ax2.imshow(profil, cmap="viridis")

fig.colorbar(im, ax=ax1, label= "Höhe z")
plt.show()
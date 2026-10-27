# Jonas Weg zum Python-Entwickler

Diese Aufgabensammlung werden wir stetig erweitern. Die Aufgaben werden immer schwieriger und Du wirst immer mehr von der Programmiersprache Python lernen.

Die ersten Aufgaben werden noch nichts mit den Daten der Schweißnahtinspektion "VIRO WSI" zu tun haben. Spätere Aufgaben, vielleicht schon welche am Ende der  Wochen stehen.

Du wirst Daten von Deinen eigenen Scans nutzen und eine (kleine) Funktionalitäten, selbst bauen. 


## Zwischen den Aufgaben

Wie bereits besprochen, nutze https://checkio.org/ , um im Selbststudium Dich die Programmiersprache **Python** zu erlernen.
Außerdem habe ich hier noch das PYTHON 3 Buch welches du gerne nutzten kannst. 

Nutze auch ChatGPT oder Copilot als **Lernbegleiter**. Sei Dir dabei der Gefahr bewusst, dass Du schnell die KI die Aufgaben lösen lässt, ohne selbst etwas dabei zu machen. Daumenregel: Sobald Du die KI bittest, die Aufgabe zu lösen, bist Du (fast) in die Falle getappt. Gib' der KI Kontext, beschreibe Deine Situation, wie beispielsweise:

> "Ich möchte mit Deiner Hilfe Python lernen. Ich habe noch nie programmiert. Ich habe folgende Aufgabe:  [...] und komme nicht weiter. Hier mein Versuch: [...]. Bitte erläutere mir, was ich falsch gemacht habe und helfe mir, mich zu verbessern und dazuzulernen. Bitte gebe mir niemals direkt die Lösung, sondern begleite mich auf dem Weg, die Aufgabe selbst zu lösen.


 
## Aufgabe 1

Schreibe ein Programm in Python, das Wertetabellen für Funktionen aus der Mathematik berechnet und ausgibt.

- Lege als erstes einen neuen Ordern für die Aufgaben an
- Öffene in VS Code diesen Ordner
- Kopiere diese README.md in den root Ordner
- Lege eine neue Datei Aufgabe_1.py an


Das Programm soll die x-Werte in einer Liste wie folgt definieren:


```python
x_i = [
    -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0,
    0.0,  1.0,  2.0,  3.0,  4.0,  5.0,  6.0,  7.0,  8.0,  9.0, 10.0
]
```

Die Mathematischen Funktionen $y = f_j(x)$ sollen in Python-Funktionen der Form

```python
def f_j(x_i: float) -> float:
    # Platzhalter für die Berechnung
    return y_i
```

realisiert werden.

Eine Ausgabe soll ähnlich dieser sein:

```
     x_i    f_1(x_i)
====================
   -10.0       -10.0
    -9.0        -9.0
    -8.0        -8.0
     ...
    10.0        10.0         
```

- a) Implementiere die Funktion $y = f_1(x) = x$ als `f_1`. 
- b) Implementiere die Funktion $y = f_2(x) = 2*x+3$ als `f_2`. 
- c) Implementiere die Funktion $y = f_3(x) = x^2$ als `f_3`. 
- d) Denke Dir noch weitere Funktionen aus. Vielleicht auch ein paar Variationen von a), b), c).


### Deine Lösung - notiere hier deine Ausgabe und was funktioniert oder wo es noch Fragen oder Verbessungen gibt.
```
[-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
1. Funktion Y = x
[-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
2. Funktion Y = 2x +3
[-17.0, -15.0, -13.0, -11.0, -9.0, -7.0, -5.0, -3.0, -1.0, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0]
3. Funktion Y = x^2
[100.0, 81.0, 64.0, 49.0, 36.0, 25.0, 16.0, 9.0, 4.0, 1.0, 0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0, 100.0]
4. Funktion Y = 5x +2^3
[-42.0, -37.0, -32.0, -27.0, -22.0, -17.0, -12.0, -7.0, -2.0, 3.0, 8.0, 13.0, 18.0, 23.0, 28.0, 33.0, 38.0, 43.0, 48.0, 53.0, 58.0]
5. Funktion Y = b*3.14
[0.0, 3.14, 3.14, 6.28, 9.42, 15.7, 25.12, 40.82, 65.94, 106.76, 172.7, 279.46, 452.16]
```
### Meine Notiz

|Debug|-
|---|---|
|F5|Starten|
|F9|Breakpoint|
|F10|durchlaufen|
|F11|In Funktion springen|

|Befehle| -
|---|---|
|Print|Schreiben|
|def|Definieren/unterbefehle|
|append|Listen füllen/anhängen|
|for|for schleife|
|return|sendet Wert zurück|
### Feedback

Jonas, das sieht schon sehr gut aus. Alle Funktionen sind definiert und die Ergebnisse werden geordnet ausgegeben. Prima

## Aufgabe 2

Neben Python gehört heutzutage "git" und "GitHub" zu den wichtigsten Werkzeugen eines Software Entwicklers.

Hier Deine Aufgabe:

- a) Erstelle Dir einen eigenen Account auf https://github.com . Lass' Dir von ChatGPT helfen, einen geeigneten Usernamen zu wählen. Der Username wird Deine Identität auf der weltweiten Plattform "GitHub" sein und ist nicht veränderbar.
- b) Schreibe mir per Teams Deinen Usernamen.

Dann werde ich Dir Schreibzugriff auf dieses Repository geben und auf Dich zukommen, damit wir gemeinsam Deine Lösung von Aufgabe 1 in dieses Repository hinzufügen.

### Deine Lösung:

### Feedback

Du hast erfolgreich ein git clone und ein Commit/ push gemacht. Kannst du die Konsolen Befehle hierzu noch angeben?




## Aufgabe 3

- a) Kopiere die Datei `aufgabe_1.py` und nenne die Kopie `aufgabe_3.py`.
- b) Ändere die Kopie so, dass sie anstelle einer Wertetabelle ein Diagramm erzeugt, welches alle drei Graphen $f_i(x)$ mit $i = {1, 2, 3}$ darstellt.

Nutze dazu das Modul `matplotlib`. Einen Einstieg dazu bekommst Du im [Getting Started](https://matplotlib.org/stable/users/getting_started/) 
Jonas, das sieht schon sehr gut aus. Alle Funktionen sind definiert und die Ergebnisse werden geordnet ausgegeben.

Dazu muss du das Module matplotlib holen. In der Console den befehl

```
pip install matplotlib
```

Dann das Module über ein import einbinden. Siehe Link oben.

```import matplotlib.pyplot as plt```


Bitte mache folgende Erweiterung:

- c) Das Fenster soll ein weiteres Diagramm haben, also insgesamt zwei. Das neue Diagramm soll die Graphen der selben Funktionen zeigen, jedoch als Datenpunkte und nicht als durchgezogene Linien. Weiterhin soll das Diagramm Gitternetzlinien haben, damit man sich besser orientieren kann. Die Achsen sollen durch den Punkt $(0, 0)$ gehen, also das typischen Achsenkreuz, wie wir es aus der Schule kennen. 


### Deine Lösung:



### Feedback


## Aufgabe 4

Installiere eine eigene virtuelle Umgebung (.venv) in deinem Projekt. Dazu wird scoop Verwendet. Ein großer Vorteil davon ist, das dein python mit im Projekt liegt, z.B. derren Version dort festgehalten sind und man sehr schnell diese venv wieder herstellen kann.

Commands:

```
uv sync     
```

## Aufgabe 5

In Aufgabe 3 hast Du Deine Funktionen gezeichnet. Ein Diagramm ist aber erst dann wirklich gut, wenn ein anderer Mensch es verstehen kann, **ohne** dass Du daneben stehst und es erklärst. Genau das machen wir jetzt: aus dem Diagramm wird eine fertige Abbildung, so wie Du sie in einem Physik-Protokoll oder einem Buch finden würdest.

- a) Kopiere die Datei `Aufgabe_3.py` und nenne die Kopie `Aufgabe_5.py`.

Erweitere die Kopie dann Schritt für Schritt:

- b) **Beschriftung:** Gib dem Diagramm eine Überschrift und beschrifte beide Achsen (`x` und `y`).
- c) **Legende:** Zeichne mehrere Funktionen in *ein* Diagramm. Jede Kurve bekommt beim Zeichnen einen Namen, und das Diagramm bekommt eine Legende, damit man die Kurven unterscheiden kann.
- d) **Aussehen:** Gib jeder Kurve eine eigene Farbe und einen eigenen Linienstil (z.B. durchgezogen, gestrichelt, gepunktet) und mache die Linien etwas dicker.
- e) **Ausschnitt:** Lege selbst fest, welcher Bereich der x- und y-Achse zu sehen ist. Probiere aus, was passiert, wenn Du den Bereich der y-Achse auf $-20$ bis $20$ begrenzt, obwohl $f_3(x) = x^2$ bei $x = 10$ schon den Wert $100$ hat.
- f) **Besonderen Punkt markieren:** Suche Dir einen interessanten Punkt aus (z.B. den Schnittpunkt zweier Graphen oder den tiefsten Punkt der Parabel), zeichne dort einen dicken Punkt hin und schreibe mit einem Pfeil einen kurzen Text daneben.
- g) **Speichern:** Speichere das fertige Diagramm als Bilddatei `aufgabe_5.png` in Deinem Projektordner — und zwar aus dem Programm heraus, nicht mit der Maus über den Speichern-Knopf im Fenster.

### Hinweise

Alle neuen Befehle gehören zum `ax`-Objekt, das Du schon aus Aufgabe 3 kennst (`fig, ax = plt.subplots()`). Hier die Stichworte, den Rest findest Du in der Dokumentation:

```python
ax.plot(x, y, label="f_1(x) = x", color="blue", linestyle="--", linewidth=2)
ax.set_title("...")
ax.set_xlabel("...")
ax.set_ylabel("...")
ax.set_xlim(...)
ax.set_ylim(...)
ax.legend()
ax.annotate("...", xy=(0, 0), xytext=(3, 10), arrowprops={"arrowstyle": "->"})

fig.savefig("aufgabe_5.png", dpi=150)
```

Nachschlagen kannst Du das hier:

- [Beschriftungen und Legende](https://matplotlib.org/stable/users/explain/quick_start.html#labelling-plots)
- [Linienstile und Farben](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)
- [Text und Pfeile (annotate)](https://matplotlib.org/stable/users/explain/text/annotations.html)
- [Abbildung speichern](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.savefig)

**Wichtig:** `fig.savefig(...)` muss **vor** `plt.show()` stehen. Überlege Dir, woran das liegen könnte — das ist eine typische Stolperfalle.

**Tipp zur Reihenfolge:** Mache immer nur *eine* Änderung und starte das Programm danach direkt neu (F5). So siehst Du sofort, was der neue Befehl bewirkt, und weißt bei einem Fehler genau, welche Zeile schuld ist.

### Deine Lösung:



### Feedback


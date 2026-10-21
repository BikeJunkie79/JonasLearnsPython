# Jonas Weg zum Python-Entwickler

Diese Aufgabensammlung werden wir stetig erweitern. Die Aufgaben werden immer schwieriger und Du wirst immer mehr von der Programmiersprache Python lernen.

Die ersten Aufgaben werden noch nichts mit dem Ganzkörper-Scanner "BodyLoop" zu tun haben. Spätere Aufgaben, vielleicht schon welche am Ende Deiner ersten von zwei Wochen, werden mit dem BodyLoop zu tun haben.

Du wirst Daten von Deinen eigenen Scans nutzen und einige (kleine) Funktionalitäten, die Du im BodyLoop findest, selbst entwickeln.


## Zwischen den Aufgaben

Wie bereits besprochen, nutze https://checkio.org/ , um im Selbststudium Dich die Programmiersprache **Python** zu erlernen.

Nutze auch ChatGPT oder Copilot als **Lernbegleiter**. Sei Dir dabei der Gefahr bewusst, dass Du schnell die KI die Aufgaben lösen lässt, ohne selbst etwas dabei zu machen. Daumenregel: Sobald Du die KI bittest, die Aufgabe zu lösen, bist Du (fast) in die Falle getappt. Gib' der KI Kontext, beschreibe Deine Situation, wie beispielsweise:

> "Ich möchte mit Deiner Hilfe Python lernen. Ich habe noch nie programmiert. Ich habe folgende Aufgabe:  [...] und komme nicht weiter. Hier mein Versuch: [...]. Bitte erläutere mir, was ich falsch gemacht habe und helfe mir, mich zu verbessern und dazuzulernen. Bitte gebe mir niemals direkt die Lösung, sondern begleite mich auf dem Weg, die Aufgabe selbst zu lösen.



## Aufgabe 1

Schreibe ein Programm in Python, das Wertetabellen für Funktionen aus der Mathematik berechnet und ausgibt.

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

### Feedback

## Aufgabe 2

Neben Python gehört heutzutage "git" und "GitHub" zu den wichtigsten Werkzeugen eines Software Entwicklers.

Hier Deine Aufgabe:

- a) Erstelle Dir einen eigenen Account auf https://github.com . Lass' Dir von ChatGPT helfen, einen geeigneten Usernamen zu wählen. Der Username wird Deine Identität auf der weltweiten Plattform "GitHub" sein und ist nicht veränderbar.
- b) Schreibe mir per Teams Deinen Usernamen.

Dann werde ich Dir Schreibzugriff auf dieses Repository geben und auf Dich zukommen, damit wir gemeinsam Deine Lösung von Aufgabe 1 in dieses Repository hinzufügen.

### Deine Lösung:

### Feedback

## Aufgabe 3

- a) Kopiere die Datei `aufgabe_1.py` und nenne die Kopie `aufgabe_3.py`.
- b) Ändere die Kopie so, dass sie anstelle einer Wertetabelle ein Diagramm erzeugt, welches alle drei Graphen $f_i(x)$ mit $i = {1, 2, 3}$ darstellt.

Nutze dazu das Modul `matplotlib`. Einen Einstieg dazu bekommst Du im [Getting Started](https://matplotlib.org/stable/users/getting_started/).


### Feedback

Klasse! Sieht sehr gut aus!

Bitte mache folgende Erweiterung:

- c) Das Fenster soll ein weiteres Diagramm haben, also insgesamt zwei. Das neue Diagramm soll die Graphen der selben Funktionen zeigen, jedoch als Datenpunkte und nicht als durchgezogene Linien. Weiterhin soll das Diagramm Gitternetzlinien haben, damit man sich besser orientieren kann. Die Achsen sollen durch den Punkt $(0, 0)$ gehen, also das typischen Achsenkreuz, wie wir es aus der Schule kennen. 

## Aufgabe 4

JSON (JavaScript Object Notation) ist ein weit verbreitetes Datenformat zum Austausch von strukturierten Daten. In dieser Aufgabe lernst Du, wie man in Python mit JSON-Daten arbeitet.

Diese Aufgabe bereitet Dich darauf vor, ab übermorgen oder sogar schon morgen mit aus dem [BodyLoop](https://www.vitronic.com/de-de/3d-bodyscan/scanner-leistungsdiagnostik) exportierten Daten von Deinem eigenen Körper-Vermessungs-Scan zu arbeiten.

- a) Erstelle eine Datei `aufgabe_4.py`. Schreibe ein Programm, das ein einfaches Python-Dictionary erstellt und es als JSON-String ausgibt. Das Dictionary soll folgende Daten enthalten:
  ```python
  person = {
      "name": "Max Mustermann",
      "alter_jahre": 25,
      "stadt": "Berlin"
  }
  ```
  Nutze `json.dumps()` um das Dictionary in einen JSON-String zu konvertieren und gib ihn aus. Dafür wirst Du im Kopf der Datei den Ausdruck `import json` verwenden müssen, damit die Funktionalitäten in Deinem Programm verfügbar sind.

  Erzeuge einen Commit mit der Message `Solve assignment 4.a`, damit Du diesen Entwicklungsstand gesichert hast, bevor Du weiter machst und den Code damit durch Hinzufügen, Abändern, Löschen, also allgemeiner gesprochen modifizieren/ändern wirst.

- b) Erweitere das Programm so, dass es den JSON-String aus a) wieder zurück in ein Python-Dictionary konvertiert. Nutze dazu `json.loads()`. Gib sowohl das ursprüngliche Dictionary als auch das aus JSON zurück konvertierte Dictionary aus und überprüfe, ob sie identisch sind.

  Erzeuge wieder einen Commit mit Deiner Lösung für diesen Schritt.

- c) Erstelle eine JSON-Datei `personen.json` mit einer Liste von mehreren Personen. Jede Person soll mindestens die Felder "name", "alter_jahre", "stadt" und "beruf" haben. Schreibe dann Code, der diese JSON-Datei einliest (mit `json.load()`) und alle Personen ausgibt. Beispiel-Struktur:
  ```json
  {
      "personen": [
          {
              "name": "Anna Schmidt",
              "alter_jahre": 28,
              "stadt": "München",
              "beruf": "Ingenieurin"
          },
          {
              "name": "Tom Weber",
              "alter_jahre": 34,
              "stadt": "Hamburg",
              "beruf": "Lehrer"
          }
      ]
  }
  ```

  Commit nicht vergessen!

- d) Erweitere das Programm um eine Funktion, die neue Personen zur JSON-Datei hinzufügt. Die Funktion soll die bestehende Datei einlesen, eine neue Person hinzufügen und die aktualisierte Liste wieder in die Datei schreiben. Teste die Funktion, indem Du eine neue Person hinzufügst.

  Commit nicht vergessen!

- e) Erweitere die JSON-Struktur um die Felder "groesse_m" (in Metern) und "gewicht_kg" (in Kilogramm) für jede Person, gruppiert in einem "koerper" Objekt. Aktualisiere die `personen.json` Datei entsprechend:
  ```json
  {
      "personen": [
          {
              "name": "Anna Schmidt",
              "alter_jahre": 28,
              "stadt": "München",
              "beruf": "Ingenieurin",
              "koerper": {
                  "groesse_m": 1.68,
                  "gewicht_kg": 65.5
              }
          },
          {
              "name": "Tom Weber",
              "alter_jahre": 34,
              "stadt": "Hamburg",
              "beruf": "Lehrer",
              "koerper": {
                  "groesse_m": 1.82,
                  "gewicht_kg": 78.2
              }
          }
      ]
  }
  ```
  
  Implementiere eine Python Funktion `def bmi(name: str) -> float`, die nach einem gegebenen Namen sucht und, falls dieser gefunden wird, den [Body Mass Index (BMI)](https://en.wikipedia.org/wiki/Body_mass_index) berechnet und zurückgibt. Falls der Name nicht gefunden wird, soll `0` zurückgegeben werden.

  Mache die BMI-Funktionalität dem Anwender in einer Art und Weise Deiner Wahl zugänglich.

  Commit nicht vergessen!

- f) Könnte man den Eintrag `alter_jahre` durch eine geeignetere Angabe ersetzen? Überlege. Mit welcher? Begründe Deine Aussage. Verbessere Dein Programm bzw. Deine Daten auf Basis Deiner Überlegung.

  Und einen Commit ...

- g) Ändere die JSON-Struktur so, dass der Eintrag `gewicht_kg` anstelle eines einzelnen Wertes eine Liste mit einem Eintrag wird. Dies bereitet eine spätere Erweiterung vor, bei der mehrere Gewichtsmessungen zu verschiedenen Zeitpunkten gespeichert werden können.
  
  Beispiel:
  ```json
  "koerper": {
      "groesse_m": 1.68,
      "gewicht_kg": [65.5]
  }
  ```
  
  Passe Deine BMI-Funktion entsprechend an, damit sie weiterhin funktioniert. 

  Commit nicht vergessen! 

- h) Erweitere die `gewicht_kg` Listen um mehrere Einträge, um verschiedene Gewichtsmessungen zu verschiedenen Zeitpunkten zu simulieren. Verschiedene Personen sollen unterschiedlich viele Messungen haben.
  
  Beispiel-Struktur:
  ```json
  {
      "personen": [
          {
              "name": "Anna",
              "alter_jahre": 28,
              "stadt": "München",
              "beruf": "Ingenieurin",
              "koerper": {
                  "groesse_m": 1.68,
                  "gewicht_kg": [65.5, 64.8, 65.2]
              }
          },
          {
              "name": "Tom",
              "alter_jahre": 34,
              "stadt": "Hamburg",
              "beruf": "Lehrer",
              "koerper": {
                  "groesse_m": 1.82,
                  "gewicht_kg": [78.2, 77.9, 78.5, 78.0, 77.7]
              }
          },
          {
              "name": "Armin",
              "alter_jahre": 18,
              "stadt": "Mainz",
              "beruf": "Student",
              "koerper": {
                  "groesse_m": 1.65,
                  "gewicht_kg": [58.3, 58.8]
              }
          }
      ]
  }
  ```
  



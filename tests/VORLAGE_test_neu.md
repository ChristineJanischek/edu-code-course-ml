# [TITEL] - Version [X] (KI/ML und Python)

<!--
Vorlage fuer neue Tests und Musterloesungen

Best Practice fuer Word-Kopie:
- Tabellen immer als HTML-Tabelle im unten stehenden Standard verwenden.
- Fliesstext und Aufgaben normal in Markdown schreiben.
- Code als fenced code block (```python ... ```), ohne zusaetzliche Wrapper.
- Keine verschachtelten <div>-Container verwenden.

Nach dem Erstellen optional normalisieren:
  python3 scripts/format_tests.py tests/pfad/zur/datei.md
-->

- Bereich: [BEREICH]
- Gesamtpunkte: 25
- Gewichtung: Theorie 17,5 Punkte (70%), Praxis 7,5 Punkte (30%)
- Bearbeitungszeit (Vorschlag): 45-60 Minuten
- Hilfsmittel: Stift, Papier, optional Syntaxhilfe unten

## Hinweise zur Bearbeitung

- Der Test ist so aufgebaut, dass er komplett handschriftlich bearbeitet werden kann.
- Bei Programmieraufgaben zaehlt der korrekte Ablauf. Kleine Syntaxfehler sind weniger wichtig als die richtige Logik.
- Antworte klar und in ganzen Saetzen, wenn es gefordert ist.

## Teil A: Theorie ([X] Punkte)

### Aufgabe A1: [Titel] ([X] Punkte)

[Aufgabentext ...]

<table style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; font-size: 11pt;">
  <thead>
    <tr>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Begriff</th>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Kurzdefinition</th>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Beispiel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; vertical-align: top;">[Begriff 1]</td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; vertical-align: top;"></td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; vertical-align: top;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; vertical-align: top;">[Begriff 2]</td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; vertical-align: top;"></td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; vertical-align: top;"></td>
    </tr>
  </tbody>
</table>

Bewertung:
- pro Zeile: 1 Punkt Definition + 1 Punkt Beispiel

### Aufgabe A2: [Titel] ([X] Punkte)

[Aufgabentext ...]

Antwort:



### Aufgabe A3: [Titel] ([X] Punkte)

[Aufgabentext ...]

Antwort:



## Teil B: Praxis (Programmierung, [X] Punkte)

### Aufgabe B1: [Titel] ([X] Punkte)

Schreibe den Code handschriftlich oder in sauberem Pseudocode.

Szenario:
- Dateiname: ../daten/[datei].csv
- Spalten: [spalte1], [spalte2], [ziel]

1. Lade die CSV-Datei mit Pandas und gib die ersten 5 Zeilen aus. (2 Punkte)
2. Berechne Durchschnitt, Minimum und Maximum von [Zielgroesse]. (2,5 Punkte)
3. Teile die Daten 80/20, trainiere ein lineares Regressionsmodell und gib MSE und R2 aus. (3 Punkte)

Antwort:

```python
# loesung hier
```

## Syntaxhilfe (optional)

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Daten laden
df = pd.read_csv("../daten/[datei].csv")
print(df.head())

# Kennzahlen
mean_ziel = df["[ziel]"].mean()
min_ziel = df["[ziel]"].min()
max_ziel = df["[ziel]"].max()

# Features / Ziel
X = df[["[spalte1]", "[spalte2]"]]
y = df["[ziel]"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modell
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Bewertung
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse:.2f}  R2: {r2:.4f}")
```

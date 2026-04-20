# Grundlagen-Test (KI/ML und Python)

- Bereich: Grundlagen
- Gesamtpunkte: 25
- Gewichtung: Theorie 17,5 Punkte (70%), Praxis 7,5 Punkte (30%)
- Bearbeitungszeit (Vorschlag): 45-60 Minuten
- Hilfsmittel: Stift, Papier, optional Syntaxhilfe unten

## Hinweise zur Bearbeitung

- Der Test ist so aufgebaut, dass er komplett handschriftlich bearbeitet werden kann.
- Bei Programmieraufgaben zaehlt der korrekte Ablauf. Kleine Syntaxfehler sind weniger wichtig als die richtige Logik.
- Antworte klar und in ganzen Saetzen, wenn es gefordert ist.

## Teil A: Theorie (17,5 Punkte)

### Aufgabe A1: Begriffe sicher unterscheiden (6 Punkte)

Ergaenze die Tabelle mit einer kurzen Definition und einem passenden Beispiel.

| Begriff | Kurzdefinition | Beispiel aus Alltag oder Wirtschaft |
|---|---|---|
| KI |  |  |
| Machine Learning |  |  |
| Deep Learning |  |  |

Bewertung:
- pro Begriff: 1 Punkt Definition + 1 Punkt Beispiel

### Aufgabe A2: Regelbasiert vs. datenbasiert (3 Punkte)

1. Erklaere den Unterschied zwischen regelbasierter und datenbasierter Loesung in 2-4 Saetzen. (2 Punkte)
2. Nenne ein konkretes Beispiel fuer beide Ansaetze. (1 Punkt)

Antwort:



### Aufgabe A3: Training, Test, labeled, unlabeled (5,5 Punkte)

1. Warum muessen Trainingsdaten und Testdaten getrennt sein? (2 Punkte)
2. Erklaere labeled Data und unlabeled Data jeweils mit einem Beispiel aus dem Hauspreis-Kontext. (2 Punkte)
3. Darf ein Modell Testdaten beim Lernen sehen? Begruende kurz. (1,5 Punkte)

Antwort:



### Aufgabe A4: Datenmenge und Datenqualitaet bewerten (3 Punkte)

Ein Team trainiert dasselbe Regressionsmodell zweimal:
- Lauf 1: 20 Datensaetze
- Lauf 2: vollstaendiger Datensatz

Bewerte in 4-6 Saetzen, wie sich Datenmenge und Datenqualitaet auf MSE und R2 auswirken koennen. (3 Punkte)

Antwort:



## Teil B: Praxis (Programmierung, 7,5 Punkte)

### Aufgabe B1: Python/Pandas-Grundablauf (7,5 Punkte)

Schreibe den Code handschriftlich oder in sauberem Pseudocode. Nutze folgende Annahme:
- Dateiname: ../notebooks/daten/haeuser.csv
- wichtige Spalten: groesse_m2, zimmer, baujahr, preis_euro

1. Lade die CSV-Datei mit Pandas und gib die ersten 5 Zeilen aus. (2 Punkte)
2. Berechne den durchschnittlichen, minimalen und maximalen Hauspreis. (2,5 Punkte)
3. Teile die Daten in Training/Test (80/20), trainiere eine lineare Regression und gib MSE und R2 aus. (3 Punkte)

Antwort:

```python



```

## Syntaxhilfe (optional)

Diese Hilfe darf bei handschriftlicher Loesung als Orientierung genutzt werden.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Daten laden
df = pd.read_csv("../notebooks/daten/haeuser.csv")
print(df.head())

# Kennzahlen
mean_preis = df["preis_euro"].mean()
min_preis = df["preis_euro"].min()
max_preis = df["preis_euro"].max()

# Features/Ziel
X = df[["groesse_m2", "zimmer", "baujahr"]]
y = df["preis_euro"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modell
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Bewertung
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

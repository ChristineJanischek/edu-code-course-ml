# Grundlagen-Test – Version B (KI/ML und Python)

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

### Aufgabe A1: Begriffe und ihre Anwendung (6 Punkte)

Ordne folgende Begriffe den Beschreibungen zu und nenne jeweils ein Beispiel:

| Konzept | Kurze Erklaerung | Beispiel aus Alltag oder Industrie |
|---|---|---|
| Kuenstliche Intelligenz |  |  |
| Machine Learning |  |  |
| Neuronale Netze |  |  |

Bewertung:
- pro Zeile: 1 Punkt Erklaerung + 1 Punkt passendes Beispiel

### Aufgabe A2: Fest programmiert vs. lernend (3 Punkte)

1. Erklaere in 2-4 Saetzen, worin sich fest programmierte Systeme von lernenden Systemen unterscheiden. (2 Punkte)
2. Gib zwei konkrete Alltagsbeispiele: eines, das fest programmiert ist, eins, das lernt. (1 Punkt)

Antwort:



### Aufgabe A3: Trainings- und Testphase in ML (5,5 Punkte)

Arbeite mit dem Kontext: Ein Unternehmen moechte die Restwertpreise von Autos vorhersagen (Alter, KM-Stand, PS).

1. Warum ist eine Aufteilung in Trainings- und Testdaten sinnvoll? (2 Punkte)
2. Erklaere, was labeled Data und unlabeled Data in diesem Kontext bedeuten (mit jeweils einem Beispiel). (2 Punkte)
3. Was waere die Folge, wenn Testdaten beim Training \"mitlernen\" duerfen? (1,5 Punkte)

Antwort:



### Aufgabe A4: Einfluss von Datenmenge und Datenbestand (3 Punkte)

Ein Team testet ein Regressionsmodell zweimal:
- Experiment 1: 25 Auto-Datensaetze
- Experiment 2: 500 Auto-Datensaetze

Begruende in 4-6 Saetzen, welche Auswirkungen Datenmenge und Datenqualitaet (z. B. fehlerhafte KM-Angaben) auf Die Vorhersageguete haben koennen. (3 Punkte)

Antwort:



## Teil B: Praxis (Programmierung, 7,5 Punkte)

### Aufgabe B1: Datenverarbeitung mit Python/Pandas (7,5 Punkte)

Schreibe den Code handschriftlich oder in sauberem Pseudocode.

Szenario:
- Dateiname: ../daten/auto_preise.csv
- Spalten: alter_jahre, km_stand, ps, preis_euro

1. Lade die CSV-Datei mit Pandas, gib die ersten 5 Zeilen aus. (2 Punkte)
2. Berechne Durchschnitt, Minimum und Maximum des Preises. (2,5 Punkte)
3. Teile die Daten 80/20 auf, trainiere ein lineares Regressionsmodell und gib MSE sowie R2 aus. (3 Punkte)

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
df = pd.read_csv("../daten/auto_preise.csv")
print(df.head())

# Kennzahlen
mean_price = df["preis_euro"].mean()
min_price = df["preis_euro"].min()
max_price = df["preis_euro"].max()

# Features/Ziel
X = df[["alter_jahre", "km_stand", "ps"]]
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

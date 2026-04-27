# Grundlagen-Test – Version D (KI/ML und Python)

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

### Aufgabe A1: Konzepte rund um KI (6 Punkte)

Erklaere folgende Begriffe und gib zu jedem ein Beispiel:

| Begriff | Erklaerung | Beispiel |
|---|---|---|
| KI |  |  |
| Maschinenelles Lernen |  |  |
| Tiefe Netze |  |  |

Bewertung:
- pro Zeile: 1 Punkt Erklaerung + 1 Punkt Beispiel

### Aufgabe A2: Hart kodiert vs. adaptiv (3 Punkte)

1. Unterscheide in 2-4 Saetzen: Was ist der Unterschied zwischen starr programmierten Systemen und Systemen, die lernen? (2 Punkte)
2. Nenne zur Unterscheidung jeweils ein Beispiel. (1 Punkt)

Antwort:



### Aufgabe A3: Daten in Training und Pruefung (5,5 Punkte)

Szenario: Ein Unternehmen moechte Studierenden-Noten basierend auf Lernstunden, Anwesenheit und bearbeiteten Uebungen vorhersagen.

1. Begruende, warum eine Aufteilung der Daten in Training und Test notwendig ist. (2 Punkte)
2. Was sind labeled vs. unlabeled Data in diesem Kontext? Gib je ein Beispiel. (2 Punkte)
3. Welche Fehlerquellen entstehen, wenn Test-Beispiele (Noten) waehrend des Trainings benutzt werden? (1,5 Punkte)

Antwort:



### Aufgabe A4: Menge und Qualitaet von Daten (3 Punkte)

Ein Lehrerteam teste ein Noten-Vorhersage-Modell zweimal:
- Szenario A: 30 Studierenden-Datensaetze
- Szenario B: 300 Studierenden-Datensaetze

Analysiere in 5-7 Saetzen, wie Datenmenge und Datenqualitaet (z. B. fehlerhafte Anwesenheitsangaben) die Modellguete bezueglich MSE und R2 veraendern. (3 Punkte)

Antwort:



## Teil B: Praxis (Programmierung, 7,5 Punkte)

### Aufgabe B1: Datenverarbeitung und Modelltraining (7,5 Punkte)

Schreibe den Code handschriftlich oder in sauberem Pseudocode.

Szenario:
- Dateiname: ../daten/studierende_noten.csv
- Spalten: lern_stunden, anwesenheit_prozent, uebungen_bearbeitet, note

1. Lade die CSV-Datei mit Pandas und zeige die ersten 5 Zeilen. (2 Punkte)
2. Berechne Durchschnitt, Minimum und Maximum der Noten. (2,5 Punkte)
3. Teile Daten 80/20, trainiere ein lineares Regressionsmodell und gib MSE und R2 aus. (3 Punkte)

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
df = pd.read_csv("../daten/studierende_noten.csv")
print(df.head())

# Kennzahlen Noten
mean_note = df["note"].mean()
min_note = df["note"].min()
max_note = df["note"].max()

# Features und Ziel
X = df[["lern_stunden", "anwesenheit_prozent", "uebungen_bearbeitet"]]
y = df["note"]

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

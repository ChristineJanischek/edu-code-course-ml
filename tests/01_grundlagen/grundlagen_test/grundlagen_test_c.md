# Grundlagen-Test – Version C (KI/ML und Python)

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

### Aufgabe A1: KI-Paradigmen unterscheiden (6 Punkte)

Vergleiche folgende Konzepte in einer Tabelle:

| Konzept | Definition | Anwendungsbeispiel |
|---|---|---|
| Intelligente Systeme |  |  |
| Lernende Modelle |  |  |
| Tiefes Lernen |  |  |

Bewertung:
- pro Zeile: 1 Punkt korrekte Definition + 1 Punkt relevantes Beispiel

### Aufgabe A2: Algorithmen und Daten (3 Punkte)

1. Erklaere in 3-5 Saetzen den Unterschied zwischen einem regelgesteuerten System und einem datengetriebenen Modell. (2 Punkte)
2. Gib fuer jede Methode ein Beispiel aus dem Bereich Wetter/Klima. (1 Punkt)

Antwort:



### Aufgabe A3: Daten teilen und labeln (5,5 Punkte)

Kontext: Ein Wetter-Modell soll Tageshöchsttemperaturen vorhersagen (Min-Temp, Luftfeuchtigkeit, Luftdruck gehören zu den Inputs).

1. Erklaere, warum man Daten in Train- und Testsets teilt. (2 Punkte)
2. Definiere labeled und unlabeled Data mit Beispielen aus dem Wetter-Kontext. (2 Punkte)
3. Welche Probleme entstehen, wenn Testdaten beim Training verwendet werden? (1,5 Punkte)

Antwort:



### Aufgabe A4: Datenumfang und Qualitaetsaspekte (3 Punkte)

Ein Forscherteam trainiert ein Wetter-Vorhersage-Modell in zwei Varianten:
- Version 1: 50 Messwerte ueber einen Monat
- Version 2: 1000 Messwerte ueber ein Jahr

Begruende in 5-7 Saetzen, wie Datenmenge (temporal/volumenmaessig) und Messfehler (z. B. fehlerhafte Sensoren) die Modellguete (MSE, R2) beeinflussen. (3 Punkte)

Antwort:



## Teil B: Praxis (Programmierung, 7,5 Punkte)

### Aufgabe B1: Datenanalyse mit Python und Pandas (7,5 Punkte)

Schreibe den Code handschriftlich oder in sauberem Pseudocode.

Szenario:
- Dateiname: ../daten/wetter_daten.csv
- Spalten: min_temp_celsius, luftfeuchtigkeit_prozent, luftdruck_mbar, max_temp_celsius

1. Lade die CSV-Datei mit Pandas und zeige die ersten 5 Zeilen. (2 Punkte)
2. Berechne Mittelwert, Minimale und Maximale Tageshoechsttemperatur. (2,5 Punkte)
3. Teile Daten im Verhaeltnis 80/20, trainiere ein Regressionsmodell und gib MSE und R2 aus. (3 Punkte)

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
df = pd.read_csv("../daten/wetter_daten.csv")
print(df.head())

# Kennzahlen Max-Temp
mean_temp = df["max_temp_celsius"].mean()
min_temp = df["max_temp_celsius"].min()
max_temp = df["max_temp_celsius"].max()

# Features und Zielwert
X = df[["min_temp_celsius", "luftfeuchtigkeit_prozent", "luftdruck_mbar"]]
y = df["max_temp_celsius"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelltraining
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluierung
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

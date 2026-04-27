# Musterloesung: Grundlagen-Test – Version C (KI/ML und Python)

- Gesamtpunkte: 25
- Theorie: 17,5 Punkte
- Praxis: 7,5 Punkte

## Teil A: Theorie (17,5 Punkte)

### Aufgabe A1: KI-Paradigmen unterscheiden (6 Punkte)

Aufgabenstellung:

Vergleiche folgende Konzepte in einer Tabelle:

| Konzept | Definition | Anwendungsbeispiel |
|---|---|---|
| Intelligente Systeme |  |  |
| Lernende Modelle |  |  |
| Tiefes Lernen |  |  |

Musterloesung:

| Konzept | Definition | Anwendungsbeispiel |
|---|---|---|
| Intelligente Systeme | Systeme, die Probleme loesen, Entscheidungen treffen oder lernen koennen. | Navigationssystem findet die schnellste Route. |
| Lernende Modelle | Algorithmen, die Muster aus Trainingsdaten erfassen und damit Vorhersagen machen. | Vorhersage von Boersenkursen basierend auf historischen Daten. |
| Tiefes Lernen | Machine-Learning-Methode mit vielen verschachtelten Schichten, aehnlich neuronalen Netzen. | Erkennung von Objekten in Bildern oder Gesichtserkennung. |

Punktevergabe:
- Pro Zeile 2 Punkte: 1 Punkt Definition, 1 Punkt Beispiel.

### Aufgabe A2: Algorithmen und Daten (3 Punkte)

Aufgabenstellung:

1. Erklaere in 3-5 Saetzen den Unterschied zwischen einem regelgesteuerten System und einem datengetriebenen Modell. (2 Punkte)
2. Gib fuer jede Methode ein Beispiel aus dem Bereich Wetter/Klima. (1 Punkt)

Musterloesung:

1. Regelgesteuerte Systeme basieren auf vordefinierten Wenn-Dann-Regeln, die Programmierer schreiben. Sie sind staerr und veraendern sich nicht. Datengetriebene Modelle beobachten Muster in Daten und passen sich an. Sie koennen neue Situations erkennern, die urspruenglich nicht geprogrammiert waren.

2. Regelgesteuert: "Wenn Temperatur unter 0°C, dann Frostwarnung ausgeben." Datengetrieben: Ein Modell lernt aus 10 Jahren Wetterdaten, wann eine Sturmoende wahrscheinlich ist.

Punktevergabe:
- 2 Punkte: Unterschied klar erklaert (Regeln vs. Muster/Lernen).
- 1 Punkt: Mindestens ein relevantes Wetter-Beispiel fuer beide Kategorien.

### Aufgabe A3: Daten teilen und labeln (5,5 Punkte)

Aufgabenstellung:

Kontext: Ein Wetter-Modell soll Tageshöchsttemperaturen vorhersagen (Min-Temp, Luftfeuchtigkeit, Luftdruck gehören zu den Inputs).

1. Erklaere, warum man Daten in Train- und Testsets teilt. (2 Punkte)
2. Definiere labeled und unlabeled Data mit Beispielen aus dem Wetter-Kontext. (2 Punkte)
3. Welche Probleme entstehen, wenn Testdaten beim Training verwendet werden? (1,5 Punkte)

Musterloesung:

1. Die Aufteilung prüft, ob das Modell generalisieren kann. Trainingsdaten lehren das Modell, Testdaten prüfen, wie gut es auf neuen Wetterdaten funktioniert, die es noch nicht gesehen hat. Ohne Trennung weiss man nicht, ob das Modell wirklich vorhersagen kann oder nur die Trainingsfaelle auswendig lernt.

2. labeled Data: Wettermessungen mit bekanntem Ergebnis – z. B. (Min-Temp=5°C, Feuchte=70%, Druck=1013) → Max-Temp=18°C. unlabeled Data: Aktuelle Messwerte (5°C, 70%, 1013), ohne dass wir die Max-Temp schon kennen – das Modell soll diese vorhersagen.

3. Information Leakage: Das Modell "kennt" bereits die richtige Antwort bei Testdaten. Die Evaluierung waere zu positiv (MSE zu niedrig, R2 zu hoch), und man erkennt nicht die echte Vorhersageguete. Neue, echte Wetterdaten wuerden dann enttaeuschend sein.

Punktevergabe:
- 2 Punkte: Gute Erklaerung fuer die Aufteilung (Generaliserung testen).
- 2 Punkte: klare Definition + Beispiel labeled/unlabeled Daten im Wetter-Kontext.
- 1,5 Punkte: Klare Erklaerung der Folge (falsch positive Metriken, Data Leakage).

### Aufgabe A4: Datenumfang und Qualitaetsaspekte (3 Punkte)

Aufgabenstellung:

Ein Forscherteam trainiert ein Wetter-Vorhersage-Modell in zwei Varianten:
- Version 1: 50 Messwerte ueber einen Monat
- Version 2: 1000 Messwerte ueber ein Jahr

Begruende in 5-7 Saetzen, wie Datenmenge (temporal/volumenmaessig) und Messfehler (z. B. fehlerhafte Sensoren) die Modellguete (MSE, R2) beeinflussen. (3 Punkte)

Musterloesung:

- 50 Messwerte ueber einen Monat erfassen nur ein Zeitfenster, nicht saisonale Muster. Das Modell verallgemeinert schlecht.
- 1000 Messwerte ueber ein Jahr zergeben Variation durch Jahreszeiten und zeigen echte Muster. Das Modell kann besser generalisieren, MSE sinkt, R2 steigt.
- Defekte Sensoren erzeugen fehlerhafte Min-Temps oder Feuchteangaben. Diese Fehler verzerren das Training, erhoehen MSE undkoennen R2 verringern, auch wenn viel Daten vorhanden ist.
- Eine grosse, aber schmutzige Datenmenge ist weniger wertvoll als kleinere, saubere Daten.

Punktevergabe:
- 1 Punkt: Temporale/volumenmaessige Aspekte der Menge erkannt.
- 1 Punkt: Einfluss fehlerhafter Sensoren auf Guete erklaert.
- 1 Punkt: Bezug zu MSE/R2 und praktische Schlussfolgerung.

## Teil B: Praxis (7,5 Punkte)

### Aufgabe B1: Datenanalyse mit Python und Pandas (7,5 Punkte)

Aufgabenstellung:

Schreibe den Code handschriftlich oder in sauberem Pseudocode.

Szenario:
- Dateiname: ../daten/wetter_daten.csv
- Spalten: min_temp_celsius, luftfeuchtigkeit_prozent, luftdruck_mbar, max_temp_celsius

1. Lade die CSV-Datei mit Pandas und zeige die ersten 5 Zeilen. (2 Punkte)
2. Berechne Mittelwert, Minimale und Maximale Tageshoechsttemperatur. (2,5 Punkte)
3. Teile Daten im Verhaeltnis 80/20, trainiere ein Regressionsmodell und gib MSE und R2 aus. (3 Punkte)

Musterloesung:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1) Daten laden
df = pd.read_csv("../daten/wetter_daten.csv")
print(df.head())

# 2) Statistiken Max-Temp
mean_max = df["max_temp_celsius"].mean()
min_max = df["max_temp_celsius"].min()
max_max = df["max_temp_celsius"].max()
print("Mittelwert:", mean_max)
print("Minimum:", min_max)
print("Maximum:", max_max)

# 3) Train-Test Split und Modell
X = df[["min_temp_celsius", "luftfeuchtigkeit_prozent", "luftdruck_mbar"]]
y = df["max_temp_celsius"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MSE:", mse)
print("R2:", r2)
```

Punktevergabe:
- 2 Punkte: CSV korrekt geladen, head() ausgegeben.
- 2,5 Punkte: mean(), min(), max() korrekt auf max_temp_celsius angewendet.
- 3 Punkte: 80/20 Split, LinearRegression trainiert, MSE und R2 berechnet/ausgegeben.

## Korrekturhinweis fuer handschriftliche Loesungen

- Fachlogik geht vor Syntaxperfektion.
- Spalten-Schreibvarianten (z. B. "max_temp" statt "max_temp_celsius") akzeptabel, wenn Absicht klar.
- Pseudocode oder halbformales Textformat wird vollstaendig anerkannt, wenn alle Schritte vorhanden.

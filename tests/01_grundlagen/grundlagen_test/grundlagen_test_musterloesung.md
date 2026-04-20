# Musterloesung: Grundlagen-Test (KI/ML und Python)

- Gesamtpunkte: 25
- Theorie: 17,5 Punkte
- Praxis: 7,5 Punkte

## Teil A: Theorie (17,5 Punkte)

### Aufgabe A1: Begriffe sicher unterscheiden (6 Punkte)

Aufgabenstellung:

Ergaenze die Tabelle mit einer kurzen Definition und einem passenden Beispiel.

| Begriff | Kurzdefinition | Beispiel aus Alltag oder Wirtschaft |
|---|---|---|
| KI |  |  |
| Machine Learning |  |  |
| Deep Learning |  |  |

Musterloesung:

| Begriff | Kurzdefinition | Beispiel aus Alltag oder Wirtschaft |
|---|---|---|
| KI | Oberbegriff fuer Systeme, die Aufgaben mit intelligentem Verhalten loesen. | Chatbot im Kundenservice beantwortet Standardanfragen. |
| Machine Learning | Teilgebiet der KI: Modelle lernen Muster aus Daten statt nur fester Regeln. | Spamfilter lernt aus markierten E-Mails. |
| Deep Learning | Teilgebiet von ML mit mehrschichtigen neuronalen Netzen. | Bilderkennung in einer Qualitaetskontrolle. |

Punktevergabe:
- Pro Zeile 2 Punkte: 1 Punkt Definition, 1 Punkt passendes Beispiel.

### Aufgabe A2: Regelbasiert vs. datenbasiert (3 Punkte)

Aufgabenstellung:

1. Erklaere den Unterschied zwischen regelbasierter und datenbasierter Loesung in 2-4 Saetzen. (2 Punkte)
2. Nenne ein konkretes Beispiel fuer beide Ansaetze. (1 Punkt)

Musterloesung:

- Regelbasiert bedeutet: Entscheidungen erfolgen ueber feste Wenn-Dann-Regeln, die von Menschen vorgegeben werden.
- Datenbasiert bedeutet: Ein Modell lernt Zusammenhaenge aus Beispieldaten und trifft darauf basierend Vorhersagen.
- Beispiel regelbasiert: Wenn Rechnungsbetrag > 1000 Euro, dann zweite Freigabe noetig.
- Beispiel datenbasiert: Modell schaetzt Hauspreise aus Wohnflaeche, Zimmern und Baujahr.

Punktevergabe:
- 2 Punkte fuer korrekte Erklaerung (beide Ansaetze klar abgegrenzt).
- 1 Punkt fuer mindestens ein korrektes Beispiel je Ansatz (oder ein sehr gutes Vergleichsbeispiel).

### Aufgabe A3: Training, Test, labeled, unlabeled (5,5 Punkte)

Aufgabenstellung:

1. Warum muessen Trainingsdaten und Testdaten getrennt sein? (2 Punkte)
2. Erklaere labeled Data und unlabeled Data jeweils mit einem Beispiel aus dem Hauspreis-Kontext. (2 Punkte)
3. Darf ein Modell Testdaten beim Lernen sehen? Begruende kurz. (1,5 Punkte)

Musterloesung:

1. Training und Test muessen getrennt sein, damit fair geprueft wird, ob das Modell auf unbekannten Daten funktioniert. Sonst waere das Ergebnis zu optimistisch.
2. labeled Data im Hauskontext: Eingaben (groesse_m2, zimmer, baujahr) plus Zielwert preis_euro. unlabeled Data: gleiche Eingaben, aber ohne preis_euro.
3. Testdaten duerfen nicht beim Lernen verwendet werden, weil sonst Informationsleck (Data Leakage) entsteht und die Bewertung unzuverlaessig wird.

Punktevergabe:
- 2 Punkte fuer gute Begruendung der Trennung.
- 2 Punkte fuer korrekte Definition + Beispiel labeled/unlabeled.
- 1,5 Punkte fuer klare Antwort auf Testdatenfrage mit Begruendung.

### Aufgabe A4: Datenmenge und Datenqualitaet bewerten (3 Punkte)

Aufgabenstellung:

Ein Team trainiert dasselbe Regressionsmodell zweimal:
- Lauf 1: 20 Datensaetze
- Lauf 2: vollstaendiger Datensatz

Bewerte in 4-6 Saetzen, wie sich Datenmenge und Datenqualitaet auf MSE und R2 auswirken koennen. (3 Punkte)

Musterloesung:

- Bei nur 20 Datensaetzen lernt das Modell oft instabil und verallgemeinert schlechter.
- Mit mehr Daten werden Muster besser erfasst, wodurch MSE typischerweise sinkt und R2 steigen kann.
- Schlechte Datenqualitaet (Ausreisser, fehlende Werte, falsche Einheiten) kann die Guete trotz grosser Datenmenge verschlechtern.
- Gute Datenqualitaet und ausreichende Datenmenge zusammen liefern meist robustere Vorhersagen.

Punktevergabe:
- 1 Punkt: Effekt der Datenmenge.
- 1 Punkt: Effekt der Datenqualitaet.
- 1 Punkt: Bezug zu MSE/R2 fachlich korrekt.

## Teil B: Praxis (7,5 Punkte)

### Aufgabe B1: Python/Pandas-Grundablauf (7,5 Punkte)

Aufgabenstellung:

Schreibe den Code handschriftlich oder in sauberem Pseudocode. Nutze folgende Annahme:
- Dateiname: ../notebooks/daten/haeuser.csv
- wichtige Spalten: groesse_m2, zimmer, baujahr, preis_euro

1. Lade die CSV-Datei mit Pandas und gib die ersten 5 Zeilen aus. (2 Punkte)
2. Berechne den durchschnittlichen, minimalen und maximalen Hauspreis. (2,5 Punkte)
3. Teile die Daten in Training/Test (80/20), trainiere eine lineare Regression und gib MSE und R2 aus. (3 Punkte)

Musterloesung:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1) CSV laden und erste Zeilen anzeigen
df = pd.read_csv("../notebooks/daten/haeuser.csv")
print(df.head())

# 2) Grundstatistiken Preis
durchschnitt = df["preis_euro"].mean()
minimum = df["preis_euro"].min()
maximum = df["preis_euro"].max()
print(durchschnitt, minimum, maximum)

# 3) Split, Modell, Kennzahlen
X = df[["groesse_m2", "zimmer", "baujahr"]]
y = df["preis_euro"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MSE:", mse)
print("R2:", r2)
```

Punktevergabe:
- 2 Punkte: CSV korrekt geladen, `head()` ausgegeben.
- 2,5 Punkte: Mittelwert, Minimum, Maximum korrekt aus `preis_euro` berechnet.
- 3 Punkte: korrekter 80/20-Split, lineare Regression trainiert, MSE und R2 ausgegeben.

## Korrekturhinweis fuer handschriftliche Loesungen

- Fachlogik geht vor perfekter Syntax.
- Leichte Schreibfehler in Variablennamen koennen toleriert werden, wenn der Ablauf klar und richtig ist.
- Auch strukturierter Pseudocode kann voll bewertet werden, wenn alle geforderten Schritte vorhanden sind.

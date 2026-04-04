# Grundlagen KI und ML - Skript (ca. 30 LPE)

Dieses Skript ist als durchgehender Lernpfad fuer den schulischen Einsatz gedacht.
Es kombiniert Fachinhalte, Impulse, Begriffe, Mini-Aufgaben und Reflexion.

## Zielbild

- Schueler unterscheiden KI, ML und Datenkompetenz sicher.
- Schueler koennen einfache Datensaetze lesen, interpretieren und vorbereiten.
- Schueler koennen ein einfaches Regressionsmodell verstehen, nutzen und kritisch bewerten.

## Empfohlener Umfang

- Gesamtumfang: ca. 30 LPE
- Vorschlag: 10 Lernbloecke zu je 3 LPE

## Struktur fuer jede LPE

1. Einstieg (5-10 Min): Leitfrage oder Beispiel aus dem Alltag
2. Erarbeitung (20-25 Min): Begriff, Methode, Demonstration
3. Sicherung (10-15 Min): Mini-Aufgabe + gemeinsamer Check
4. Transfer (5-10 Min): kurze Anwendung auf neuen Kontext

## Lernblock 1 (3 LPE): KI im Alltag, Chancen und Grenzen

### Kerninhalte

- Was ist KI?
- Wo begegnet uns KI im Alltag (Navigation, Empfehlungssysteme, Sprachassistenten)?
- Chancen (Unterstuetzung, Automatisierung) und Risiken (Bias, Intransparenz)

### Begriffe

- KI
- Algorithmus
- Automatisierung
- Datenbasis

### Impulse

- Warum ist nicht jedes "smarte" System automatisch KI?
- Welche Entscheidungen sollten Menschen nicht vollstaendig an KI delegieren?

### Mini-Aufgabe

- Sammle 5 Alltagsbeispiele und ordne: KI oder keine KI? Begruende jeweils in 1 Satz.

## Lernblock 2 (3 LPE): Was ist Machine Learning?

### Kerninhalte

- ML als Teilgebiet der KI
- Unterschied: regelbasiertes Programmieren vs. Lernen aus Daten

```
Klassisches Programmieren: Eingabe + Regeln -> Ausgabe
Machine Learning:          Eingabe + Ausgabe -> Regeln (Modell)
```

### Begriffe

- Machine Learning
- Modell
- Training
- Vorhersage

### Mini-Aufgabe

- Formuliere fuer zwei Probleme, ob klassisches Programmieren oder ML sinnvoller ist.

## Lernblock 3 (3 LPE): Lernarten im ML

### Kerninhalte

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning

### Begriffe

- Label
- Klassifikation
- Regression
- Clustering
- Reward

### Mini-Aufgabe

- Ordne 6 Beispielprobleme einer Lernart zu und erklaere kurz die Wahl.

## Lernblock 4 (3 LPE): Daten verstehen

### Kerninhalte

- Datensatz aufbauen und lesen
- Feature vs. Label
- Datentypen (numerisch, kategorial)

### Begriffe

- Datensatz
- Feature
- Label
- Zielvariable

### Mini-Aufgabe

- Nutze einen einfachen Datensatz und markiere pro Spalte: Feature oder Label, Datentyp, moegliche Probleme.

## Lernblock 5 (3 LPE): Datenqualitaet und Vorbereitung

### Kerninhalte

- Fehlende Werte
- Ausreisser
- Skalierung und einfache Bereinigung

### Begriffe

- Missing Values
- Outlier
- Vorverarbeitung

### Mini-Aufgabe

- Fuehre drei Bereinigungsschritte durch und begruende jeden Schritt in 1-2 Saetzen.

## Lernblock 6 (3 LPE): Lineare Regression verstehen

### Kerninhalte

- Idee der linearen Regression
- Gerade als Modell
- Zusammenhang zwischen Eingabe und Zielwert

### Begriffe

- Lineare Regression
- Koeffizient (Steigung)
- Intercept (Achsenabschnitt)

### Mini-Aufgabe

- Interpretiere Steigung und Intercept in einem konkreten Beispiel (z. B. Wohnflaeche -> Preis).

## Lernblock 7 (3 LPE): Modell trainieren

### Kerninhalte

- Trainings- und Testdaten
- Einfacher Trainingsablauf in Python/Notebook

### Begriffe

- Train-Test-Split
- Fit
- Predict

### Mini-Aufgabe

- Trainiere ein einfaches Modell und dokumentiere die Schritte als Lernprotokoll.

## Lernblock 8 (3 LPE): Modell bewerten

### Kerninhalte

- Fehlermae (einfach erklaert)
- Aussagekraft einer Vorhersage
- Plausibilitaetscheck

### Begriffe

- MAE
- MSE
- R2
- Residuum

### Mini-Aufgabe

- Vergleiche zwei Modelle mit denselben Daten und entscheide, welches sinnvoller ist.

## Lernblock 9 (3 LPE): Fehleranalyse und Modellgrenzen

### Kerninhalte

- Overfitting und Underfitting
- Generalisierung
- Datenverzerrung (Bias)

### Begriffe

- Overfitting
- Underfitting
- Generalisierung
- Bias

### Mini-Aufgabe

- Erklaere zu drei Fehlerszenarien die wahrscheinliche Ursache und eine Verbesserungsidee.

## Lernblock 10 (3 LPE): Transferprojekt und Reflexion

### Kerninhalte

- Kleine Projektfrage entwickeln
- Daten nutzen, Modell bauen, Ergebnis reflektieren
- Grenzen und Verantwortung benennen

### Begriffe

- Modellkritik
- Transparenz
- Verantwortung

### Mini-Aufgabe

- Teamprojekt mit Kurzpraesentation (Problem, Vorgehen, Ergebnis, Grenzen, naechster Schritt).

## Glossar der wichtigsten Begriffe

| Begriff | Kurzdefinition |
|---|---|
| KI | Systeme, die Aufgaben mit intelligent wirkendem Verhalten ausfuehren |
| ML | Teilgebiet der KI, bei dem Systeme aus Daten lernen |
| Datensatz | Strukturierte Sammlung von Beobachtungen |
| Feature | Eingabemerkmal zur Vorhersage |
| Label | Zielwert, der vorhergesagt werden soll |
| Modell | Mathematische Abbildung von Eingaben auf Ausgaben |
| Training | Lernphase des Modells |
| Test | Pruefung mit unbekannten Daten |
| Vorhersage | Ergebnis des Modells fuer neue Eingaben |
| Regression | Vorhersage kontinuierlicher Werte |
| Klassifikation | Zuordnung zu Klassen |
| Clustering | Gruppierung ohne vorgegebene Labels |
| Overfitting | Modell passt Trainingsdaten zu stark an |
| Underfitting | Modell ist zu einfach und lernt zu wenig |
| Bias | Systematische Verzerrung in Daten oder Modell |

## Didaktische Hinweise fuer Lehrkraefte

- Arbeite mit gestuften Hilfen:
  - Hilfe 1: Impulsfrage
  - Hilfe 2: Strategiehinweis
  - Hilfe 3: Fachhinweis
- Lass Schueler zuerst Hypothesen formulieren, dann rechnen/coden.
- Nutze Fehler als Lernanlass ("Was sagt uns der Fehler?").
- Halte Fachsprache sichtbar (Tafel/Glossarwand).

## Erwartungshorizont (kompakt)

- Basisniveau:
  - KI/ML begrifflich unterscheiden
  - einfache Datensaetze lesen
  - lineare Regression in Grundidee erklaeren
- Mittleres Niveau:
  - Modell auf einfachem Datensatz anwenden
  - Ergebnisse mit Fehlerwerten deuten
  - Grenzen des Modells benennen
- Erweitertes Niveau:
  - Verbesserungsmassnahmen begruenden
  - Datenqualitaet kritisch reflektieren
  - Transfer auf neue Fragestellungen leisten

## Pruef- und Aufgabenideen fuer den Kurs

1. Begriffstest mit Begruendung (KI/ML/Feature/Label)
2. Datensatzanalyse mit 5 Leitfragen
3. Guided Coding zur linearen Regression
4. Ergebnisinterpretation mit Fehleranalyse
5. Mini-Projekt mit Reflexionsbericht

## Verbindung zum Repository

- Lernhorizont: ../../informationen/lehrplan/lernhorizont.md
- Marschplan KI/ML: ../../informationen/lehrplan/marschplan-ki-ml.md
- Aufgaben: ../../aufgaben/
- Notebooks: ../../notebooks/
- Tests: ../../tests/

# Marschplan KI/ML Lehrplaneinheit

## Metadaten

- Bereich: KI und Machine Learning
- Stand: 2026-04-01
- Bezug: lernhorizont.md Version 0.1
- Zielgruppe: Schuelerinnen und Schueler (Sek I/II, anpassbar)
- Zweck: Didaktischer Fahrplan + Aufgabenvorschlaege + Umsetzungsreihenfolge

## Kurzantwort auf deine Frage

Ja, ein Marschplan existiert bereits unter `template/docs/handbuch/marschplaene/HAUPTMARSCHPLAN.md`.
Dieser ist jedoch auf die Routinen-Wissensdatenbank ausgerichtet, nicht auf die KI/ML-Lehrplaneinheit.
Dieser neue Marschplan schliesst genau diese Luecke.

## Didaktische Leitidee

- Ziel: Schueler sollen von Begriffsverstaendnis zu eigenstaendiger Modellanwendung gelangen.
- Prinzip: Fuehren -> Ueben -> Transfer -> Reflektieren.
- Hilfe-Design: Gestufte Hilfen (Impuls, Strategie, fachliche Hilfe), damit Selbststaendigkeit erhalten bleibt.
- Bewertung: Erwartungshorizont pro Aufgabe transparent machen (fachlich, methodisch, begruendend).

## Umfangsvorschlag (konkretisierbar)

- Moduldauer: 4 Module
- Zeit je Modul: 90 Minuten (oder 2 x 45 Min)
- Gesamtzeit: 6-8 Unterrichtsstunden

## Lernpfad (Module)

### Modul 1: KI, ML, Datenbegriff

- Lernziel: KI, ML und Daten sauber unterscheiden; Begriffe sicher anwenden.
- Fokus: KI vs. ML, Datensatz, Feature, Label, Modell.
- Produkt: Begriffslandkarte + kurze Begruendung in eigenen Worten.

### Modul 2: Daten erkunden und aufbereiten

- Lernziel: Einfache Datensaetze beschreiben und interpretieren.
- Fokus: Spaltenarten, Ausreisser, Fehlwerte, einfache Visualisierung.
- Produkt: Mini-Datenreport (3 Erkenntnisse + 1 Frage an die Daten).

### Modul 3: Lineare Regression verstehen

- Lernziel: Lineare Regression konzeptionell erklaeren.
- Fokus: Gerade als Modell, Zusammenhang Feature-Label, Training.
- Produkt: Regressionsplot + verbale Erklaerung.

### Modul 4: Modellbewertung und Fehleranalyse

- Lernziel: Ergebnisse nachvollziehbar begruenden.
- Fokus: Vorhersagefehler, einfache Guetemasse, Grenzen des Modells.
- Produkt: Kurze Ergebnisreflexion mit Verbesserungsvorschlag.

## Aufgabenpool (Erwartungshorizont-konform)

### A1 Begriffe sortieren (Einstieg)

- Typ: Kurzaufgabe (15-20 Min)
- Auftrag: Ordne 12 Begriffe den Kategorien KI, ML, Daten zu und begruende 3 Zuordnungen.
- Erwartungshorizont:
  - Basis: 8/12 korrekt.
  - Standard: 10/12 korrekt + 2 sinnvolle Begruendungen.
  - Erweitert: 12/12 + fachsprachlich praezise Begruendung.

### A2 Datensatz lesen und erklaeren

- Typ: Analyseaufgabe (30 Min)
- Auftrag: Beschreibe den Datensatz `notebooks/daten/haeuser.csv` anhand von 5 Leitfragen.
- Erwartungshorizont:
  - erkennt Features/Label korrekt,
  - beschreibt Auffaelligkeiten,
  - formuliert mindestens 1 Hypothese.

### A3 Datenaufbereitung minimal

- Typ: Notebook-Aufgabe (30-40 Min)
- Auftrag: Fehlende Werte behandeln, 1 Ausreisser markieren, 1 begruendete Bereinigungsentscheidung.
- Erwartungshorizont:
  - nachvollziehbarer Workflow,
  - fachlich stimmige Entscheidung,
  - Begruendung in 3-5 Saetzen.

### A4 Erste Regression bauen

- Typ: Guided Coding (45 Min)
- Auftrag: Trainiere ein lineares Regressionsmodell und gib Koeffizient/Intercept aus.
- Erwartungshorizont:
  - Pipeline laeuft,
  - Parameter koennen in Worten erklaert werden,
  - 1 fachlicher Grenzenhinweis.

### A5 Vorhersage interpretieren

- Typ: Transferaufgabe (20-30 Min)
- Auftrag: Interpretiere 3 neue Vorhersagen und entscheide, welche plausibel ist.
- Erwartungshorizont:
  - nutzt Modelllogik statt Raten,
  - begruendet Unsicherheit,
  - erkennt mindestens 1 unplausiblen Wert.

### A6 Fehleranalyse und Verbesserung

- Typ: Reflexionsaufgabe (30 Min)
- Auftrag: Vergleiche Ist/Soll-Werte, identifiziere Fehlermuster und schlage 2 Verbesserungen vor.
- Erwartungshorizont:
  - benennt Fehlermuster,
  - verknuepft Ursache und Wirkung,
  - macht umsetzbare Vorschlaege.

### A7 Mini-Projekt (optional, differenzierend)

- Typ: Teamarbeit (60-90 Min)
- Auftrag: Eigene Fragestellung mit kleinem Datensatz, Modellbau, Kurzpraesentation.
- Erwartungshorizont:
  - strukturierte Vorgehensweise,
  - nachvollziehbare Ergebnisse,
  - kritische Reflexion der Modellgrenzen.

## Paedagogisch sinnvolle Hilfestruktur pro Aufgabe

- Hilfe 1 Impulsfrage: "Was ist hier die Kernfrage?"
- Hilfe 2 Strategiehinweis: "Welche 3 Schritte fuehren zum Ziel?"
- Hilfe 3 Fachhilfe: "Welche Formel/Funktion passt konkret?"
- Selbstcheck: 2-3 Kontrollfragen vor Abgabe.

## Bewertungsraster (einfach, transparent)

- Fachlichkeit (40%): inhaltlich korrekt, Begriffe richtig.
- Methode (30%): nachvollziehbarer Arbeitsweg.
- Begruendung (20%): Entscheidungen und Ergebnisse erklaert.
- Darstellung (10%): klar, strukturiert, lesbar.

## Umsetzungs-Marschplan in 4 Phasen

### Phase 1: Lehrplan konkretisieren (1 Tag)

1. TBDs in lernhorizont.md fuellen (Kursdauer, Lernzeit, Modulanzahl).
2. Bewertungsraster finalisieren.
3. Lernziele je Modul in "muss/kann" differenzieren.

### Phase 2: Aufgabenbasis erstellen (2-3 Tage)

1. Aufgaben A1-A6 als Markdown in `aufgaben/` anlegen.
2. Musterloesungen in `loesungen/` anlegen.
3. Zu jeder Aufgabe 3 Hilfestufen definieren.

### Phase 3: Praktische Durchfuehrung absichern (2 Tage)

1. Notebooks fuer Modul 1-4 erstellen/aktualisieren.
2. Browserbasierte Uebungs- und Teststrecken erweitern.
3. Tests in `tests/` je Aufgabe ergänzen.

### Phase 4: Pilot und Iteration (1-2 Durchlaeufe)

1. Pilot in einer Lerngruppe (30-60 Min Beobachtung).
2. Auswertung: Wo brauchten Schueler zu viel Hilfe?
3. Aufgaben und Hilfen iterativ nachjustieren.

## Konkrete naechste 10 ToDos

1. `informationen/lehrplan/lernhorizont.md`: TBD-Felder konkret ausfuellen.
2. `aufgaben/01_grundlagen/`: Aufgabe A1 und A2 anlegen.
3. `aufgaben/03_regression/`: Aufgabe A4 und A5 anlegen.
4. `loesungen/01_grundlagen/`: Loesungen zu A1/A2 anlegen.
5. `loesungen/03_regression/`: Loesungen zu A4/A5 anlegen.
6. `notebooks/`: Notebook fuer A2 (Datenanalyse) und A4 (Regression) erstellen.
7. `tests/01_grundlagen/`: Tests fuer A1/A2 ergaenzen.
8. `tests/03_regression/`: Tests fuer A4/A5 ergaenzen.
9. Frontend-Hilfe-Boxen um Hilfestufen pro Aufgabe erweitern.
10. Lehrkraft-Checkliste fuer Erwartungshorizont-Bewertung erstellen.

## Zuordnung Lernziel -> Aufgaben (Startvorschlag)

- KI/ML unterscheiden -> A1
- Datensaetze beschreiben/interpretieren -> A2, A3
- Regression erklaeren -> A4
- Regressionsergebnis begruenden -> A5, A6
- Modellbewertung/Fehleranalyse -> A6, A7

## Hinweise zur Erweiterbarkeit und Wiederverwendung

- Aufgaben als strukturierte Daten halten (JSON/YAML/DB), nicht fest im UI.
- Hilfen, Tests und Bewertungsraster als wiederverwendbare Felder modellieren.
- API versionieren (`/api/v1/...`) fuer andere Repos als stabile Schnittstelle.
- Dokumentation als Single Source of Truth im Lehrplan-Ordner pflegen.

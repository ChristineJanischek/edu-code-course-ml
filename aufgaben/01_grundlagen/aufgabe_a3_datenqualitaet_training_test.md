# Aufgabe A3: Datenqualitaet, Training/Test, labeled/unlabeled

**BPE-Bezug:** BPE 6.2 (Bedeutung von Daten fuer ML)  
**Dauer:** 4 Unterrichtsstunden  
**Niveau:** Standard

## Lernziele

- Trainings- und Testdaten sicher unterscheiden und anwenden.
- labeled und unlabeled Data fachlich korrekt einordnen.
- Zusammenhang zwischen Datenmenge und Vorhersagequalitaet begruenden.

## Schritt-fuer-Schritt (Pflichtpfad)

1. Lade den Datensatz [haeuser.csv](../../notebooks/daten/haeuser.csv) in Python.
2. Erstelle zwei Datensaetze:
   - klein (erste 20 Zeilen)
   - gross (vollstaendige Daten)
3. Teile beide Datensaetze in Training und Test (80/20).
4. Trainiere in beiden Faellen dasselbe einfache Regressionsmodell.
5. Vergleiche MSE und R2 der beiden Modelle.
6. Kennzeichne in einem Beispiel, was labeled Data und was unlabeled Data waere.
7. Formuliere eine Bewertung in 8 bis 10 Saetzen: Welche Rolle spielen Datenmenge und Datenqualitaet?

## Hilfekarten

- Hilfe 1 (Impuls): Darf das Modell Testdaten beim Lernen sehen?
- Hilfe 2 (Strategie): Halte Modell und Parameter konstant, variiere nur die Datenmenge.
- Hilfe 3 (Fachhilfe): labeled Data enthalten Zielwerte, unlabeled Data nicht.

## Kennzahlenhilfe (MSE und R2)

- MSE (Mean Squared Error): Durchschnitt der quadrierten Fehler zwischen echtem Preis und Vorhersage.
- Interpretation MSE: Je kleiner, desto besser. Einheit ist Preis^2, daher ist MSE vor allem fuer den Vergleich von Modellen auf demselben Datensatz geeignet.
- R2 (Bestimmtheitsmass): Anteil der erklaerten Varianz im Zielwert.
- Interpretation R2: Je naeher an 1.0, desto besser. 0.0 bedeutet "nicht besser als Mittelwert", negative Werte bedeuten "schlechter als Mittelwert".
- Wichtig fuer A3: Vergleiche immer MSE und R2 gemeinsam und nur bei gleichem Zielwert, gleichem Split und gleichem Modell.

## Abgabe

- Notebook-Auswertung mit Kennzahlenvergleich
- Kurztext zur Datenbedeutung

## Selbstcheck

- Kann ich Trainingsdaten und Testdaten begruenden?
- Kann ich labeled/unlabeled anhand eines Beispiels erklaeren?
- Kann ich den Effekt der Datenmenge argumentativ darstellen?

## Kann-Ziel (Erweiterung)

Fuehre zusaetzlich einen Qualitaetsvergleich durch (z. B. Ausreisser entfernen) und bewerte die Aenderung der Modellguete.

# Grundlagen: Künstliche Intelligenz & Machine Learning

## Was ist Künstliche Intelligenz (KI)?

KI bezeichnet Systeme, die Aufgaben ausführen, die normalerweise menschliche Intelligenz erfordern – z. B. Bilder erkennen, Texte verstehen oder Entscheidungen treffen.

## Was ist Machine Learning (ML)?

Machine Learning ist ein Teilgebiet der KI. Statt Regeln manuell zu programmieren, **lernt** das System selbst aus Daten.

```
Traditionelle Programmierung:   Eingabe + Regeln → Ausgabe
Machine Learning:               Eingabe + Ausgabe → Regeln (das Modell)
```

---

## Die drei Lernarten

### 1. Überwachtes Lernen (Supervised Learning)
- Das Modell lernt aus **beschrifteten Beispielen** (Eingabe + richtige Antwort)
- Beispiel: E-Mails als Spam / Kein Spam klassifizieren
- Aufgabentypen: **Klassifikation**, **Regression**

### 2. Unüberwachtes Lernen (Unsupervised Learning)
- Das Modell bekommt **keine Beschriftungen**, sucht selbst nach Mustern
- Beispiel: Kunden nach Kaufverhalten gruppieren
- Aufgabentypen: **Clustering**, **Dimensionsreduktion**

### 3. Bestärkendes Lernen (Reinforcement Learning)
- Ein Agent lernt durch **Belohnungen und Strafen** in einer Umgebung
- Beispiel: KI lernt, ein Videospiel zu spielen

---

## Wichtige Begriffe

| Begriff | Erklärung |
|--------|-----------|
| **Datensatz (Dataset)** | Sammlung von Daten, mit denen das Modell lernt |
| **Feature** | Eingabemerkmal (z. B. Alter, Größe, Farbe) |
| **Label / Zielgröße** | Die richtige Antwort / das, was vorhergesagt werden soll |
| **Training** | Das Modell lernt aus den Trainingsdaten |
| **Test** | Das Modell wird auf neuen, unbekannten Daten geprüft |
| **Modell** | Das Ergebnis des Lernprozesses – eine mathematische Funktion |
| **Vorhersage** | Das Ergebnis, das das Modell für neue Eingaben ausgibt |
| **Genauigkeit (Accuracy)** | Anteil der richtigen Vorhersagen in % |
| **Overfitting** | Modell hat Trainingsdaten auswendig gelernt, funktioniert bei neuen Daten schlecht |
| **Underfitting** | Modell ist zu einfach und lernt zu wenig aus den Daten |

---

## Typischer ML-Ablauf

```
1. Problem definieren
       ↓
2. Daten sammeln & aufbereiten
       ↓
3. Modell auswählen
       ↓
4. Modell trainieren
       ↓
5. Modell testen & bewerten
       ↓
6. Modell verbessern (zurück zu Schritt 3/4)
       ↓
7. Modell einsetzen
```

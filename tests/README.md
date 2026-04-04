# Tests

Dieses Verzeichnis enthält automatisierte Tests, mit denen Schüler ihre Lösungen selbst überprüfen können.

## Struktur

```
tests/
├── 01_grundlagen/      ← Tests zu Grundlagenaufgaben
├── 02_klassifikation/  ← Tests zu Klassifikationsaufgaben
├── 03_regression/      ← Tests zu Regressionsaufgaben
├── live/               ← Live-Test für Docker-Gesamtstack (Java, MySQL, Python, PHP, JS)
└── konfig/             ← Gemeinsame Hilfsfunktionen
```

## Tests ausführen

```bash
# Alle Tests
python -m pytest tests/ -v

# Tests für eine bestimmte Aufgabe
python -m pytest tests/01_grundlagen/ -v

# Live-Test der Docker-Anwendung
chmod +x tests/live/test_live_stack.sh
./tests/live/test_live_stack.sh

# Security-Smoke-Test der Docker-Anwendung
chmod +x tests/live/security_smoke.sh
./tests/live/security_smoke.sh
```

## Hinweise für Schüler

- Die Tests prüfen, ob deine Lösung das richtige Ergebnis liefert
- Ein ✓ (grün) bedeutet: Test bestanden
- Ein ✗ (rot) bedeutet: Noch nicht korrekt – lies die Fehlermeldung genau
- Die Tests geben dir Hinweise, aber nicht die vollständige Lösung

# edu-code-course-ml
Dieses Repo enthält die speziellen Kenntnisse (Aufgaben, Lösungen, Informationen, Tests) und eine vollständige Testumgebung zum besseren Verständnis der Künstlichen Intelligenz und im Speziellen des Machine Learning. Es richtet sich an Schüler und Lehrer mit Interesse an einem praxisnahen Unterricht.

## Projektstruktur & Template

Dieses Repo nutzt [edu-code-projecttemplate](https://github.com/ChristineJanischek/edu-code-projecttemplate) als Basis-Infrastruktur. Das Template stellt eine vollständige Laufzeitumgebung bereit (PHP-Webapp, Python-API, MySQL, Java) inklusive Scripts und Dokumentationsvorlagen.

```
edu-code-course-ml/
├── template/       ← Submodule: edu-code-projecttemplate (Laufzeitumgebung)
├── aufgaben/       ← ML-Aufgaben für Schüler
├── loesungen/      ← Musterlösungen
├── notebooks/      ← Jupyter Notebooks
├── tests/          ← Tests zu den Aufgaben
└── README.md
```

## Schnellstart

**1. Repo klonen (mit Submodule):**
```bash
git clone --recurse-submodules https://github.com/ChristineJanischek/edu-code-course-ml.git
# oder nach einem normalen Clone:
git submodule update --init --recursive
```

**2. Umgebung starten:**
```bash
cd template
bash scripts/bootstrap.sh        # .env aus .env.example erstellen und anpassen
bash scripts/start-services.sh   # Docker-Dienste starten
```

**3. Services erreichbar unter:**
- PHP-Webapp: `http://localhost:8080`
- Python-API: `http://localhost:8000/health`

**4. Template aktualisieren (bei Änderungen am Original):**
```bash
git submodule update --remote template
git commit -m "chore: template aktualisiert"
git push
```

---

## Umgang mit dem Template

### Was ist das Template?

Das Template [edu-code-projecttemplate](https://github.com/ChristineJanischek/edu-code-projecttemplate) ist eine vorgefertigte Entwicklungsumgebung für Schulprojekte. Es liegt in diesem Repo unter `template/` und ist als **Git Submodule** eingebunden — d. h. es ist eine Verknüpfung zum Original-Repo, kein einfacher Ordner.

---

### Täglicher Umgang

#### Services starten und stoppen
```bash
cd template

# Starten (beim ersten Mal oder nach Änderungen)
bash scripts/start-services.sh

# Stoppen
bash scripts/stop-services.sh
```

#### Tests ausführen
```bash
cd template

# Alle Services testen (PHP, Python-API, MySQL, Java)
bash scripts/test-services.sh

# Nur Dokumentation prüfen
bash scripts/validate-docs.sh

# Architektur prüfen (Java OOP-Regeln)
bash scripts/validate-architecture.sh

# Sicherheit prüfen (.env, Credentials)
bash scripts/validate-security.sh
```

---

### Neue Inhalte ergänzen (ML-Kurs)

Das Template stellt die Infrastruktur bereit. Die eigentlichen ML-Kursinhalte kommen **nicht** in den `template/`-Ordner, sondern direkt ins Hauptverzeichnis:

```
aufgaben/          ← Neue Aufgabe hier anlegen
loesungen/         ← Musterlösung hier ablegen
notebooks/         ← Jupyter Notebook hier speichern
tests/             ← Tests zur Aufgabe hier ergänzen
```

Die **Python-API** (`template/services/python-api/app.py`) kann für ML-Demos direkt erweitert werden.

---

### Template-Änderungen übernehmen

Wenn am Original-Template (`edu-code-projecttemplate`) etwas geändert wurde und du die Neuigkeiten übernehmen möchtest:

```bash
# Im Hauptverzeichnis des Repos
git submodule update --remote template
git add template
git commit -m "chore: template auf neueste Version aktualisiert"
git push
```

> **Wichtig:** Das Submodule verweist immer auf einen bestimmten Commit des Template-Repos. Nach `git submodule update --remote` zeigt es auf den neuesten Commit. Überprüfe vorher, ob Breaking Changes vorhanden sind.

---

### Häufige Probleme

| Problem | Lösung |
|--------|--------|
| `template/`-Ordner ist leer nach Clone | `git submodule update --init --recursive` ausführen |
| `.env` fehlt | `cd template && bash scripts/bootstrap.sh` |
| `.env` enthält noch `CHANGE_ME` | `template/.env` öffnen und Werte eintragen |
| Docker-Services starten nicht | Docker Desktop läuft? `docker info` prüfen |
| Port bereits belegt | In `template/.env` Port-Variablen anpassen (`PHP_WEB_PORT`, `PYTHON_API_PORT`) |

---

### Übersicht der Template-Scripts

| Script | Beschreibung |
|--------|-------------|
| `scripts/bootstrap.sh` | `.env` aus `.env.example` erzeugen, Rechte setzen |
| `scripts/start-services.sh` | Docker-Dienste bauen und starten |
| `scripts/stop-services.sh` | Docker-Dienste stoppen |
| `scripts/test-services.sh` | Alle Services testen (HTTP, MySQL, Java) |
| `scripts/validate-docs.sh` | Dokumentationspflicht prüfen |
| `scripts/validate-architecture.sh` | Java-Architekturregeln prüfen |
| `scripts/validate-security.sh` | Sicherheits-Check (Credentials, `.env`) |

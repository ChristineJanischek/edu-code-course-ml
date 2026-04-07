# edu-code-course-ml
Dieses Repo enthält die speziellen Kenntnisse (Aufgaben, Lösungen, Informationen, Tests) und eine vollständige Testumgebung zum besseren Verständnis der Künstlichen Intelligenz und im Speziellen des Machine Learning. Es richtet sich an Schüler und Lehrer mit Interesse an einem praxisnahen Unterricht.

## Neu: Live testbare Anwendung im Hauptrepo

Zusätzlich zum Template gibt es jetzt eine direkt im Hauptrepo ausführbare Docker-Umgebung mit "Hallo Welt" für:

- Java
- MySQL
- Python
- PHP
- JavaScript

Sie liegt in `src/` (Services und DB-Init), wird über `docker-compose.yml` im Repo-Root gestartet und mit einem Live-Test geprüft.

Schritt-für-Schritt-Anleitung (E-Learning komplett testen): [informationen/werkzeuge/elearning-testen.md](informationen/werkzeuge/elearning-testen.md)
Schritt-für-Schritt-Anleitung (Docker-Stack): [informationen/werkzeuge/live-test-anleitung.md](informationen/werkzeuge/live-test-anleitung.md)
Lehrkraft-Kurzreferenz Tests (BPE 6/7): [informationen/werkzeuge/lehrkraft-test-kurzreferenz.md](informationen/werkzeuge/lehrkraft-test-kurzreferenz.md)
Bewertungsmatrix A1-B4 (BPE 6/7): [informationen/lehrplan/bewertungsmatrix-a1-b4.md](informationen/lehrplan/bewertungsmatrix-a1-b4.md)
Druckversion Bewertungsbogen A1-B4: [informationen/lehrplan/bewertungsbogen-a1-b4-druckversion.md](informationen/lehrplan/bewertungsbogen-a1-b4-druckversion.md)
Kompaktbogen A1-B4 (2 Seiten): [informationen/lehrplan/bewertungsbogen-a1-b4-kompakt-2seiten.md](informationen/lehrplan/bewertungsbogen-a1-b4-kompakt-2seiten.md)
Einzelbogen erweitert: [informationen/lehrplan/bewertungsbogen-einzelperson-erweitert.md](informationen/lehrplan/bewertungsbogen-einzelperson-erweitert.md)
PDF-Exportversion A1-B4: [informationen/lehrplan/bewertungsbogen-a1-b4-pdf-export.md](informationen/lehrplan/bewertungsbogen-a1-b4-pdf-export.md)
Branch-Protection-Checkliste: [informationen/werkzeuge/branch-protection-checkliste.md](informationen/werkzeuge/branch-protection-checkliste.md)
Git-Freigabe und Backupstrategie: [informationen/werkzeuge/git-freigabe-backupstrategie.md](informationen/werkzeuge/git-freigabe-backupstrategie.md)

## Projektstruktur & Template

Dieses Repo nutzt [edu-code-projecttemplate](https://github.com/ChristineJanischek/edu-code-projecttemplate) als Basis-Infrastruktur. Das Template stellt eine vollständige Laufzeitumgebung bereit (PHP-Webapp, Python-API, MySQL, Java) inklusive Scripts und Dokumentationsvorlagen.

```
edu-code-course-ml/
├── src/              ← Neue live testbare Demo-Services (Java, Python, PHP, JS, MySQL-Init)
├── docker-compose.yml← Startet die Root-Live-Umgebung
├── template/         ← Submodule: edu-code-projecttemplate (Laufzeitumgebung)
├── informationen/    ← Hilfsmittel für Schüler (Grundlagen, Cheatsheets, Werkzeuge)
├── informationen/lehrplan/ ← Lernhorizont, Erwartungshorizont, Begrifflichkeiten, Themen
├── aufgaben/         ← ML-Aufgaben für Schüler
├── loesungen/        ← Musterlösungen
├── notebooks/        ← Jupyter Notebooks
├── tests/            ← Tests zu den Aufgaben
└── README.md
```

## Schnellstart

### A) Neue Root-Live-Umgebung (empfohlen für schnellen Start)

```bash
cp .env.example .env
## CHANGE_ME-Werte in .env durch sichere Passwoerter ersetzen
docker compose up -d --build
chmod +x tests/live/test_live_stack.sh
./tests/live/test_live_stack.sh
chmod +x tests/live/security_smoke.sh
./tests/live/security_smoke.sh
```

Wichtige URLs:
- PHP: `http://localhost:8080`
- JS-Web: `http://localhost:8081`
- Python: `http://localhost:8000/health`
- Java: `http://localhost:8082`

Details: [informationen/werkzeuge/live-test-anleitung.md](informationen/werkzeuge/live-test-anleitung.md)

Sicherheit:
- `.env` wird im Repo-Root per `.gitignore` ausgeschlossen.
- Services sind nur an `127.0.0.1` gebunden.
- Container laufen mit Security-Hardening (`no-new-privileges`, `cap_drop`, read-only wo sinnvoll).
- CI-Sicherheits-Scans laufen in `.github/workflows/security-scans.yml`.

### B) Template-Umgebung (Submodule)

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

Curriculare Leitdokumente (Lernhorizont) liegen in `informationen/lehrplan/`.

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

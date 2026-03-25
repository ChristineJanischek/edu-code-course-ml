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

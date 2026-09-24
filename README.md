# CI/CD-Demo mit GitHub Actions

Dieses Repository zeigt an einem kleinen Beispiel, wie eine CI/CD-Pipeline mit GitHub Actions funktioniert: von automatisierten Unit-Tests über einen geschützten Hauptzweig bis zum automatischen Deployment einer Webseite mit manueller Freigabe.

Es ergänzt die Ausarbeitung „DevOps – CI/CD als Kernbestandteil moderner Softwareentwicklung“ (THM, Modul WK1104, SoSe 2026) um ein praktisches Beispiel.

**Live-Seite:** https://ksukh-ux.github.io/cicd-demo/

## Übersicht der Übungen

| Nr. | Übung | Dateien / Einstellungen | Bezug zur Arbeit |
|---|---|---|---|
| 0 | CI-Pipeline mit Unit-Tests, bewusst rot und grün | `calc.py`, `test_calc.py`, `.github/workflows/ci.yml` | Kap. 2.2 CI, 3.3 Feedback, 3.3.1 Testpyramide |
| 1 | Geschützter `main`-Branch, Pull Request mit Pflicht-Check | Ruleset `main-schutz` | Kap. 3.4 Versionsverwaltung |
| 2A | Automatisches Deployment auf GitHub Pages | `site/index.html`, `.github/workflows/02-deploy.yml` | Kap. 2.3 Continuous Deployment |
| 2B | Manuelle Freigabe vor dem Go-live | Environment `github-pages` mit Required Reviewers | Kap. 2.3 Continuous Delivery, Kap. 7.4 |

## Aufbau des Repositorys

```
cicd-demo/
├── .github/
│   └── workflows/
│       ├── ci.yml           # CI: Tests bei jedem Push und Pull Request
│       └── 02-deploy.yml    # CD: Tests, danach Veröffentlichung auf GitHub Pages
├── site/
│   └── index.html           # Webseite, die veröffentlicht wird
├── calc.py                  # Programmcode: Funktionen add() und multiply()
├── test_calc.py             # Unit-Tests für calc.py
└── README.md
```

## Übung 0: Continuous Integration mit Unit-Tests

`calc.py` enthält zwei einfache Funktionen, `add(a, b)` und `multiply(a, b)`. `test_calc.py` enthält die zugehörigen **Unit-Tests**. Ein Unit-Test prüft eine einzelne Funktion isoliert und bildet damit die unterste Ebene der Testpyramide.

Die Pipeline `ci.yml` startet bei jedem Push auf `main` und bei jedem Pull Request. Sie holt den Code auf einen Runner (virtuelle Ubuntu-Maschine), richtet Python 3.12 ein, installiert pytest und führt alle Tests aus.

**Experiment:** In `add()` wurde `a + b` absichtlich zu `a - b` geändert. Der Test erwartet für `add(2, 3)` den Wert `5`, erhielt aber `-1`, und die Pipeline wurde rot. Nach der Korrektur wurde sie wieder grün.

**Erkenntnis:** Der Test blieb unverändert, nur der Code änderte sich. Der Test hält fest, wie sich der Code verhalten soll, und meldet jede Abweichung sofort nach dem Commit. Ohne Test hätte die Pipeline den syntaktisch korrekten, aber falschen Code durchgelassen.

## Übung 1: Geschützter Branch und Pull Requests

Für `main` gilt ein Ruleset:

- Änderungen nur über Pull Requests
- Der Check `test` aus `ci.yml` muss grün sein, bevor gemergt werden darf
- `main` darf nicht gelöscht oder per Force Push überschrieben werden

**Ablauf:** Die Funktion `multiply()` wurde auf einem eigenen Branch entwickelt und per Pull Request eingebracht. In einem zweiten Pull Request schlug ein Test fehl, und der Merge wurde automatisch blockiert. Die Pipeline wirkt damit als **Quality Gate**.

**Erkenntnis:** Ein grüner Check bedeutet nur, dass die vorhandenen Tests bestehen. Der erste Commit mit `multiply()` war grün, obwohl die Funktion noch nicht getestet war. Neuer Code braucht deshalb immer neue Tests (Testabdeckung).

## Übung 2A: Continuous Deployment

Die Pipeline `02-deploy.yml` startet bei jedem Push auf `main`, also nach jedem Merge. Sie besteht aus zwei Stufen:

1. **test:** führt die Unit-Tests aus
2. **deploy:** veröffentlicht den Ordner `site/` auf GitHub Pages

Durch `needs: test` startet `deploy` nur, wenn `test` erfolgreich war.

**Erkenntnis:** Nach dem Merge ist kein Mensch mehr beteiligt. Die Tests sind die einzige Qualitätsschranke vor dem Go-live.

## Übung 2B: Continuous Delivery

Für die Umgebung `github-pages` ist eine Freigabe eingerichtet (Required Reviewers). Nach erfolgreichen Tests wartet die Pipeline, bis das Deployment über „Review deployments“ manuell freigegeben wird. Anschließend wurde Version 2 der Seite veröffentlicht.

**Erkenntnis:** Continuous Delivery und Continuous Deployment unterscheiden sich nicht in der Pipeline selbst, sondern nur darin, ob vor dem letzten Schritt ein Mensch entscheidet. Die Freigabesteuerung über Environments zeigt außerdem, dass auch GitHub differenzierte Kontrollen über Umgebungen bietet (vgl. Kap. 7.4).

## Commit-Konvention

Die Commit-Nachrichten folgen den Conventional Commits, zum Beispiel `feat:`, `fix:`, `test:`, `docs:` und `ci:`.

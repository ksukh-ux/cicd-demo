# CI-Demo mit GitHub Actions

Dieses Repository zeigt an einem kleinen Beispiel, wie Continuous Integration (CI) mit GitHub Actions funktioniert. Eine Python-Funktion wird bei einem Push automatisch getestet. Anschließend wird absichtlich ein Rechenfehler eingebaut, damit sichtbar wird, wie der Test einen Fehler erkennt und der Workflow fehlschlägt.

Das Beispiel gehört zur Ausarbeitung „DevOps – CI/CD“.

## Dateien im Repository

- `calc.py` enthält die Programmfunktion `add(a, b)`. Sie soll zwei Zahlen addieren.
- `test_calc.py` enthält die Testfunktion `test_add()`. Sie prüft, ob `add(2, 3)` das erwartete Ergebnis `5` liefert.
- `.github/workflows/` enthält den GitHub-Actions-Workflow, der den Test automatisch ausführt.

## Was ist ein Unit-Test?

Ein Unit-Test prüft eine kleine Einheit eines Programms, hier die einzelne Funktion `add()`. Dafür wurde zusätzlich die Testfunktion `test_add()` angelegt:

Der Test kennt die richtige Antwort und prüft, ob der Code sie liefert. Das ist ein Unit-Test: Er prüft eine einzelne Einheit (Funktion) isoliert, also die unterste Ebene deiner Testpyramide.

## Warum erst grün, dann rot?

Bei jedem Push auf main startet die Pipeline, so steht es in on: push. Sie macht jedes Mal das Gleiche:

1. checkout holt den aktuellen Code auf den Runner.
2. setup-python richtet Python 3.12 ein.
3. pip install pytest installiert das Test-Werkzeug.
4. pytest sucht alle Tests und führt sie aus.

Erster Lauf (grün):
add(2, 3) rechnet 2 + 3 = 5. Der Vergleich 5 == 5 ist wahr, der Test besteht, und die Pipeline ist grün.

Zweiter Lauf (rot):
Du hast + zu - geändert. Jetzt rechnet add(2, 3) 2 - 3 = -1. Der Vergleich -1 == 5 ist falsch, assert schlägt fehl, pytest meldet einen Fehler, und die Pipeline wird rot.

Der entscheidende Punkt: Der Test hat sich nicht geändert, nur der Code. Der Test ist wie ein Sicherheitsnetz. Er hält fest, wie der Code sich verhalten soll, und schlägt Alarm, sobald jemand das Verhalten kaputt macht, selbst wenn es nur ein einziges Zeichen ist.

## Prüfung: betroffene Kapitel
- CI (2.2): Jeder Commit löst automatisch Build und Tests aus.
- Kontinuierliches Feedback (3.3): Der Fehler fällt Sekunden nach dem Commit auf, nicht erst beim Kunden.
- Warum CI ohne Tests nichts bringt: Die Pipeline hätte a - b ohne Test klaglos durchgelassen. Der Code ist ja syntaktisch korrekt, er rechnet nur falsch.




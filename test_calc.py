# Importiert die Funktion add aus der Datei calc.py.
from calc import add

# def test_add(): ist wieder eine Funktion, diesmal ein Test. pytest erkennt Tests automatisch daran, dass Datei und Funktion mit test_ beginnen.
def test_add():
    # assert heißt „ich behaupte, dass …“. Ist die Aussage wahr, passiert nichts und der Test besteht. Ist sie falsch, schlägt der Test fehl.
    # add(2, 3) == 5: == vergleicht zwei Werte. Die Behauptung lautet also: „Wenn ich add mit 2 und 3 aufrufe, kommt 5 heraus.“
    assert add(2, 3) == 5

#Der Zusammenhang ist:
# calc.py: enthält die Funktion, die rechnen soll.
# test_calc.py: prüft, ob die Funktion richtig rechnet.
# Die Pipeline: führt den Test automatisch aus.
# Den absichtlichen Fehler bauen wir in calc.py ein. Der Test bleibt unverändert, damit er den Fehler erkennt.

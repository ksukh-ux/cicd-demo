# Programmcode

# def definiert eine Funktion: ein wiederverwendbares Stück Code.
# add ist der Name der Funktion.
# (a, b) sind die Parameter, also die zwei Werte, die man der Funktion übergibt.
# : bedeutet Jetzt folgt, was die Funktion tut. Alles darunter, was eingerückt ist, gehört dazu.
def add(a, b):
    # Die Einrückung zeigt, dass diese Zeile zur Funktion gehört.
    # return a + b rechnet a + b und gibt das Ergebnis zurück.
    # add(2, 3) liefert also 5. Das ist die „Anwendung“, die wir testen wollen, bewusst winzig. In einem echten Projekt wäre das zum Beispiel die Berechnung einer Versicherungsprämie.
    return a + b


# CI Pipeline:
# Für die Demo bauen wir absichtlich einen Fehler ein:
# Wir ändern "return a + b" zu "return a - b" und committen die Änderung.
# Wenn der Workflow bei einem Push startet, führt GitHub Actions die Tests aus.
# Der Test erwartet z. B. bei add(2, 3) das Ergebnis 5,
# unsere Funktion liefert durch die Änderung aber -1.
# Dadurch schlägt der Test fehl und der Workflow wird rot angezeigt.
# Zum Beheben ändern wir das Minus wieder in ein Plus und committen erneut.
# Die Pipeline erkennt hier also absichtlich fehlerhaften Programmcode.



# Neue Funktion für diese Übung (Branch ksukh-ux-patch-1)
# Multipliziert zwei Zahlen.
# Beispiel: multiply(3, 4) liefert 12
def multiply(a, b):
    return a * b





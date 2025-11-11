# Aufgabe zur Permutation

---

Implementieren Sie eine statische Methode in Java, die alle Permutation für ein Array erzeugt. Es genügt, wenn Sie sich auf die Permutationen von {1, 2, 3, ..., n-1} beschränken.

Verwenden Sie dazu die Klasse Permutations und vervollständigen Sie diese Klasse
(mit TODO gekennzeichnet).



# Aufgabenstellung Parkettierung

---

![](../../../../../resources/parketierung.png)

- Ein «Schachbrett» mit Seitenlängen 𝑚 und 𝑛 soll mit 𝑚⋅𝑛/2 Dominosteinen überdeckt werden. \
 Auf wie viele Arten ist das möglich?
- Erstellen Sie eine Funktion, die für ein solches Schachbrett angibt, auf wie viele Arten es sich durch Dominosteine überdecken lässt, wobei ein Dominostein genau zwei Felder des Schachbretts überdeckt.
- Verwenden Sie dazu die Klasse [Parkettierung](Parkettierung.java) aus dem Package `ch.ffhs.dua.park` im Aufgabenprojekt aus dem Informationsblock dieses Moodle-Kurses und vervollständigen Sie dort diese Klasse (mit `TODO` gekennzeichnet).

---

### Hinweis für eine Lösungsmöglichkeit

- Auf rechteckige Schachbretter kann Rekursion nicht direkt angewendet werden, denn wenn ein Dominostein gesetzt wird, ist der unbedeckte Rest des Brettes nicht mehr rechteckig 😀

- Man kann das Problem verallgemeinern auf nicht-rechteckige «Schachbretter»

- Verallgemeinertes Problem: Auf wie viele Arten kann ein Schachbrett überdeckt werden mit einem rechten Flatterrand, also ein Brett der folgenden Form:
  ```
  XXXXXX
  XXXX
  XXXXXXXXXX
  XXXXXXXXXX
  XXX
  ```

- Idee für die Rekursion: Man wähle ein Feld am rechten Rand, das möglichst weit rechts liegt. Falls es mehrere solche Felder gibt, wähle man das oberste:
  ```
  XXXXXX
  XXXX
  XXXXXXXXXO
  XXXXXXXXXX
  XXX
  ```

- Jetzt wird der nächste Dominostein gelegt, sodass das gewählte Feld überdeckt wird; es gibt dazu maximal zwei Möglichkeiten:
  ```
  XXXXXX
  XXXX
  XXXXXXXXOO
  XXXXXXXXXX
  XXX
  ```
  oder
  ```
  XXXXXX
  XXXX
  XXXXXXXXXO
  XXXXXXXXXO
  XXX
  ```

- Damit kann das Problem rekursiv gelöst werden.

- Als Datenstruktur zur Beschreibung der (teilüberdeckten) Bretter kann ein int-Array mit der Länge der Reihen gewählt werden.


# Doppelt gekettete Listen
Implementieren Sie eine doppelt gekettete Liste sowie eine dazugehörige Iterator-Klasse.

Die Listenklasse soll die folgenden Methoden implementieren:

* `append(el)`
* `insert(index, el)`
* `pop(index=-1)`
* `__getitem__(index)`
* `__setitem__(index, val)`
* `__contains__(val)`
* `__len__()`
* `__iter__()`

Die `__iter__`-Methode soll eine Instanz einer Iterator-Klasse liefern. Diese sollte möglichst effizient implementiert sein und die folgenden Methoden implementieren:

* `__next__()`
* `__iter__()`

Die `__iter__` Methode gibt einfach `self` zurück; der Sinn dabei ist, dass in einem `for`-Loop der Form:

```python
for element in my_list:
    pass
```

intern zuerst `my_list.__iter__()` aufgerufen wird. Daher kann `my_list` sowohl selber ein Iterator sein oder aber eine Kollektion wie eine `list`, ein `set` oder eben eine DoubleLinkedList.

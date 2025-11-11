def binary_search(array, value, lower=0, higher=None):
    """
    Suche nach einem bestimmten Wert in einem sortierten Array mithilfe des Binärsuchalgorithmus.
    Diese Methode verwendet Rekursion, um alle Vorkommen des Werts in dem gegebenen Array zu finden,
    und gibt deren Indexbereich (einschließlich) zurück. Wenn der Wert im Array nicht gefunden wird,
    gibt die Funktion `None` zurück.

    :param array: Die sortierte Liste von Elementen, in der der Wert gesucht werden soll.
    :type array: list
    :param value: Wert, der im Array gesucht werden soll.
    :type value: Beliebiger Typ
    :param lower: unterer Grenzindex für das Suchintervall im Array.
    :type lower: int
    :param higher: oberer Grenzindex für das Suchintervall im Array.
    :type higher: int, optional
    :return: Tupel, das den Indexbereich (Startindex, Endindex) enthält, in dem der Wert gefunden wurde,
        oder `None`, falls der Wert nicht im Array vorhanden ist.
    :rtype: tuple[int, int] | None
    """

    pass


import unittest


class BinarySearchTest(unittest.TestCase):

    def test_empty_liste(self):
        self.assertIsNone(binary_search([], 0))

    def test_not_found(self):
        array = [1]
        self.assertIsNone(binary_search(array, 0))
        self.assertIsNone(binary_search(array, 3))

        array = [1, 2, 4, 5];
        self.assertIsNone(binary_search(array, 0))
        self.assertIsNone(binary_search(array, 3))
        self.assertIsNone(binary_search(array, 6))

    def test_strict(self):
        array = [0, 10, 20, 30, 40]
        self.assertEqual((4, 4), binary_search(array, 40))
        self.assertEqual((2, 2), binary_search(array, 20))
        self.assertEqual((0, 0), binary_search(array, 0))

    def test_several_matches(self):
        self.assertEqual((0, 3), binary_search([0, 0, 0, 0], 0))
        self.assertEqual((0, 3), binary_search([0, 0, 0, 0, 1, 1], 0))
        self.assertEqual((0, 3), binary_search([0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 0))
        self.assertEqual((1, 3), binary_search([0, 1, 1, 1], 1))
        self.assertEqual((5, 7), binary_search([0, 0, 0, 0, 0, 1, 1, 1], 1))
        self.assertEqual((1, 3), binary_search([0, 1, 1, 1, 2, 2, 2, 2, 2, 2], 1))
        self.assertEqual((5, 7), binary_search([0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2], 1))


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

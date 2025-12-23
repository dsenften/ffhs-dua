"""Tests für Boyer-Moore String-Suchalgorithmus.

Diese Tests überprüfen die Korrektheit und Robustheit der Boyer-Moore
Implementierung für verschiedene Szenarien und Edge-Cases.
"""

import pytest

from src.algs4.pva_5_strings.boyer_moore import BoyerMoore


class TestBoyerMooreBasics:
    """Grundlegende Tests für Boyer-Moore Konstruktor und Properties."""

    def test_init_valid_pattern(self):
        """Teste Initialisierung mit gültigem Muster."""
        bm = BoyerMoore("NEEDLE")
        assert bm.pattern == "NEEDLE"

    def test_init_single_char(self):
        """Teste Initialisierung mit einzelnem Zeichen."""
        bm = BoyerMoore("A")
        assert bm.pattern == "A"

    def test_init_none_pattern(self):
        """Teste Initialisierung mit None-Muster."""
        with pytest.raises(ValueError, match="Muster darf nicht None sein"):
            BoyerMoore(None)

    def test_init_empty_pattern(self):
        """Teste Initialisierung mit leerem Muster."""
        with pytest.raises(ValueError, match="Muster darf nicht leer sein"):
            BoyerMoore("")

    def test_pattern_property(self):
        """Teste pattern Property."""
        pattern = "ABRACADABRA"
        bm = BoyerMoore(pattern)
        assert bm.pattern == pattern


class TestBoyerMooreSearch:
    """Tests für die search() Methode."""

    def test_search_found_beginning(self):
        """Teste Suche mit Muster am Anfang."""
        bm = BoyerMoore("HELLO")
        assert bm.search("HELLO WORLD") == 0

    def test_search_found_middle(self):
        """Teste Suche mit Muster in der Mitte."""
        bm = BoyerMoore("WORLD")
        assert bm.search("HELLO WORLD") == 6

    def test_search_found_end(self):
        """Teste Suche mit Muster am Ende."""
        bm = BoyerMoore("END")
        assert bm.search("THIS IS THE END") == 12

    def test_search_not_found(self):
        """Teste Suche mit nicht vorhandenem Muster."""
        bm = BoyerMoore("MISSING")
        text = "HELLO WORLD"
        assert bm.search(text) == len(text)

    def test_search_exact_match(self):
        """
        Verifies that searching a text identical to the pattern returns the index 0.
        """
        bm = BoyerMoore("EXACT")
        assert bm.search("EXACT") == 0

    def test_search_pattern_longer_than_text(self):
        """Teste Suche mit Muster länger als Text."""
        bm = BoyerMoore("TOOLONG")
        text = "SHORT"
        assert bm.search(text) == len(text)

    def test_search_empty_text(self):
        """Teste Suche in leerem Text."""
        bm = BoyerMoore("PATTERN")
        assert bm.search("") == 0

    def test_search_none_text(self):
        """
        Verify that BoyerMoore.search raises a ValueError when called with text set to None.
        
        Raises:
            ValueError: with the message "Text darf nicht None sein".
        """
        bm = BoyerMoore("PATTERN")
        with pytest.raises(ValueError, match="Text darf nicht None sein"):
            bm.search(None)

    def test_search_repeated_pattern(self):
        """Teste Suche mit sich wiederholendem Muster."""
        bm = BoyerMoore("ABAB")
        assert bm.search("ABABAB") == 0

    def test_search_case_sensitive(self):
        """Teste dass Suche case-sensitive ist."""
        bm = BoyerMoore("Hello")
        assert bm.search("HELLO WORLD") == 11  # Nicht gefunden
        assert bm.search("Hello World") == 0  # Gefunden


class TestBoyerMooreSearchAll:
    """Tests für die search_all() Methode."""

    def test_search_all_single_match(self):
        """Teste search_all mit einem Match."""
        bm = BoyerMoore("WORLD")
        matches = list(bm.search_all("HELLO WORLD"))
        assert matches == [6]

    def test_search_all_multiple_matches(self):
        """Teste search_all mit mehreren Matches."""
        bm = BoyerMoore("THE")
        matches = list(bm.search_all("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"))
        assert matches == [0, 31]

    def test_search_all_no_matches(self):
        """Teste search_all ohne Matches."""
        bm = BoyerMoore("MISSING")
        matches = list(bm.search_all("HELLO WORLD"))
        assert matches == []

    def test_search_all_overlapping_pattern(self):
        """Teste search_all mit überlappenden Mustern."""
        bm = BoyerMoore("AA")
        matches = list(bm.search_all("AAAA"))
        assert matches == [0, 1, 2]  # Überlappende Matches

    def test_search_all_empty_text(self):
        """Teste search_all mit leerem Text."""
        bm = BoyerMoore("PATTERN")
        matches = list(bm.search_all(""))
        assert matches == []

    def test_search_all_none_text(self):
        """Teste search_all mit None-Text."""
        bm = BoyerMoore("PATTERN")
        with pytest.raises(ValueError, match="Text darf nicht None sein"):
            list(bm.search_all(None))

    def test_search_all_iterator(self):
        """Teste dass search_all einen Iterator zurückgibt."""
        bm = BoyerMoore("A")
        result = bm.search_all("ABACA")
        assert hasattr(result, "__iter__")
        assert hasattr(result, "__next__")

    def test_search_all_real_world_example(self):
        """Teste search_all mit realem Beispiel."""
        bm = BoyerMoore("sea")
        text = "she sells sea shells by the sea shore"
        matches = list(bm.search_all(text))
        assert matches == [10, 28]


class TestBoyerMooreCount:
    """Tests für die count() Methode."""

    def test_count_no_matches(self):
        """Teste count ohne Matches."""
        bm = BoyerMoore("MISSING")
        assert bm.count("HELLO WORLD") == 0

    def test_count_single_match(self):
        """Teste count mit einem Match."""
        bm = BoyerMoore("WORLD")
        assert bm.count("HELLO WORLD") == 1

    def test_count_multiple_matches(self):
        """Teste count mit mehreren Matches."""
        bm = BoyerMoore("THE")
        assert bm.count("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == 2

    def test_count_overlapping(self):
        """Teste count mit überlappenden Mustern."""
        bm = BoyerMoore("AA")
        assert bm.count("AAAA") == 3

    def test_count_empty_text(self):
        """Teste count mit leerem Text."""
        bm = BoyerMoore("PATTERN")
        assert bm.count("") == 0

    def test_count_none_text(self):
        """Teste count mit None-Text."""
        bm = BoyerMoore("PATTERN")
        with pytest.raises(ValueError, match="Text darf nicht None sein"):
            bm.count(None)

    def test_count_real_world_example(self):
        """Teste count mit realem Beispiel."""
        bm = BoyerMoore("the")
        text = "the quick brown fox jumps over the lazy dog"
        assert bm.count(text) == 2


class TestBoyerMooreRepr:
    """Tests für die __repr__() Methode."""

    def test_repr_format(self):
        """Teste __repr__ Format."""
        bm = BoyerMoore("PATTERN")
        assert repr(bm) == "BoyerMoore(pattern='PATTERN')"

    def test_repr_single_char(self):
        """Teste __repr__ mit einzelnem Zeichen."""
        bm = BoyerMoore("A")
        assert repr(bm) == "BoyerMoore(pattern='A')"

    def test_repr_long_pattern(self):
        """Teste __repr__ mit langem Muster."""
        pattern = "VERYLONGPATTERN"
        bm = BoyerMoore(pattern)
        assert repr(bm) == f"BoyerMoore(pattern='{pattern}')"


class TestBoyerMooreEdgeCases:
    """Tests für Edge-Cases und spezielle Szenarien."""

    def test_whitespace_pattern(self):
        """Teste Muster mit Leerzeichen."""
        bm = BoyerMoore(" ")
        assert bm.search("HELLO WORLD") == 5

    def test_special_characters(self):
        """Teste Muster mit Sonderzeichen."""
        bm = BoyerMoore("@#$")
        assert bm.search("EMAIL@#$DOMAIN") == 5

    def test_newline_in_pattern(self):
        """Teste Muster mit Zeilenwechsel."""
        bm = BoyerMoore("LINE1\nLINE2")
        text = "FIRST LINE1\nLINE2 LAST"
        assert bm.search(text) == 6

    def test_unicode_pattern(self):
        """Teste Muster mit Unicode-Zeichen (innerhalb ASCII-Bereich)."""
        bm = BoyerMoore("café")
        # Nur ASCII-Zeichen funktionieren zuverlässig
        assert bm.search("visit café today") == 6

    def test_unicode_german_text(self):
        """Teste deutsche Umlaute (falls im ASCII-Bereich)."""
        bm = BoyerMoore("test")
        text = "das ist ein test für deutsche texte"
        assert bm.search(text) == 12

    def test_very_long_pattern(self):
        """Teste mit sehr langem Muster (500 Zeichen)."""
        pattern = "a" * 500
        bm = BoyerMoore(pattern)
        text = "b" * 1000 + "a" * 500 + "c" * 1000
        assert bm.search(text) == 1000

    def test_very_long_text(self):
        """Teste mit sehr langem Text (10000 Zeichen)."""
        bm = BoyerMoore("NEEDLE")
        text = "HAY" * 3000 + "NEEDLE" + "STACK" * 1000
        assert bm.search(text) == 9000

    def test_repeated_character_pattern(self):
        """Teste Muster mit wiederholten Zeichen."""
        bm = BoyerMoore("AAAA")
        assert bm.search("BAAAAAAC") == 1

    def test_alternating_pattern(self):
        """Teste alternierendes Muster."""
        bm = BoyerMoore("ABAB")
        assert bm.search("XABABABY") == 1

    def test_pattern_at_multiple_positions(self):
        """Teste Muster an mehreren Positionen."""
        bm = BoyerMoore("AB")
        text = "ABABAB"
        matches = list(bm.search_all(text))
        assert matches == [0, 2, 4]


class TestBoyerMooreAlgorithmCorrectness:
    """Tests für algorithmische Korrektheit."""

    def test_bad_character_table_construction(self):
        """Teste Bad Character Table Konstruktion."""
        bm = BoyerMoore("ABCAB")
        # Teste interne _right Tabelle
        assert bm._right[ord("A")] == 3  # Rechteste Position von 'A'
        assert bm._right[ord("B")] == 4  # Rechteste Position von 'B'
        assert bm._right[ord("C")] == 2  # Rechteste Position von 'C'
        assert bm._right[ord("D")] == -1  # 'D' kommt nicht vor

    def test_boyer_moore_skip_logic(self):
        """Teste Boyer-Moore Skip-Logik."""
        bm = BoyerMoore("NEEDLE")
        # Bei Mismatch sollte der Algorithmus grosse Sprünge machen
        # Dies ist schwer direkt zu testen, aber wir können Korrektheit prüfen
        text = "HAYSTACK WITH NEEDLE IN IT"
        assert bm.search(text) == 14

    def test_boyer_moore_worst_case_pattern(self):
        """Teste Boyer-Moore mit Worst-Case Muster."""
        # Worst-Case: Muster und Text bestehen aus gleichen Zeichen
        bm = BoyerMoore("AAAA")
        text = "A" * 1000
        assert bm.search(text) == 0

    def test_boyer_moore_best_case_pattern(self):
        """Teste Boyer-Moore mit Best-Case Muster."""
        # Best-Case: Muster hat einzigartiges letztes Zeichen
        bm = BoyerMoore("ABCX")
        text = "A" * 1000 + "ABCX"
        assert bm.search(text) == 1000


class TestBoyerMooreIntegration:
    """Integrationstests mit realen Daten."""

    def test_search_in_sentence(self):
        """Teste Suche in normalem Satz."""
        bm = BoyerMoore("quick")
        text = "The quick brown fox jumps over the lazy dog"
        assert bm.search(text) == 4

    def test_search_dna_sequence(self):
        """Teste Suche in DNA-Sequenz."""
        bm = BoyerMoore("ATCG")
        dna = "ATAGATCGCATAGCGCATAGCTAGATGTGCTAGC"
        assert bm.search(dna) == 4

    def test_search_code_pattern(self):
        """Teste Suche in Code-ähnlichem Text."""
        bm = BoyerMoore("def ")
        code = "class MyClass:\n    def method(self):\n        pass"
        assert bm.search(code) == 19

    def test_search_url_pattern(self):
        """Teste Suche in URL."""
        bm = BoyerMoore("https://")
        text = "Visit https://example.com for more info"
        assert bm.search(text) == 6

    def test_find_repeated_words(self):
        """Teste Suche nach wiederholten Wörtern."""
        bm = BoyerMoore("the")
        text = "the cat and the dog and the bird"
        matches = list(bm.search_all(text))
        assert matches == [0, 12, 24]

    def test_case_sensitive_search(self):
        """
        Verify that search_all is case-sensitive: with pattern "Python" and a text containing both "python" and "Python", only the exact-case occurrence is returned (index 18).
        """
        bm = BoyerMoore("Python")
        text = "I love python and Python programming"
        matches = list(bm.search_all(text))
        assert matches == [18]  # Nur "Python", nicht "python"


class TestBoyerMooreTypeSafety:
    """Tests für Type-Safety und Fehlerbehandlung."""

    def test_pattern_must_be_string(self):
        """Teste dass pattern ein String sein muss."""
        with pytest.raises((TypeError, ValueError)):
            BoyerMoore(123)

    def test_text_must_be_string(self):
        """Teste dass text ein String sein muss."""
        bm = BoyerMoore("PATTERN")
        with pytest.raises((TypeError, AttributeError)):
            bm.search(123)

    def test_none_handling_in_all_methods(self):
        """Teste None-Behandlung in allen Methoden."""
        bm = BoyerMoore("PATTERN")

        with pytest.raises(ValueError):
            bm.search(None)

        with pytest.raises(ValueError):
            list(bm.search_all(None))

        with pytest.raises(ValueError):
            bm.count(None)


class TestBoyerMoorePerformance:
    """Performance-Tests (nicht zeitkritisch, nur Korrektheit)."""

    def test_large_text_performance(self):
        """Teste Performance mit grossem Text."""
        bm = BoyerMoore("NEEDLE")
        # 100KB Text
        large_text = "HAY" * 30000 + "NEEDLE" + "STACK" * 5000
        result = bm.search(large_text)
        assert result == 90000  # 30000 * 3 = 90000

    def test_many_matches_performance(self):
        """Teste Performance mit vielen Matches."""
        bm = BoyerMoore("A")
        text = "A" * 10000
        matches = list(bm.search_all(text))
        assert len(matches) == 10000
        assert matches == list(range(10000))

    def test_worst_case_pattern_performance(self):
        """Teste Performance mit Worst-Case Muster."""
        bm = BoyerMoore("AAAB")
        text = "A" * 10000 + "AAAB"
        assert bm.search(text) == 10000
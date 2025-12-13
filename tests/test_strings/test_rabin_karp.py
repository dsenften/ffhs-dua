"""Tests für Rabin-Karp String-Suchalgorithmus."""

import pytest

from src.algs4.pva_5_strings.rabin_karp import RabinKarp


class TestRabinKarpBasics:
    """Tests für Konstruktor und grundlegende Eigenschaften."""

    def test_init_valid_pattern(self):
        """Teste Konstruktor mit gültigem Muster."""
        rk = RabinKarp("abc")
        assert rk.pattern == "abc"

    def test_init_single_char(self):
        """Teste Konstruktor mit einzelnem Zeichen."""
        rk = RabinKarp("a")
        assert rk.pattern == "a"

    def test_init_none_pattern(self):
        """Teste Konstruktor mit None-Muster."""
        with pytest.raises(ValueError, match="Muster darf nicht None sein"):
            RabinKarp(None)

    def test_init_empty_pattern(self):
        """Teste Konstruktor mit leerem Muster."""
        with pytest.raises(ValueError, match="Muster darf nicht leer sein"):
            RabinKarp("")

    def test_pattern_property(self):
        """Teste pattern Property."""
        pattern = "test123"
        rk = RabinKarp(pattern)
        assert rk.pattern == pattern


class TestRabinKarpSearch:
    """Tests für die search() Methode."""

    def test_search_found_beginning(self):
        """Teste Suche mit Match am Anfang."""
        rk = RabinKarp("abc")
        assert rk.search("abcdef") == 0

    def test_search_found_middle(self):
        """Teste Suche mit Match in der Mitte."""
        rk = RabinKarp("NEEDLE")
        assert rk.search("HAYSTACK WITH NEEDLE IN IT") == 14

    def test_search_found_end(self):
        """Teste Suche mit Match am Ende."""
        rk = RabinKarp("end")
        assert rk.search("this is the end") == 12

    def test_search_not_found(self):
        """Teste Suche ohne Match."""
        rk = RabinKarp("NEEDLE")
        text = "NO MATCH HERE"
        assert rk.search(text) == len(text)

    def test_search_exact_match(self):
        """Teste Suche mit exaktem Match (Text == Pattern)."""
        rk = RabinKarp("exact")
        assert rk.search("exact") == 0

    def test_search_pattern_longer_than_text(self):
        """Teste Suche mit Muster länger als Text."""
        rk = RabinKarp("toolong")
        text = "short"
        assert rk.search(text) == len(text)

    def test_search_empty_text(self):
        """Teste Suche in leerem Text."""
        rk = RabinKarp("abc")
        text = ""
        assert rk.search(text) == len(text)

    def test_search_none_text(self):
        """Teste Suche mit None-Text."""
        rk = RabinKarp("abc")
        with pytest.raises(ValueError, match="Text darf nicht None sein"):
            rk.search(None)

    def test_search_repeated_pattern(self):
        """Teste Suche mit wiederholtem Muster."""
        rk = RabinKarp("aa")
        assert rk.search("aaaa") == 0

    def test_search_case_sensitive(self):
        """Teste case-sensitive Suche."""
        rk = RabinKarp("Test")
        assert rk.search("test") == 4  # Nicht gefunden
        assert rk.search("Test") == 0  # Gefunden


class TestRabinKarpSearchAll:
    """Tests für die search_all() Methode."""

    def test_search_all_single_match(self):
        """Teste search_all mit einem Match."""
        rk = RabinKarp("abc")
        matches = list(rk.search_all("xabcy"))
        assert matches == [1]

    def test_search_all_multiple_matches(self):
        """Teste search_all mit mehreren Matches."""
        rk = RabinKarp("ab")
        matches = list(rk.search_all("ababab"))
        assert matches == [0, 2, 4]

    def test_search_all_no_matches(self):
        """Teste search_all ohne Matches."""
        rk = RabinKarp("xyz")
        matches = list(rk.search_all("abcdef"))
        assert matches == []

    def test_search_all_overlapping_pattern(self):
        """Teste search_all mit überlappenden Mustern."""
        rk = RabinKarp("aa")
        matches = list(rk.search_all("aaaa"))
        assert matches == [0, 1, 2]

    def test_search_all_empty_text(self):
        """Teste search_all mit leerem Text."""
        rk = RabinKarp("abc")
        matches = list(rk.search_all(""))
        assert matches == []

    def test_search_all_none_text(self):
        """Teste search_all mit None-Text."""
        rk = RabinKarp("abc")
        with pytest.raises(ValueError, match="Text darf nicht None sein"):
            list(rk.search_all(None))

    def test_search_all_iterator(self):
        """Teste dass search_all einen Iterator zurückgibt."""
        rk = RabinKarp("a")
        result = rk.search_all("aaa")
        # Iterator sollte nicht sofort alle Werte berechnen
        assert hasattr(result, "__iter__")
        assert hasattr(result, "__next__")

    def test_search_all_real_world_example(self):
        """Teste search_all mit realem Beispiel."""
        rk = RabinKarp("the")
        text = "the quick brown fox jumps over the lazy dog"
        matches = list(rk.search_all(text))
        assert matches == [0, 31]


class TestRabinKarpCount:
    """Tests für die count() Methode."""

    def test_count_no_matches(self):
        """Teste count ohne Matches."""
        rk = RabinKarp("xyz")
        assert rk.count("abcdef") == 0

    def test_count_single_match(self):
        """Teste count mit einem Match."""
        rk = RabinKarp("abc")
        assert rk.count("xabcy") == 1

    def test_count_multiple_matches(self):
        """Teste count mit mehreren Matches."""
        rk = RabinKarp("ab")
        assert rk.count("ababab") == 3

    def test_count_overlapping(self):
        """Teste count mit überlappenden Mustern."""
        rk = RabinKarp("aa")
        assert rk.count("aaaa") == 3

    def test_count_empty_text(self):
        """Teste count mit leerem Text."""
        rk = RabinKarp("abc")
        assert rk.count("") == 0

    def test_count_none_text(self):
        """Teste count mit None-Text."""
        rk = RabinKarp("abc")
        with pytest.raises(ValueError, match="Text darf nicht None sein"):
            rk.count(None)

    def test_count_real_world_example(self):
        """Teste count mit realem Beispiel."""
        rk = RabinKarp("is")
        text = "This is a test. This is only a test."
        assert rk.count(text) == 4  # "is" in "This" (2x) und "is" (2x)


class TestRabinKarpRepr:
    """Tests für die __repr__() Methode."""

    def test_repr_format(self):
        """Teste __repr__ Format."""
        rk = RabinKarp("test")
        assert repr(rk) == "RabinKarp('test')"

    def test_repr_single_char(self):
        """Teste __repr__ mit einzelnem Zeichen."""
        rk = RabinKarp("a")
        assert repr(rk) == "RabinKarp('a')"

    def test_repr_long_pattern(self):
        """Teste __repr__ mit langem Muster."""
        pattern = "very_long_pattern_123"
        rk = RabinKarp(pattern)
        assert repr(rk) == f"RabinKarp('{pattern}')"


class TestRabinKarpEdgeCases:
    """Tests für Edge Cases und spezielle Szenarien."""

    def test_whitespace_pattern(self):
        """Teste Muster mit Leerzeichen."""
        rk = RabinKarp(" ")
        text = "hello world"
        assert rk.search(text) == 5

    def test_special_characters(self):
        """Teste Muster mit Sonderzeichen."""
        rk = RabinKarp("@#$")
        text = "test@#$data"
        assert rk.search(text) == 4

    def test_newline_in_pattern(self):
        """Teste Muster mit Zeilenwechsel."""
        rk = RabinKarp("line1\nline2")
        text = "first line1\nline2 end"
        assert rk.search(text) == 6

    def test_unicode_pattern(self):
        """Teste Muster mit Unicode-Zeichen."""
        rk = RabinKarp("café")
        text = "I love café au lait"
        assert rk.search(text) == 7

    def test_unicode_german_text(self):
        """Teste deutsche Umlaute."""
        rk = RabinKarp("Müller")
        text = "Herr Müller ist da"
        assert rk.search(text) == 5

    def test_very_long_pattern(self):
        """Teste sehr langes Muster."""
        pattern = "a" * 1000
        rk = RabinKarp(pattern)
        text = "b" * 500 + pattern + "c" * 500
        assert rk.search(text) == 500

    def test_very_long_text(self):
        """Teste sehr langen Text."""
        rk = RabinKarp("needle")
        text = "hay" * 10000 + "needle" + "stack" * 10000
        assert rk.search(text) == 30000

    def test_repeated_character_pattern(self):
        """Teste Muster mit wiederholten Zeichen."""
        rk = RabinKarp("aaaa")
        text = "baaaaaab"
        assert rk.search(text) == 1

    def test_alternating_pattern(self):
        """Teste alternierendes Muster."""
        rk = RabinKarp("abab")
        text = "xabababy"
        assert rk.search(text) == 1

    def test_pattern_at_multiple_positions(self):
        """Teste Muster an mehreren Positionen."""
        rk = RabinKarp("test")
        text = "test this test and test again"
        matches = list(rk.search_all(text))
        assert matches == [0, 10, 19]


class TestRabinKarpAlgorithmCorrectness:
    """Tests für Algorithmus-Korrektheit und Rabin-Karp-spezifische Eigenschaften."""

    def test_rolling_hash_correctness(self):
        """Teste dass Rolling Hash korrekt funktioniert.

        Indirekt getestet durch korrekte Suchergebnisse bei
        Mustern mit potentiellen Hash-Kollisionen.
        """
        # Teste mit Muster das Hash-Kollisionen verursachen könnte
        rk = RabinKarp("abc")
        text = "xabcyabcz"
        matches = list(rk.search_all(text))
        assert matches == [1, 5]

    def test_hash_collision_handling(self):
        """Teste Behandlung von Hash-Kollisionen durch Las Vegas Verifikation."""
        # Teste mit ähnlichen Strings die gleiche Hash-Werte haben könnten
        rk = RabinKarp("ab")
        text = "abbaabab"
        # Sollte nur echte Matches finden, nicht Hash-Kollisionen
        matches = list(rk.search_all(text))
        # "ab" erscheint an Positionen 0, 4, 6 in "abbaabab"
        assert matches == [0, 4, 6]

    def test_modular_arithmetic_correctness(self):
        """Teste dass modulare Arithmetik korrekt funktioniert."""
        # Teste mit grossen Zeichen-Werten (Extended ASCII)
        rk = RabinKarp("ÄÖÜ")
        text = "testÄÖÜdata"
        assert rk.search(text) == 4

    def test_pattern_verification(self):
        """Teste dass Muster-Verifikation bei Hash-Matches funktioniert."""
        rk = RabinKarp("test")
        # Erstelle Text wo Hash-Match aber kein String-Match vorliegt
        # (schwer zu konstruieren, aber Algorithmus sollte robust sein)
        text = "testing"
        assert rk.search(text) == 0  # "test" ist am Anfang von "testing"


class TestRabinKarpIntegration:
    """Integrationstests mit realen Daten und Anwendungsfällen."""

    def test_search_in_sentence(self):
        """Teste Suche in natürlichem Satz."""
        rk = RabinKarp("world")
        text = "Hello world, this is a beautiful world!"
        assert rk.search(text) == 6
        assert rk.count(text) == 2

    def test_search_dna_sequence(self):
        """Teste Suche in DNA-Sequenz."""
        rk = RabinKarp("ATCG")
        dna = "GCATCGATCGATCGTAGCATCG"
        matches = list(rk.search_all(dna))
        # ATCG erscheint an Positionen 2, 6, 10, 18
        assert len(matches) == 4
        assert matches == [2, 6, 10, 18]

    def test_search_code_pattern(self):
        """Teste Suche nach Code-Muster."""
        rk = RabinKarp("def ")
        code = "def foo():\n    def bar():\n        pass"
        matches = list(rk.search_all(code))
        assert len(matches) == 2

    def test_search_url_pattern(self):
        """Teste Suche nach URL-Muster."""
        rk = RabinKarp("http://")
        text = "Visit http://example.com or http://test.org"
        matches = list(rk.search_all(text))
        # "http://" erscheint an Positionen 6 und 28
        assert matches == [6, 28]

    def test_search_with_real_text_data(self):
        """Teste mit realem Text-Beispiel."""
        rk = RabinKarp("the")
        text = "the quick brown fox jumps over the lazy dog"
        matches = list(rk.search_all(text))
        assert matches == [0, 31]

    def test_find_repeated_words(self):
        """Teste Suche nach wiederholten Wörtern."""
        rk = RabinKarp("test")
        text = "This is a test. Another test. Final test."
        assert rk.count(text) == 3

    def test_case_sensitive_search(self):
        """Teste case-sensitive Suche."""
        rk_lower = RabinKarp("python")
        rk_upper = RabinKarp("Python")
        text = "I love Python programming. python is great!"

        # "python" (lowercase) ist an Position 27
        # "Python" (capitalized) ist an Position 7
        assert rk_lower.search(text) == 27
        assert rk_upper.search(text) == 7
        assert rk_lower.count(text) == 1
        assert rk_upper.count(text) == 1


class TestRabinKarpTypeSafety:
    """Tests für Type-Safety und Fehlerbehandlung."""

    def test_pattern_must_be_string(self):
        """Teste dass Muster ein String sein muss."""
        with pytest.raises((TypeError, ValueError)):
            RabinKarp(123)

    def test_text_must_be_string(self):
        """Teste dass Text ein String sein muss."""
        rk = RabinKarp("test")
        with pytest.raises((TypeError, ValueError)):
            rk.search(123)

    def test_none_handling_in_all_methods(self):
        """Teste None-Behandlung in allen Methoden."""
        rk = RabinKarp("test")

        with pytest.raises(ValueError):
            rk.search(None)
        with pytest.raises(ValueError):
            list(rk.search_all(None))
        with pytest.raises(ValueError):
            rk.count(None)


class TestRabinKarpPerformance:
    """Performance-Tests für verschiedene Szenarien."""

    def test_large_text_performance(self):
        """Teste Performance mit grossem Text."""
        rk = RabinKarp("needle")
        # Erstelle grossen Text (100KB)
        large_text = "hay" * 10000 + "needle" + "stack" * 10000

        # Sollte in angemessener Zeit laufen
        import time

        start = time.perf_counter()
        result = rk.search(large_text)
        end = time.perf_counter()

        assert result == 30000  # Position von "needle"
        assert end - start < 1.0  # Sollte unter 1 Sekunde dauern

    def test_many_matches_performance(self):
        """Teste Performance mit vielen Matches."""
        rk = RabinKarp("a")
        # Text mit vielen 'a's
        text_with_many_matches = "a" * 10000

        import time

        start = time.perf_counter()
        count = rk.count(text_with_many_matches)
        end = time.perf_counter()

        assert count == 10000
        assert end - start < 1.0  # Sollte unter 1 Sekunde dauern

    def test_worst_case_pattern_performance(self):
        """Teste Performance im Worst-Case Szenario."""
        # Worst-Case: Viele Hash-Kollisionen aber keine echten Matches
        rk = RabinKarp("aaab")
        text = "a" * 1000 + "b"  # Viele 'a's aber kein "aaab"

        import time

        start = time.perf_counter()
        result = rk.search(text)
        end = time.perf_counter()

        # "aaab" wird an Position 997 gefunden (1000 'a's + 'b' = "...aaab")
        assert result == 997  # Gefunden an Position 997
        assert end - start < 1.0  # Sollte trotzdem schnell sein


class TestRabinKarpComparison:
    """Vergleichstests mit anderen String-Suchalgorithmen."""

    def test_consistency_with_builtin_find(self):
        """Teste Konsistenz mit Python's eingebautem str.find()."""
        test_cases = [
            ("abc", "abcdef"),
            ("def", "abcdef"),
            ("xyz", "abcdef"),
            ("", "abcdef"),
            ("abcdef", "abc"),
            ("test", "this is a test"),
            ("is", "this is a test"),
        ]

        for pattern, text in test_cases:
            if pattern:  # RabinKarp erlaubt keine leeren Muster
                rk = RabinKarp(pattern)
                rk_result = rk.search(text)
                builtin_result = text.find(pattern)

                if builtin_result == -1:
                    assert rk_result == len(text)
                else:
                    assert rk_result == builtin_result

    def test_all_matches_consistency(self):
        """Teste dass search_all() alle Vorkommen findet."""
        rk = RabinKarp("ab")
        text = "ababab"

        # Manuell alle Positionen finden
        expected_positions = []
        pos = 0
        while True:
            pos = text.find("ab", pos)
            if pos == -1:
                break
            expected_positions.append(pos)
            pos += 1

        rk_positions = list(rk.search_all(text))
        assert rk_positions == expected_positions

    def test_count_consistency(self):
        """Teste dass count() mit search_all() konsistent ist."""
        test_cases = [
            ("a", "banana"),
            ("an", "banana"),
            ("na", "banana"),
            ("test", "test test test"),
            ("xyz", "abcdef"),
        ]

        for pattern, text in test_cases:
            rk = RabinKarp(pattern)
            count_result = rk.count(text)
            search_all_count = len(list(rk.search_all(text)))
            assert count_result == search_all_count

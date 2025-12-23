"""Tests für KMP String-Suchalgorithmus.

Diese Testsuite deckt alle Funktionen des KMP-Algorithmus ab:
- Konstruktor und Pattern-Property
- Einfache Suche mit search()
- Mehrfachsuche mit search_all()
- Zählfunktion mit count()
- Edge Cases und Fehlerbehandlung
"""

import pytest

from src.algs4.pva_5_strings.kmp import KMP


class TestKMPBasics:
    """Tests für grundlegende KMP-Funktionalität."""

    def test_init_valid_pattern(self):
        """Teste Initialisierung mit gültigem Muster."""
        kmp = KMP("NEEDLE")
        assert kmp.pattern == "NEEDLE"

    def test_init_single_char(self):
        """Teste Initialisierung mit einzelnem Zeichen."""
        kmp = KMP("A")
        assert kmp.pattern == "A"

    def test_init_none_pattern(self):
        """Teste Initialisierung mit None als Muster."""
        with pytest.raises(ValueError, match="Muster darf nicht None sein"):
            KMP(None)

    def test_init_empty_pattern(self):
        """Teste Initialisierung mit leerem Muster."""
        with pytest.raises(ValueError, match="Muster darf nicht leer sein"):
            KMP("")

    def test_pattern_property(self):
        """Teste Pattern-Property Accessor."""
        kmp = KMP("test")
        assert kmp.pattern == "test"
        # Pattern sollte read-only sein (kein Setter)
        assert hasattr(type(kmp).pattern, "fget")
        assert type(kmp).pattern.fset is None


class TestKMPSearch:
    """Tests für die search() Methode."""

    def test_search_found_beginning(self):
        """Teste Suche mit Match am Anfang."""
        kmp = KMP("abc")
        assert kmp.search("abcdef") == 0

    def test_search_found_middle(self):
        """Teste Suche mit Match in der Mitte."""
        kmp = KMP("NEEDLE")
        assert kmp.search("HAYSTACK WITH NEEDLE IN IT") == 14

    def test_search_found_end(self):
        """Teste Suche mit Match am Ende."""
        kmp = KMP("end")
        assert kmp.search("this is the end") == 12

    def test_search_not_found(self):
        """Teste Suche ohne Match."""
        kmp = KMP("NEEDLE")
        text = "NO MATCH HERE"
        assert kmp.search(text) == len(text)

    def test_search_exact_match(self):
        """Teste Suche mit exaktem Match (Text == Pattern)."""
        kmp = KMP("exact")
        assert kmp.search("exact") == 0

    def test_search_pattern_longer_than_text(self):
        """Teste Suche mit Muster länger als Text."""
        kmp = KMP("very long pattern")
        text = "short"
        assert kmp.search(text) == len(text)

    def test_search_empty_text(self):
        """Teste Suche in leerem Text."""
        kmp = KMP("abc")
        assert kmp.search("") == 0

    def test_search_none_text(self):
        """Teste Suche mit None als Text."""
        kmp = KMP("abc")
        with pytest.raises(ValueError, match="Text darf nicht None sein"):
            kmp.search(None)

    def test_search_repeated_pattern(self):
        """Teste Suche mit wiederholtem Muster."""
        kmp = KMP("aa")
        assert kmp.search("aaaa") == 0

    def test_search_case_sensitive(self):
        """Teste dass Suche case-sensitive ist."""
        kmp = KMP("ABC")
        text = "abc ABC"
        assert kmp.search(text) == 4  # Findet nur "ABC", nicht "abc"


class TestKMPSearchAll:
    """Tests für die search_all() Methode."""

    def test_search_all_single_match(self):
        """Teste search_all mit einem Match."""
        kmp = KMP("abc")
        matches = list(kmp.search_all("xyzabcdef"))
        assert matches == [3]

    def test_search_all_multiple_matches(self):
        """Teste search_all mit mehreren Matches."""
        kmp = KMP("ab")
        matches = list(kmp.search_all("ababab"))
        assert matches == [0, 2, 4]

    def test_search_all_no_matches(self):
        """Teste search_all ohne Matches."""
        kmp = KMP("xyz")
        matches = list(kmp.search_all("abcdefgh"))
        assert matches == []

    def test_search_all_overlapping_pattern(self):
        """Teste search_all mit überlappenden Vorkommen.

        Die Implementierung findet überlappende Vorkommen durch
        Weiterrücken um 1 nach jedem Fund.
        In "aaaa" findet "aa" an Positionen 0, 1, 2 (nicht 3, da
        ab Position 3 nur noch 1 Zeichen übrig ist).
        """
        kmp = KMP("aa")
        matches = list(kmp.search_all("aaaa"))
        # Findet an Position 0, 1, 2
        assert matches == [0, 1, 2]

    def test_search_all_empty_text(self):
        """Teste search_all mit leerem Text."""
        kmp = KMP("abc")
        matches = list(kmp.search_all(""))
        assert matches == []

    def test_search_all_none_text(self):
        """Teste search_all mit None als Text."""
        kmp = KMP("abc")
        with pytest.raises(ValueError, match="Text darf nicht None sein"):
            list(kmp.search_all(None))

    def test_search_all_iterator(self):
        """Teste dass search_all einen Iterator zurückgibt."""
        kmp = KMP("ab")
        result = kmp.search_all("ababab")
        # Sollte ein Iterator sein, nicht eine Liste
        assert hasattr(result, "__iter__")
        assert hasattr(result, "__next__")

    def test_search_all_real_world_example(self):
        """Teste search_all mit realem Beispiel."""
        kmp = KMP("abra")
        text = "abacadabrabracabracadabrabrabracad"
        matches = list(kmp.search_all(text))
        # "abra" erscheint an Positionen 6, 9, 14, 21, 24, 27
        # (überlappende Vorkommen werden durch pos+1 gefunden)
        assert matches == [6, 9, 14, 21, 24, 27]


class TestKMPCount:
    """Tests für die count() Methode."""

    def test_count_no_matches(self):
        """Teste count ohne Matches."""
        kmp = KMP("xyz")
        assert kmp.count("abcdefgh") == 0

    def test_count_single_match(self):
        """Teste count mit einem Match."""
        kmp = KMP("abc")
        assert kmp.count("xyzabcdef") == 1

    def test_count_multiple_matches(self):
        """Teste count mit mehreren Matches."""
        kmp = KMP("ab")
        assert kmp.count("ababab") == 3

    def test_count_overlapping(self):
        """Teste count mit überlappenden Vorkommen."""
        kmp = KMP("aa")
        # In "aaaa" findet "aa" an Positionen 0, 1, 2
        assert kmp.count("aaaa") == 3

    def test_count_empty_text(self):
        """Teste count mit leerem Text."""
        kmp = KMP("abc")
        assert kmp.count("") == 0

    def test_count_none_text(self):
        """Teste count mit None als Text."""
        kmp = KMP("abc")
        with pytest.raises(ValueError, match="Text darf nicht None sein"):
            kmp.count(None)

    def test_count_real_world_example(self):
        """Teste count mit realem Beispiel."""
        kmp = KMP("abra")
        text = "abacadabrabracabracadabrabrabracad"
        # "abra" erscheint 6 mal (inkl. überlappende Vorkommen)
        assert kmp.count(text) == 6


class TestKMPRepr:
    """Tests für __repr__ Methode."""

    def test_repr_format(self):
        """Teste Format der String-Repräsentation."""
        kmp = KMP("test")
        assert repr(kmp) == "KMP(pattern='test')"

    def test_repr_single_char(self):
        """Teste repr mit einzelnem Zeichen."""
        kmp = KMP("A")
        assert repr(kmp) == "KMP(pattern='A')"

    def test_repr_long_pattern(self):
        """Teste repr mit langem Muster."""
        kmp = KMP("this is a very long pattern")
        assert repr(kmp) == "KMP(pattern='this is a very long pattern')"


class TestKMPEdgeCases:
    """Tests für Edge Cases und Spezialfälle."""

    def test_whitespace_pattern(self):
        """Teste Muster mit Leerzeichen."""
        kmp = KMP("hello world")
        assert kmp.search("say hello world today") == 4

    def test_special_characters(self):
        """Teste Muster mit Sonderzeichen."""
        kmp = KMP("a.b*c")
        assert kmp.search("test a.b*c here") == 5

    def test_newline_in_pattern(self):
        """Teste Muster mit Zeilenumbruch."""
        kmp = KMP("line1\nline2")
        assert kmp.search("text line1\nline2 more") == 5

    def test_unicode_pattern(self):
        """Teste Muster mit Unicode-Zeichen."""
        kmp = KMP("Ü")
        assert kmp.search("ÜBER") == 0

    def test_unicode_german_text(self):
        """Teste deutsche Umlaute."""
        kmp = KMP("München")
        assert kmp.search("Ich wohne in München") == 13

    def test_emoji_pattern(self):
        """Teste Muster mit Emoji.

        KMP verwendet eine 256-Element DFA-Tabelle für Extended ASCII.
        Unicode-Zeichen mit ord() > 255 (wie Emojis) führen zu einem
        IndexError. Dies ist eine bekannte Limitierung der Implementierung.
        """
        with pytest.raises(IndexError):
            KMP("😀")  # ord('😀') = 128512, > 255

    def test_very_long_pattern(self):
        """Teste mit sehr langem Muster (500 Zeichen)."""
        pattern = "a" * 500
        kmp = KMP(pattern)
        text = "b" * 1000 + "a" * 500 + "c" * 1000
        assert kmp.search(text) == 1000

    def test_very_long_text(self):
        """Teste mit sehr langem Text."""
        kmp = KMP("target")
        text = "x" * 100000 + "target" + "y" * 100000
        assert kmp.search(text) == 100000
        assert kmp.count(text) == 1

    def test_repeated_character_pattern(self):
        """Teste Muster mit wiederholten Zeichen."""
        kmp = KMP("aaaa")
        assert kmp.search("bbbaaaabbb") == 3

    def test_alternating_pattern(self):
        """Teste alternierendes Muster."""
        kmp = KMP("ababab")
        assert kmp.search("xyzabababxyz") == 3

    def test_pattern_at_multiple_positions(self):
        """Teste Muster an mehreren Positionen."""
        kmp = KMP("abc")
        text = "abc xyz abc 123 abc"
        matches = list(kmp.search_all(text))
        assert matches == [0, 8, 16]
        assert kmp.count(text) == 3


class TestKMPAlgorithmCorrectness:
    """Tests für Algorithmus-Korrektheit und KMP-spezifische Eigenschaften."""

    def test_kmp_dfa_construction(self):
        """Teste dass DFA korrekt konstruiert wird.

        Indirekt getestet durch korrekte Suchergebnisse bei
        Mustern mit selbst-überlappenden Präfixen.
        """
        # Muster mit Präfix-Überlappung: "ABABAC"
        # Bei Mismatch nach "ABABA" sollte KMP zu Position 3 zurückspringen
        kmp = KMP("ABABAC")
        text = "ABABABABAC"
        # Sollte an Position 4 finden (nicht am Anfang wegen Mismatch)
        assert kmp.search(text) == 4

    def test_kmp_no_backtracking_in_text(self):
        """Teste dass KMP nicht im Text zurückgeht.

        Dies ist eine Kerneigenschaft von KMP: Der Text-Index
        läuft nur vorwärts. Dies wird indirekt durch korrekte
        Ergebnisse bei komplexen Mustern bestätigt.
        """
        kmp = KMP("abracadabra")
        text = "abacadabrabracabracadabrabrabracad"
        assert kmp.search(text) == 14

    def test_kmp_linear_time(self):
        """Teste dass KMP in linearer Zeit läuft.

        Worst-Case für naive Algorithmen: Wiederholte Zeichen.
        KMP sollte trotzdem effizient sein.
        """
        kmp = KMP("a" * 100)
        text = "b" * 10000 + "a" * 100 + "b" * 10000
        # Sollte schnell finden, auch bei 20100 Zeichen
        assert kmp.search(text) == 10000

    def test_kmp_worst_case_pattern(self):
        """Teste KMP Worst-Case Muster.

        Muster wie "aaab" in Text "aaaaaaaaab" sind worst-case
        für naive Algorithmen, aber nicht für KMP.
        """
        kmp = KMP("aaab")
        text = "aaaaaaaaab"
        assert kmp.search(text) == 6

    def test_kmp_prefix_function(self):
        """Teste dass KMP-Präfix-Funktion korrekt arbeitet.

        Bei Muster "ABABC" sollte ein Mismatch nach "ABAB"
        zu Position 2 zurückspringen (nicht zu 0).
        """
        kmp = KMP("ABABC")
        # Text hat "ABABA", dann Mismatch, dann "ABABC"
        text = "ABABABC"
        assert kmp.search(text) == 2


class TestKMPIntegration:
    """Integrationstests mit realen Daten und Anwendungsfällen."""

    def test_search_in_sentence(self):
        """Teste Suche in natürlichem Satz."""
        kmp = KMP("world")
        text = "Hello world, this is a beautiful world!"
        assert kmp.search(text) == 6
        assert kmp.count(text) == 2

    def test_search_dna_sequence(self):
        """Teste Suche in DNA-Sequenz."""
        kmp = KMP("ATCG")
        dna = "GCATCGATCGATCGTAGCATCG"
        matches = list(kmp.search_all(dna))
        # ATCG erscheint an Positionen 2, 6, 10, 18
        assert len(matches) == 4
        assert matches == [2, 6, 10, 18]

    def test_search_code_pattern(self):
        """Teste Suche nach Code-Muster."""
        kmp = KMP("def ")
        code = "def foo():\n    def bar():\n        pass"
        matches = list(kmp.search_all(code))
        assert len(matches) == 2

    def test_search_url_pattern(self):
        """Teste Suche nach URL-Muster."""
        kmp = KMP("http://")
        text = "Visit http://example.com or http://test.org"
        matches = list(kmp.search_all(text))
        # "http://" erscheint an Positionen 6 und 28
        assert matches == [6, 28]

    def test_search_with_real_text_data(self):
        """Teste mit realem Text-Beispiel."""
        kmp = KMP("the")
        text = "the quick brown fox jumps over the lazy dog"
        matches = list(kmp.search_all(text))
        assert matches == [0, 31]

    def test_find_repeated_words(self):
        """Teste Suche nach wiederholten Wörtern."""
        kmp = KMP("test")
        text = "This is a test. Another test. Final test."
        assert kmp.count(text) == 3

    def test_case_sensitive_search(self):
        """Teste case-sensitive Suche."""
        kmp_lower = KMP("python")
        kmp_upper = KMP("Python")
        text = "I love Python programming. python is great!"

        # "python" (lowercase) ist an Position 27
        # "Python" (capitalized) ist an Position 7
        assert kmp_lower.search(text) == 27
        assert kmp_upper.search(text) == 7
        assert kmp_lower.count(text) == 1
        assert kmp_upper.count(text) == 1


class TestKMPTypeSafety:
    """Tests für Type-Safety und Fehlerbehandlung."""

    def test_pattern_must_be_string(self):
        """Teste dass Muster ein String sein muss."""
        # Python's Type-Hints würden dies zur Compile-Zeit erkennen,
        # aber wir testen das Runtime-Verhalten
        with pytest.raises((TypeError, AttributeError)):
            kmp = KMP(123)
            kmp.search("test")

    def test_text_must_be_string(self):
        """Teste dass Text ein String sein muss."""
        kmp = KMP("test")
        with pytest.raises((TypeError, AttributeError)):
            kmp.search(123)

    def test_none_handling_in_all_methods(self):
        """Teste None-Handling in allen Methoden."""
        kmp = KMP("test")

        with pytest.raises(ValueError):
            kmp.search(None)

        with pytest.raises(ValueError):
            list(kmp.search_all(None))

        with pytest.raises(ValueError):
            kmp.count(None)


class TestKMPPerformance:
    """Performance-Tests für KMP-Algorithmus."""

    @pytest.mark.slow
    def test_large_text_performance(self):
        """Teste Performance mit sehr grossem Text.

        KMP sollte auch bei grossen Texten effizient sein.
        """
        kmp = KMP("pattern")
        # 1 Million Zeichen
        text = "x" * 500000 + "pattern" + "y" * 500000
        assert kmp.search(text) == 500000

    @pytest.mark.slow
    def test_many_matches_performance(self):
        """Teste Performance mit vielen Matches.

        search_all sollte auch bei vielen Matches effizient sein.
        """
        kmp = KMP("ab")
        # Text mit 50000 "ab" Vorkommen
        text = "ab" * 50000
        matches = list(kmp.search_all(text))
        assert len(matches) == 50000

    @pytest.mark.slow
    def test_worst_case_pattern_performance(self):
        """Teste Performance mit Worst-Case Muster.

        Muster mit vielen Wiederholungen sollte KMP
        nicht verlangsamen.
        """
        kmp = KMP("a" * 1000)
        text = "b" * 100000 + "a" * 1000 + "c" * 100000
        assert kmp.search(text) == 100000

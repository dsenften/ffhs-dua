"""Tests für Hash Tables (Separate Chaining und Linear Probing)."""

import pytest

from src.algs4.pva_3_searching.hashing import (
    LinearProbingHashST,
    SeparateChainingHashST,
)


class TestSeparateChainingHashST:
    """Tests für SeparateChainingHashST."""

    def test_empty_table(self) -> None:
        """Test: Leere Hash-Tabelle."""
        st = SeparateChainingHashST[str, int]()
        assert st.is_empty()
        assert st.size() == 0
        assert st.get("A") is None
        assert not st.contains("A")

    def test_put_and_get(self) -> None:
        """Test: Einfügen und Abrufen von Elementen."""
        st = SeparateChainingHashST[str, int]()

        st.put("S", 0)
        st.put("E", 1)
        st.put("A", 2)

        assert st.size() == 3
        assert st.get("S") == 0
        assert st.get("E") == 1
        assert st.get("A") == 2
        assert st.contains("S")
        assert st.contains("E")
        assert st.contains("A")

    def test_put_update(self) -> None:
        """Test: Aktualisieren eines vorhandenen Schlüssels."""
        st = SeparateChainingHashST[str, int]()

        st.put("A", 1)
        assert st.get("A") == 1

        st.put("A", 2)
        assert st.get("A") == 2
        assert st.size() == 1

    def test_delete(self) -> None:
        """Test: Löschen von Elementen."""
        st = SeparateChainingHashST[str, int]()

        st.put("S", 0)
        st.put("E", 1)
        st.put("A", 2)

        st.delete("E")
        assert st.size() == 2
        assert not st.contains("E")
        assert st.get("E") is None
        assert st.contains("S")
        assert st.contains("A")

    def test_delete_nonexistent(self) -> None:
        """Test: Löschen eines nicht vorhandenen Schlüssels."""
        st = SeparateChainingHashST[str, int]()

        st.put("A", 1)
        st.delete("B")
        assert st.size() == 1
        assert st.contains("A")

    def test_put_none_value_deletes(self) -> None:
        """Test: Einfügen von None als Wert löscht den Schlüssel."""
        st = SeparateChainingHashST[str, int]()

        st.put("A", 1)
        assert st.contains("A")

        st.put("A", None)  # type: ignore
        assert not st.contains("A")
        assert st.size() == 0

    def test_keys(self) -> None:
        """Test: Iteration über alle Schlüssel."""
        st = SeparateChainingHashST[str, int]()

        st.put("S", 0)
        st.put("E", 1)
        st.put("A", 2)

        keys = set(st.keys())
        assert keys == {"S", "E", "A"}

    def test_none_key_raises_error(self) -> None:
        """Test: None als Schlüssel wirft ValueError."""
        st = SeparateChainingHashST[str, int]()

        with pytest.raises(ValueError, match="key cannot be None"):
            st.put(None, 1)  # type: ignore

        with pytest.raises(ValueError, match="key cannot be None"):
            st.get(None)  # type: ignore

        with pytest.raises(ValueError, match="key cannot be None"):
            st.delete(None)  # type: ignore

        with pytest.raises(ValueError, match="key cannot be None"):
            st.contains(None)  # type: ignore

    def test_resize_grow(self) -> None:
        """Test: Automatisches Vergrössern der Tabelle."""
        st = SeparateChainingHashST[str, int](capacity=4)

        # Füge genug Elemente ein, um ein Resize auszulösen
        for i in range(50):
            st.put(f"key{i}", i)

        assert st.size() == 50
        for i in range(50):
            assert st.get(f"key{i}") == i

    def test_resize_shrink(self) -> None:
        """Test: Automatisches Verkleinern der Tabelle."""
        st = SeparateChainingHashST[str, int]()

        # Füge Elemente ein
        for i in range(50):
            st.put(f"key{i}", i)

        # Lösche die meisten Elemente
        for i in range(45):
            st.delete(f"key{i}")

        assert st.size() == 5
        for i in range(45, 50):
            assert st.get(f"key{i}") == i

    def test_collision_handling(self) -> None:
        """Test: Korrekte Behandlung von Kollisionen."""
        st = SeparateChainingHashST[str, int](capacity=1)

        # Alle Schlüssel landen im selben Bucket
        st.put("A", 1)
        st.put("B", 2)
        st.put("C", 3)

        assert st.size() == 3
        assert st.get("A") == 1
        assert st.get("B") == 2
        assert st.get("C") == 3


class TestLinearProbingHashST:
    """Tests für LinearProbingHashST."""

    def test_empty_table(self) -> None:
        """Test: Leere Hash-Tabelle."""
        st = LinearProbingHashST[str, int]()
        assert st.is_empty()
        assert st.size() == 0
        assert st.get("A") is None
        assert not st.contains("A")

    def test_put_and_get(self) -> None:
        """Test: Einfügen und Abrufen von Elementen."""
        st = LinearProbingHashST[str, int]()

        st.put("S", 0)
        st.put("E", 1)
        st.put("A", 2)

        assert st.size() == 3
        assert st.get("S") == 0
        assert st.get("E") == 1
        assert st.get("A") == 2
        assert st.contains("S")
        assert st.contains("E")
        assert st.contains("A")

    def test_put_update(self) -> None:
        """Test: Aktualisieren eines vorhandenen Schlüssels."""
        st = LinearProbingHashST[str, int]()

        st.put("A", 1)
        assert st.get("A") == 1

        st.put("A", 2)
        assert st.get("A") == 2
        assert st.size() == 1

    def test_delete(self) -> None:
        """Test: Löschen von Elementen."""
        st = LinearProbingHashST[str, int]()

        st.put("S", 0)
        st.put("E", 1)
        st.put("A", 2)

        st.delete("E")
        assert st.size() == 2
        assert not st.contains("E")
        assert st.get("E") is None
        assert st.contains("S")
        assert st.contains("A")

    def test_delete_nonexistent(self) -> None:
        """Test: Löschen eines nicht vorhandenen Schlüssels."""
        st = LinearProbingHashST[str, int]()

        st.put("A", 1)
        st.delete("B")
        assert st.size() == 1
        assert st.contains("A")

    def test_put_none_value_deletes(self) -> None:
        """Test: Einfügen von None als Wert löscht den Schlüssel."""
        st = LinearProbingHashST[str, int]()

        st.put("A", 1)
        assert st.contains("A")

        st.put("A", None)  # type: ignore
        assert not st.contains("A")
        assert st.size() == 0

    def test_keys(self) -> None:
        """Test: Iteration über alle Schlüssel."""
        st = LinearProbingHashST[str, int]()

        st.put("S", 0)
        st.put("E", 1)
        st.put("A", 2)

        keys = set(st.keys())
        assert keys == {"S", "E", "A"}

    def test_none_key_raises_error(self) -> None:
        """Test: None als Schlüssel wirft ValueError."""
        st = LinearProbingHashST[str, int]()

        with pytest.raises(ValueError, match="key cannot be None"):
            st.put(None, 1)  # type: ignore

        with pytest.raises(ValueError, match="key cannot be None"):
            st.get(None)  # type: ignore

        with pytest.raises(ValueError, match="key cannot be None"):
            st.delete(None)  # type: ignore

        with pytest.raises(ValueError, match="key cannot be None"):
            st.contains(None)  # type: ignore

    def test_resize_grow(self) -> None:
        """Test: Automatisches Vergrössern der Tabelle."""
        st = LinearProbingHashST[str, int](capacity=4)

        # Füge genug Elemente ein, um ein Resize auszulösen
        for i in range(50):
            st.put(f"key{i}", i)

        assert st.size() == 50
        for i in range(50):
            assert st.get(f"key{i}") == i

    def test_resize_shrink(self) -> None:
        """Test: Automatisches Verkleinern der Tabelle."""
        st = LinearProbingHashST[str, int]()

        # Füge Elemente ein
        for i in range(50):
            st.put(f"key{i}", i)

        # Lösche die meisten Elemente
        for i in range(45):
            st.delete(f"key{i}")

        assert st.size() == 5
        for i in range(45, 50):
            assert st.get(f"key{i}") == i

    def test_collision_handling(self) -> None:
        """Test: Korrekte Behandlung von Kollisionen mit Linear Probing."""
        st = LinearProbingHashST[str, int](capacity=4)

        # Füge Elemente ein, die möglicherweise kollidieren
        st.put("A", 1)
        st.put("B", 2)
        st.put("C", 3)
        st.put("D", 4)

        assert st.size() == 4
        assert st.get("A") == 1
        assert st.get("B") == 2
        assert st.get("C") == 3
        assert st.get("D") == 4

    def test_delete_and_rehash(self) -> None:
        """Test: Korrekte Neueinordnung nach Löschen."""
        st = LinearProbingHashST[str, int](capacity=4)

        # Füge Elemente ein
        st.put("A", 1)
        st.put("B", 2)
        st.put("C", 3)

        # Lösche ein Element in der Mitte eines Clusters
        st.delete("B")

        # Stelle sicher, dass andere Elemente noch erreichbar sind
        assert st.get("A") == 1
        assert st.get("C") == 3
        assert st.get("B") is None
        assert st.size() == 2

    def test_large_dataset(self) -> None:
        """Test: Grosse Datenmenge."""
        st = LinearProbingHashST[int, str]()

        # Füge viele Elemente ein
        n = 1000
        for i in range(n):
            st.put(i, f"value{i}")

        assert st.size() == n

        # Überprüfe alle Elemente
        for i in range(n):
            assert st.get(i) == f"value{i}"

        # Lösche die Hälfte
        for i in range(0, n, 2):
            st.delete(i)

        assert st.size() == n // 2

        # Überprüfe verbleibende Elemente
        for i in range(1, n, 2):
            assert st.get(i) == f"value{i}"

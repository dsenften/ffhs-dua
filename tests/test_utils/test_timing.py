"""Tests für das timing Modul."""

import time
import unittest
from unittest.mock import patch

from src.utils.timing import (
    disable_timing,
    enable_timing,
    measure_execution_time,
    timeit,
)


class TestTiming(unittest.TestCase):
    """Test-Klasse für timing utilities."""

    def setUp(self):
        """Setup für jeden Test."""
        # Stelle sicher, dass ENABLE_TIMING zu Beginn False ist
        disable_timing()

    def test_timeit_decorator_disabled(self):
        """Test: @timeit Dekorator bei deaktivierter Zeitmessung."""

        @timeit
        def test_function():
            return "result"

        # Bei deaktivierter Zeitmessung sollte keine Ausgabe erfolgen
        with patch('builtins.print') as mock_print:
            result = test_function()
            mock_print.assert_not_called()
            self.assertEqual(result, "result")

    def test_timeit_decorator_enabled(self):
        """Test: @timeit Dekorator bei aktivierter Zeitmessung."""
        enable_timing()

        @timeit
        def test_function():
            time.sleep(0.001)  # Kurze Pause für messbare Zeit
            return "result"

        # Bei aktivierter Zeitmessung sollte Ausgabe erfolgen
        with patch('builtins.print') as mock_print:
            result = test_function()
            mock_print.assert_called_once()
            # Prüfe, dass die Ausgabe die Laufzeit enthält
            call_args = mock_print.call_args[0][0]
            self.assertIn("test_function Laufzeit:", call_args)
            self.assertIn("Sekunden", call_args)
            self.assertEqual(result, "result")

    def test_enable_disable_timing(self):
        """Test: enable_timing() und disable_timing() Funktionen."""
        # Initial sollte ENABLE_TIMING False sein
        import src.utils.timing
        self.assertFalse(src.utils.timing.ENABLE_TIMING)

        # Nach enable_timing() sollte es True sein
        enable_timing()
        self.assertTrue(src.utils.timing.ENABLE_TIMING)

        # Nach disable_timing() sollte es wieder False sein
        disable_timing()
        self.assertFalse(src.utils.timing.ENABLE_TIMING)

    def test_measure_execution_time(self):
        """Test: measure_execution_time() Funktion."""
        def test_function():
            time.sleep(0.001)  # Kurze Pause für messbare Zeit
            return "result"

        result, exec_time = measure_execution_time(test_function)

        self.assertEqual(result, "result")
        self.assertIsInstance(exec_time, float)
        self.assertGreater(exec_time, 0)
        self.assertLess(exec_time, 1)  # Sollte unter 1 Sekunde sein

    def test_timeit_preserves_function_metadata(self):
        """Test: @timeit Dekorator erhält Funktions-Metadaten."""

        @timeit
        def documented_function():
            """Eine dokumentierte Testfunktion."""
            return 42

        # Funktionsname und Docstring sollten erhalten bleiben
        self.assertEqual(documented_function.__name__, "documented_function")
        self.assertEqual(documented_function.__doc__, "Eine dokumentierte Testfunktion.")

    def test_timeit_with_arguments(self):
        """Test: @timeit Dekorator mit Funktionsargumenten."""
        enable_timing()

        @timeit
        def add_function(a, b, multiplier=1):
            return (a + b) * multiplier

        with patch('builtins.print') as mock_print:
            result = add_function(2, 3, multiplier=2)
            self.assertEqual(result, 10)
            mock_print.assert_called_once()

    def test_timeit_with_classmethod(self):
        """Test: @timeit Dekorator mit @classmethod."""
        enable_timing()

        class TestClass:
            @classmethod
            @timeit
            def class_method(cls, value):
                return value * 2

        with patch('builtins.print') as mock_print:
            result = TestClass.class_method(5)
            self.assertEqual(result, 10)
            mock_print.assert_called_once()


if __name__ == "__main__":
    unittest.main()

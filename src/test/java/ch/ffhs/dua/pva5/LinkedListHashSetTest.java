package ch.ffhs.dua.pva5;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * Diese Klasse enthält Unit-Tests für die Klasse {@link LLHashSet}.
 * Sie verwendet JUnit, um die Korrektheit und Funktionalität der Methoden von {@link LLHashSet} zu überprüfen.
 * Der Fokus liegt insbesondere auf der Methode {@code contains()}, der Größenbestimmung sowie dem Einlesen von Testdaten.
 *
 * @author <a href="mailto:daniel.senften@ffhs.ch">Daniel Senften</a>
 * @version 1.0
 */
class LinkedListHashSetTest {

    private LLHashSet<String> hashSet;

    // Logger für die Klasse initialisieren
    private static final Logger logger = LoggerFactory.getLogger(LinkedListHashSetTest.class);

    // Externe Methode zur Fehlerbehandlung
    private void logError(Exception exception) {
        logger.error("Fehler beim Laden der Datei words.txt", exception);
    }

    @BeforeEach
    void setUp() {
        hashSet = new LLHashSet<>();

        try {
            try (InputStream inputStream =
                         getClass().getClassLoader().getResourceAsStream("words.txt")) {
                assert inputStream != null;
                try (InputStreamReader streamReader =
                             new InputStreamReader(inputStream, StandardCharsets.UTF_8);
                     BufferedReader reader = new BufferedReader(streamReader)) {

                    String line;
                    while ((line = reader.readLine()) != null) {
                        hashSet.add(line);
                    }

                }
            }
        } catch (IOException e) {
            logError(e);
        }

    }

    @Test
    @DisplayName("Test for several entries")
    void contains() {
        assertTrue(hashSet.contains("bore"));
        assertTrue(hashSet.contains("interpolate"));
        assertTrue(hashSet.contains("modify"));
        assertTrue(hashSet.contains("possible"));
        assertTrue(hashSet.contains("woodlot"));
        assertTrue(hashSet.contains("zucchini"));
    }

    @Test
    void size() {
        assertEquals(20_068, hashSet.size());
    }
}

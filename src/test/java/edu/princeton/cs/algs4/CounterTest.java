package edu.princeton.cs.algs4;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

class CounterTest {

    private Counter counter;

    @BeforeEach
    void setUp() {
        counter = new Counter("first");
    }

    @Test
    void checkName() {
        assertThat(counter.toString(), is("0 first"));
    }
    
    @Test
    void emptyCounter() {
       assertThat(counter.tally(), is(0));
    }
    
    @Test
    void increment() {
        counter.increment();
        assertThat(counter.tally(), is(1));
    }

    @Test
    void compareTo() {
        Counter second = new Counter("second");
        assertThat(counter.compareTo(second), is(0));
    }
}

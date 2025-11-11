package ch.ffhs.dua.pva4;

/**
 * Einfache Klasse für ein Paar von zwei int-Werten.
 */
public record Pair(int lower, int higher) {

	@Override
	public int hashCode() {
		final int prime = 101;
		int result = 1;
		result = prime * result + higher;
		result = prime * result + lower;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Pair other = (Pair) obj;
		if (higher != other.higher)
			return false;
		return lower == other.lower;
	}

	@Override
	public String toString() {
		return "(" + lower + ", " + higher + ")";
	}

}

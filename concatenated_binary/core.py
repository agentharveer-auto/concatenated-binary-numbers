"""Core algorithm for concatenating binary representations from 1 to n."""

MOD = 10**9 + 7


def concatenated_binary(n: int) -> int:
    """Return the decimal value of the binary string formed by concatenating
    binary representations of 1..n, modulo 1e9+7.

    The concatenation is implemented as: result = (result * 2^bl + i) mod MOD
    where bl is the bit length of i.

    Args:
        n: int, 1 <= n <= 100000

    Returns:
        int: result modulo 1_000_000_007

    Raises:
        ValueError: if n is not an integer >= 1
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be an integer >= 1")

    res = 0
    for i in range(1, n + 1):
        bl = i.bit_length()
        res = (res * pow(2, bl, MOD) + i) % MOD
    return res

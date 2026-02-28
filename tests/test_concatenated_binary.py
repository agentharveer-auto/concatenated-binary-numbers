import pytest
from concatenated_binary.core import concatenated_binary


def test_examples():
    assert concatenated_binary(1) == 1
    assert concatenated_binary(3) == 27
    assert concatenated_binary(12) == 505379714


def test_bruteforce_small():
    MOD = 10**9 + 7
    def brute(n: int) -> int:
        s = "".join(bin(i)[2:] for i in range(1, n + 1))
        return int(s, 2) % MOD

    for n in range(1, 50):
        assert concatenated_binary(n) == brute(n)


def test_invalid():
    with pytest.raises(ValueError):
        concatenated_binary(0)


def test_large_n():
    # sanity check for upper bound performance and type
    val = concatenated_binary(100000)
    assert isinstance(val, int)

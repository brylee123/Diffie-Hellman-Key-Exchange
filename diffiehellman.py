"""Interactive Diffie–Hellman key exchange demonstration.

Uses deliberately small parameters so the arithmetic is easy to inspect.
Do not use this program to establish real cryptographic keys.
"""

from __future__ import annotations

import getpass
import math
import secrets


def is_prime(number: int) -> bool:
    """Return whether number is prime."""
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    return all(number % divisor != 0 for divisor in range(3, math.isqrt(number) + 1, 2))


def first_primes(count: int) -> list[int]:
    """Generate the first count prime numbers."""
    if count < 0:
        raise ValueError("count must be non-negative")

    primes: list[int] = []
    candidate = 2
    while len(primes) < count:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1 if candidate == 2 else 2
    return primes


def prime_factors(number: int) -> set[int]:
    """Find the distinct prime factors of a positive integer."""
    factors: set[int] = set()
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            factors.add(divisor)
            while number % divisor == 0:
                number //= divisor
        divisor += 1 if divisor == 2 else 2
    if number > 1:
        factors.add(number)
    return factors


def choose_parameters() -> tuple[int, int]:
    """Choose a small prime modulus and a generator of its multiplicative group."""
    primes = first_primes(1000)
    modulus = secrets.choice(primes[2:])  # Exclude 2 and 3.
    order = modulus - 1
    factors = prime_factors(order)
    generators = [
        base
        for base in range(2, modulus)
        if all(pow(base, order // factor, modulus) != 1 for factor in factors)
    ]
    return modulus, secrets.choice(generators)


def read_positive_integer(label: str) -> int:
    """Prompt until the user supplies a positive integer."""
    while True:
        try:
            value = int(getpass.getpass(f"Hidden {label} value: "))
        except ValueError:
            print("Please enter a whole number greater than zero.")
            continue
        if value > 0:
            return value
        print("Please enter a whole number greater than zero.")


def exchange(base: int, modulus: int, alice_secret: int, bob_secret: int) -> tuple[int, int, int, int]:
    """Return Alice's and Bob's public values and their calculated keys."""
    alice_public = pow(base, alice_secret, modulus)
    bob_public = pow(base, bob_secret, modulus)
    alice_key = pow(bob_public, alice_secret, modulus)
    bob_key = pow(alice_public, bob_secret, modulus)
    return alice_public, bob_public, alice_key, bob_key


def main() -> None:
    modulus, base = choose_parameters()
    print("Diffie–Hellman key exchange (educational demonstration)")
    print("These small values and displayed secrets are not secure.\n")
    print(f"Public prime p = {modulus}")
    print(f"Public generator g = {base}\n")

    alice_secret = read_positive_integer("Alice's a")
    bob_secret = read_positive_integer("Bob's b")
    alice_public, bob_public, alice_key, bob_key = exchange(
        base, modulus, alice_secret, bob_secret
    )

    print("\n--- Public exchange ---")
    print(f"Alice sends A = g^a mod p = {base}^{alice_secret} mod {modulus} = {alice_public}")
    print(f"Bob sends   B = g^b mod p = {base}^{bob_secret} mod {modulus} = {bob_public}")
    print("\n--- Calculated locally ---")
    print(f"Alice: B^a mod p = {bob_public}^{alice_secret} mod {modulus} = {alice_key}")
    print(f"Bob:   A^b mod p = {alice_public}^{bob_secret} mod {modulus} = {bob_key}")

    if alice_key != bob_key:
        raise RuntimeError("The calculated keys did not match.")
    print(f"\nBoth parties calculated the same shared value: {alice_key}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")

# Diffie–Hellman Key Exchange

An interactive visualization and a Python terminal proof of concept for Diffie–Hellman key exchange.

## Browser visualizer

Open [index.html](index.html) in a modern browser. No installation, server, or external dependencies are required.

1. Choose a public prime `p` and a public base `g`.
2. Choose Alice's private exponent `a` and Bob's private exponent `b`.
3. Select **Next step** or **Play all** to see which values cross the public channel and how each participant computes the same key.
4. Use **New example** to try another set of inputs. Editing any input resets the walkthrough.

The initial example uses `p = 23`, `g = 5`, `a = 6`, and `b = 15`. Alice publishes `A = g^a mod p = 8`, and Bob publishes `B = g^b mod p = 19`. Alice computes `B^a mod p = 2`; Bob computes `A^b mod p = 2`.

The visualizer uses `BigInt` and modular exponentiation, so it does not calculate enormous intermediate powers. Inputs are deliberately limited to small values for readability. These values offer **no real security**. The browser demo displays both private exponents to teach the exchange; in practice each party keeps its exponent secret.

## Python terminal example

With Python 3 installed, run:

```sh
python diffiehellman.py
```

The terminal example chooses a small prime modulus and a generator, then prompts for two positive private integers with hidden input. It uses modular exponentiation to calculate and display each side of the exchange. The output intentionally reveals the private exponents as part of the walkthrough. These small parameters are for learning and must not be used in production.

## How the exchange works

| Value | Alice | Bob | Public? |
| --- | --- | --- | --- |
| Parameters | `p`, `g` | `p`, `g` | Yes |
| Private exponent | `a` | `b` | No |
| Value sent | `A = g^a mod p` | `B = g^b mod p` | Yes |
| Shared result | `K = B^a mod p` | `K = A^b mod p` | No |

Both results equal `g^(ab) mod p`. Diffie–Hellman establishes shared key material but does not authenticate participants or encrypt messages on its own. For real applications, use a vetted cryptography library with authenticated exchange, safe parameters, and key derivation.

Further reading: [Diffie–Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange).

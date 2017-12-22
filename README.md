# Diffie-Hellman Key Exchange (Proof of Concept)
Diffie-Hellman key exchange proof of concept

Setup and Execution:
1. Install Python 3+
2. Run from Terminal

Run Through
1. The program calculates the first 10,000 prime numbers (admittedly not efficiently) and puts them into a list.
2. Pseudo-randomly selects two values for g and p (guaranteed not the same values).
3. Then asks the user for two integer inputs for the values of a and b.
4. Computes each step of Diffie-Hellman
5. Checks if the final keys are equal (which it should be)


About Diffie-Hellman from Wikipedia (src: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)

"Diffie–Hellman key exchange (DH) is a method of securely exchanging cryptographic keys over a public channel and was one of the first public-key protocols as originally conceptualized by Ralph Merkle and named after Whitfield Diffie and Martin Hellman.[1][2] DH is one of the earliest practical examples of public key exchange implemented within the field of cryptography.

Traditionally, secure encrypted communication between two parties required that they first exchange keys by some secure physical channel, such as paper key lists transported by a trusted courier. The Diffie–Hellman key exchange method allows two parties that have no prior knowledge of each other to jointly establish a shared secret key over an insecure channel. This key can then be used to encrypt subsequent communications using a symmetric key cipher."

Illustrated with color mixing analogy: https://upload.wikimedia.org/wikipedia/commons/3/35/Diffie-Hellman_Key_Exchange-modified.png

Computerphile does a fantastic job explaining DH without the usage of mathematics based on the above color mixing analogy.
https://www.youtube.com/watch?v=NmM9HA2MQGI

They also do a mathematics-based version below as well.
https://www.youtube.com/watch?v=Yjrfm_oRO0w

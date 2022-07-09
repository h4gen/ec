from ecdsa import SigningKey, SECP128r1
sk = SigningKey.generate(curve=SECP128r1) # uses NIST192p
vk = sk.verifying_key
signature = sk.sign(b"message")
assert vk.verify(signature, b"message")
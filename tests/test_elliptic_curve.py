from ecdsa import SigningKey, SECP128r1
from hashlib import md5

def test_secp128r1_verify(accounts, SECP128R1):
    sk = SigningKey.generate(curve=SECP128r1, hashfunc=md5)
    vk = sk.verifying_key
    message = b'message'
    m = md5(message)
    m_hash = m.digest()
    signature = sk.sign(message)
    assert vk.verify(signature, b"message")

    bool_resp = SECP128R1.validateSignature(
        m_hash, 
        [signature[:16], signature[16:]], 
        [vk.to_string()[:16], vk.to_string()[16:]], 
        {'from': accounts[0], 'gas' : 15**6})
    assert bool_resp

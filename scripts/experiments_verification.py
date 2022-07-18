from brownie import ECDSA, accounts, network
from ecdsa import SigningKey, SECP128r1, NIST256p
from ecdsa.curves import Curve
import numpy as  np
from hashlib import sha256, md5


sk = SigningKey.generate(curve=SECP128r1, hashfunc=md5)
sk.to_string()
len(sk.to_string())
vk = sk.verifying_key
message = b'message'
m = md5(message)
m_hash = m.digest()
len(m_hash) * 8
signature = sk.sign(message)
len(signature) * 8 // 2
len(signature[:16])
len(signature[16:])
len(vk.to_string())
assert vk.verify(signature, b"message")


def main():
    # requires brownie account to have been created
    if network.show_active()=='development':
        # add these accounts to metamask by importing private key
        owner = accounts[0]
        # Parameters: https://neuromancer.sk/std/secg/secp128r1
        ecdsa = ECDSA.deploy(
            0xfffffffdfffffffffffffffffffffffc, #a
            0xe87579c11079f43dd824993c2cee5ed3, #b
            0x161ff7528b899b2d0c28607ca52c5b86, #gx
            0xcf5ac8395bafeb13c02da292dded7a83, #gy
            0xfffffffdffffffffffffffffffffffff, #p
            0xfffffffe0000000075a30d1b9038a115, #n
            {'from':owner})

        bool_resp = ecdsa.validateSignature(
            m_hash, 
            [signature[:16], signature[16:]], 
            [vk.to_string()[:16], vk.to_string()[16:]], 
            {'gas' : 15**6})

        assert bool_resp
        

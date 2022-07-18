import pytest
from brownie import accounts, ECDSA

@pytest.fixture(autouse=True)
def setup(fn_isolation):
    """
    Isolation setup fixture.
    This ensures that each test runs against the same base environment.
    """
    pass


@pytest.fixture(scope="module")
def SECP128R1(accounts, ECDSA):
    """
    Yield a `Contract` object for the VyperStorage contract.
    """
    # Parameters: https://neuromancer.sk/std/secg/secp128r1
    yield accounts[0].deploy(
        ECDSA,
        0xfffffffdfffffffffffffffffffffffc, #a
        0xe87579c11079f43dd824993c2cee5ed3, #b
        0x161ff7528b899b2d0c28607ca52c5b86, #gx
        0xcf5ac8395bafeb13c02da292dded7a83, #gy
        0xfffffffdffffffffffffffffffffffff, #p
        0xfffffffe0000000075a30d1b9038a115, #n
        # {'from': accounts[0]}
        )




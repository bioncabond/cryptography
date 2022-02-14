import pytest
from cryptography.encrypt import *

from cryptography import __version__

# Mic Check 
def test_version():
    assert __version__ == '0.1.0'

#Encrypt 
def test_encrypt_a_string(): 
    e = encrypt("HELLO World",3)
    actual = e
    expected = "khoor zruog" 
    assert actual == expected

#outside of our char range 
def test_char_out_of_range(): 
    e = encrypt("Hell0 W0rld$",3)
    actual = e
    expected = "khoo0 z0uog$" 
    assert actual == expected

#decrypt 
def test_decrypt_a_string(): 
    msg = ("khoo0 z0uog$")
    actual = decrypt(msg,3)
    expected = "hell0 w0rld$" 
    assert actual == expected 

#crack 
def test_crack_the_code(): 
    msg = "pa dhz aol ilza vm aptlz, pa dhz aol dvyza vm aptlz."
    actual = crack(msg) 
    expected = "it was the best of times, it was the worst of times."
    assert actual == expected
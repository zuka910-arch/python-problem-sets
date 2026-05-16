from twttr import shorten

def test_lower_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_upper_vowels():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"

def test_numbers():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("!?.,") == "!?.,"
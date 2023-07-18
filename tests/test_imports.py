from chronos import *

def test_imports():
    assert 'os' in globals(), "os must be in globals"
    assert 'sleep' in globals(), "sleep must be in globals"
    assert 'json' in globals(), "json must be in globals"
    # assert 'JSONDecodeError' in globals(), "JSONDecoderError must be in globals"
    assert 'gettempdir' in globals(), "gettempdir must be in globals"
    # assert 'logging' in globals(), "logging must be imported"

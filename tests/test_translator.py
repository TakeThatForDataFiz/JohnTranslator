from john_translator import translator


def test_source_text_retrieved():
    source_static = 'sample text'
    src = translator.receive_source(source_static)
    assert src == source_static

# def test_sample():
#     assert True

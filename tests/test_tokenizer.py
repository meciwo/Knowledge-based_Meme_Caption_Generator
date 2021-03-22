from src.tokenizer import tokenize


def test_tokinzer():
    pred = tokenize("これはテストのテキストです。ファミリーマート")
    assert ["これ", "は", "テスト", "の", "テキスト", "です", "。", "ファミリーマート"] == pred

    pred = tokenize("「これは、テストのテキストです。ファミリーマート」")
    assert ["これ", "は", "テスト", "の", "テキスト", "です", "。", "ファミリーマート"] == pred

    pred = tokenize("これは、テストのテキストです。ファミリーマート🍎")
    assert ["これ", "は", "テスト", "の", "テキスト", "です", "。", "ファミリーマート"] == pred

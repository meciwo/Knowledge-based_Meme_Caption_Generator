import MeCab
from dotenv import load_dotenv
import os
import emoji


load_dotenv()
mecab_path = os.environ["MECAB_PATH"]
mecab = MeCab.Tagger(f"-Owakati -d {mecab_path}")
mecab.parse("")  # バグ対処


def remove_emoji(src_str):
    return "".join(c for c in src_str if c not in emoji.UNICODE_EMOJI)


def tokenize(text):
    text = remove_emoji(str(text))
    text = text.replace("「", "").replace("」", "").replace("、", "")
    result = mecab.parse(text).strip().split(" ")
    return result

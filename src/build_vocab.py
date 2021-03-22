import pickle
import argparse
from collections import Counter
import pandas as pd
from tokenizer import tokenize
from tqdm import tqdm


class Vocabulary(object):
    """Simple vocabulary wrapper."""

    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0

    def add_word(self, word):
        if word not in self.word2idx:
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1

    def __call__(self, word):
        if word not in self.word2idx:
            return self.word2idx["<unk>"]
        return self.word2idx[word]

    def __len__(self):
        return len(self.word2idx)


def build_vocab(file, threshold, wiki_file=None):
    """Build a simple vocabulary wrapper."""
    captions = pd.read_csv(file, encoding="utf-8").text.values
    counter = Counter()

    for i, caption in enumerate(tqdm(captions)):
        tokens = tokenize(caption)
        counter.update(tokens)

        # if (i + 1) % 1000 == 0:
        #    print("[{}/{}] Tokenized the captions.".format(i + 1, len(captions)))

    if wiki_file is not None:
        with open(wiki_file) as f:
            # ファイルのサイズを使用しプログレスバーを作成
            for line in tqdm(f):
                tokens = tokenize(line)
                counter.update(tokens)

    # If the word frequency is less than 'threshold', then the word is discarded.
    words = [word for word, cnt in counter.items() if cnt >= threshold]

    # Create a vocab wrapper and add some special tokens.
    vocab = Vocabulary()
    vocab.add_word("<pad>")
    vocab.add_word("<start>")
    vocab.add_word("<end>")
    vocab.add_word("<unk>")

    # Add the words to the vocabulary.
    for i, word in enumerate(words):
        vocab.add_word(word)

    return vocab


def main(args):
    vocab = build_vocab(
        file=args.caption_path, threshold=args.threshold, wiki_file=None,
    )
    vocab_path = args.vocab_path
    with open(vocab_path, "wb") as f:
        pickle.dump(vocab, f)
    print("Total vocabulary size: {}".format(len(vocab)))
    print("Saved the vocabulary wrapper to '{}'".format(vocab_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--caption_path",
        type=str,
        default="data/relation.csv",
        help="path for train annotation file",
    )
    parser.add_argument(
        "--wiki_path",
        type=str,
        default="data/wiki.txt",
        help="path for train annotation file",
    )
    parser.add_argument(
        "--vocab_path",
        type=str,
        default="./data/vocab.pkl",
        help="path for saving vocabulary wrapper",
    )
    parser.add_argument(
        "--threshold", type=int, default=1, help="minimum word count threshold"
    )
    args = parser.parse_args()
    main(args)

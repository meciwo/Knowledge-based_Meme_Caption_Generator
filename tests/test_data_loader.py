"""
from src.data_loader import get_loader
import pickle


def test_data_loader():
    with open("../data/vocab.pkl", "rb") as f:
        vocab = pickle.load(f)
    data_loader = get_loader(
        "../data/resized_images/",
        vocab,
        transform=None,
        batch=4,
        shuffle=True,
        num_workers=1,
    )
    total_step = len(data_loader)
    pass
"""

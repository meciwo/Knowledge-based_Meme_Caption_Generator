# Knowledge-Base Meme Caption Generator
This is a NN model for generating a Japanese funny caption for a image

## Installation
```sh
git clone https://github.com/meciwo/Knowledge-based_Meme_Caption_Generator.git
cd KMCG
```

if you have already installed poetry
```sh
poetry install
```

if you havn't installed poetry
```sh
pip install poetry
poetry install
```

## Usage
### Scrayping
```sh
python scr/scrayping.py
```

### preprocessing
```sh
python src/build_vocab.py
```
### training
```sh
python src/train.py
```

### sampling
```sh
python src/sampling --image PATH_TO_YOUR_IMAGE
```

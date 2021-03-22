# neural_joking_machine
This is a NN model for generating a Japanese funny caption for a image referenced on [Neural Joking Machine : Humorous image captioning][1].
<br>A lot of codes are from [this repository][2].

[1]:https://arxiv.org/abs/1805.11850
[2]:hoge

## Installation
```sh
git clone https://github.com/meciwo/neural_joking_machine.git
cd neural_joking_machine
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
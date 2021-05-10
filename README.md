# Huffman coding: a simple guide

### Introduction

The Huffman code is an optimal instantaneous (or prefix) code where: optimal means that it has the shortest expected length (we'll see this in more detail later on); instantaneous means that there is no codeword that is a prefix of any other codeword, for example the code [00, 10, 01] is a prefix code.

### Features

This implementation, given a string in input, returns the optimal binary code by implementing the Huffman algorithm. Let's consider, for instance, the word 'Hello!'. The resulting binary code will be:

| Symbol | Codeword |
|--------|----------|
|    o   |    00    |
|    !   |    01    |
|    l   |    10    |
|    h   |    110   |
|    e   |    111   |

with _Expected Length_ = **2\.33** and _Entropy_ = **2\.25**. The formulas for the these two values are 

```
$E[l(X)] = \sum_{i}^{n} p_{i}l_{i}$
```

for the expected length and 

```
$H(X) = \sum_{i}^{n} p_{i}\log\frac{1}{p_{i}}$
```
for the entropy. You can call the following attributes:

- _string_: it returns the input string or 'Hello!' if nothing is no string was given;
- _probabilities_: it returns a dictionary with the frequency of the symbols (characters) of the given string;
- _encoding_: it returns a dictionary of the given string encoded;
- _tree_: it returns the binary tree generated to encode the string;

### Requirements

- numpy

### Installation

Clone or download zip
- Run `pipenv install` in directory to install requirements

### License

MIT

**Gotta love free stuff!**

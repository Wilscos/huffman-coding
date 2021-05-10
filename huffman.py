import numpy as np


class HuffmanCoding:
    """
    Encode a string with the Huffman algorithm implemented. Find expected length and entropy of the code.

    ...

    Attributes
    ----------
    string : str
        string to encode

    Methods
    -------
    huffman_code()
        encodes the a given string, otherwise it encodes the string 'hello'
    assign_code(nodes, label, result, prefix='')
        assigns the code to each node of the Huffman binary tree
    average_code_length()
        computes the average length of the code
    compute_entropy()
        computes the entropy of the code
    compute_probabilities()
        computes the probabilities associated to each symbol of the string given in input
    """

    def __init__(self, string=''):
        """
        :param string: input string to encode
        """

        if string != '':
            self.string = string
        else:
            self.string = 'Hello!'

        self.probabilities = self.compute_probabilities()
        self.encoding = self.huffman_code()[0]
        self.tree = self.huffman_code()[1]

    def huffman_code(self):
        """
        It computes the Huffman code for the string given input

        :return: the Huffman code, the associated binary tree, the array of probabilities of each symbol, the codewords
        """

        values = {'h': 0.2, 'e': 0.2, 'l': 0.4, 'o': 0.2}
        if len(self.string) > 0:
            values = self.probabilities
        probabilities = values.copy()
        nodes = {}
        for key in probabilities.keys():
            nodes[key] = []

        for i in range(len(values) - 1):
            sorted_probabilities = sorted(probabilities.items(), key=lambda x: x[1])
            min1 = sorted_probabilities[0][0]
            min2 = sorted_probabilities[1][0]
            probabilities[min1 + min2] = probabilities.pop(min1) + probabilities.pop(min2)
            nodes[min1 + min2] = [min1, min2]

        code = {}
        root = list(probabilities.keys())[0]
        tree = self.assign_code(nodes, root, code)

        probabilities_array = [values[k] for k in list(code.keys())]
        codewords = [code[k] for k in list(code.keys())]

        return code, tree, probabilities_array, codewords

    def assign_code(self, nodes, label, result, prefix=''):
        """
        It builds iteratively the codewords for each node of the tree. It follows a greedy strategy.

        :param nodes: dictionary of the nodes
        :param label: the label associated to the nodes (probabilities)
        :param result: the resulting code, which is empty at the beginning of the algorithm
        :param prefix: the prefix code built for the current node
        :return: the tree when the nodes to explore are finished, the label if not
        """

        children = nodes[label]
        tree = {}
        if len(children) == 2:
            tree['0'] = self.assign_code(nodes, children[0], result, prefix + '0')
            tree['1'] = self.assign_code(nodes, children[1], result, prefix + '1')
            return tree
        else:
            result[label] = prefix
            return label

    def average_code_length(self):
        """
        It computes the average length of the code sequence generated

        :return: the average length and the length of each codeword
        """

        code_lengths = [len(code) for code in self.codewords]
        average_length = np.sum(np.array(self.prob_array) * np.array(code_lengths))
        return average_length, code_lengths

    def compute_entropy(self):
        """
        It computes the entropy of the code. The minimum number of bits that could be used to describe the input string

        :return: the entropy
        """

        entropy = - np.sum(np.array(self.prob_array) * np.log2(self.prob_array))
        return entropy

    def compute_probabilities(self):
        """
        It computes the probability of occurrence of each symbol in the input string

        :return: a dictionary of the symbols and their frequencies in the string
        """

        lower_sequence = self.string.lower()
        frequencies = {}
        for char in lower_sequence:
            if char not in frequencies.keys():
                frequencies[char] = 1
            else:
                frequencies[char] += 1

        probabilities_array = [freq / len(self.string) for freq in list(frequencies.values())]
        probabilities = {k: v for k, v in zip(list(frequencies.keys()), probabilities_array)}
        return probabilities


print(HuffmanCoding())

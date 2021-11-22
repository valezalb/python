import sys
import heapq


def file_character_frequencies(file_name):
    # Suggested helper Dont hepify until second FUNCTION
    # create a dictionary
    dict = {}
    file = open(file_name)
    characters = []
    frequencies = []
    for line in file:
        for character in line:
            if character not in characters:
                first_seen=1
                characters.append(character)
                frequencies.append(first_seen)
            else:
                for i in range(len(characters)):
                    if(character == characters[i]):
                        frequencies[i] += 1
    file.close()
    for i in range(len(characters)):
        dict[characters[i]]=frequencies[i]
    return dict


class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one using double parens e.g. PriorityTuple((x, (y, z))) """
    def __lt__(self, other):
        return self[0] < other[0]

    def __le__(self, other):
        return self[0] <= other[0]

    def __gt__(self, other):
        return self[0] > other[0]

    def __ge__(self, other):
        return self[0] >= other[0]

    def __eq__(self, other):
        return self[0] == other[0]

    def __ne__(self, other):
        x = self.__eq__(other)
        return not x


"""class node:
    def __init__(self,frequency,character,left=None,right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right
        self.huff = ''
"""

def huffman_codes_from_frequencies(frequencies):
    # Suggested helper
    #build heap before while loop
    #use priorityTuple
    #tuple seems to be a class that compares

    huff_dict = {}
    heap = [PriorityTuple((frequency,[letter])) for letter,frequency in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        t1,char1 = heapq.heappop(heap) #left child
        t2,char2 = heapq.heappop(heap) #right child
        heapq.heappush(heap, PriorityTuple((t1+t2, [char1,char2])))
    return heapq.heappop(heap)[1]


def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    # Suggested strategy...
    freqs = file_character_frequencies(file_name)
    new_dict=huffman_codes_from_frequencies(freqs)
    return BFS(new_dict,"")

def BFS(huff,encoding):
    if(len(huff) == 1):
        return {huff[0]:encoding}
    else:
        return {**BFS(huff[0],encoding+'0'),**BFS(huff[1],encoding+'1')}


def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))


def decode_file_using_codes(file_name_encoded, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))


def main():
    """Provided to help you play with your code."""
    import pprint
    frequencies = file_character_frequencies(sys.argv[1])
    print(frequencies)
    codes = huffman_codes_from_frequencies(frequencies)
    idk=huffman_letter_codes_from_file_contents(sys.argv[1])
    print(idk)
    pprint.pprint(codes)


if __name__ == '__main__':
    """We are NOT grading you based on main, this is for you to play with."""
    main()

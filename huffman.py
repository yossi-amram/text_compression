

"""
    creates the dictionary of frequencies based on the corpus
    corpus can be any iterable
"""


def frequency_dict(corpus):
    freq = {}
    for token in corpus:
        if token in freq.keys():
            freq[token] += 1
        else:
            freq[token] = 1
    return freq

def get_min(roots):
    m = min(roots,key=lambda root: root[1])
    roots.remove(m)
    return m

"""
    creates the huffman tree based on a frequency dictionary
"""
def huffman_tree(freq):
    # initial list of leaves
    roots  = [item for item in freq.items()]

    # combining the roots until they al all in one tree
    while len(roots)>=2:
        left = get_min(roots)
        right = get_min(roots)
        new_root = [left, left[1]+right[1], right]
        roots.append(new_root)

    # only the root of the final tree left
    return roots[0]


def code_builder(root, code = {}, prefix = ""):
    if len(root) == 2:
        code[root[0]] = prefix
    if len(root) == 3:
        code_builder(root[0], code, prefix+"0")
        code_builder(root[2], code, prefix+"1")
    return code

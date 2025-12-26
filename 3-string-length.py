sentences = [
    "Python is simple",
    "I like code",
    "Readability matters",
    "Do it step by step",
    "Short",
    "Do it step by step and get rolling",
    'demo'
]
min_len = 12

"""
Expected output = 
[
  "Python is simple (16)",
  "Readability matters (20)",
  "Do it step by step (18)"
]
"""


def string_size(sentences, min_length):

    # container for the result
    result = []

    # selection function
    def select_sentence(size):
        return size > min_length

    # transformation function
    def transform(sentence, size):
        return f'{sentence} ({size})'

    for sentence in sentences:
        size = len(sentence)
        if select_sentence(size):
            transform_sentence = transform(sentence, size)
            result.append(transform_sentence)
    result1 = [transform(sentence, len(sentence))
               for sentence in sentences if select_sentence(len(sentence))]
    return result1


r = string_size(sentences, min_len)
print(r)

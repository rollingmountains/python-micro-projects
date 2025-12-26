sentences = [
    "The sun rises in the east and sets in the west.",
    "Python is a versatile programming language used for web development, data science, and automation.",
    "Reading books can expand your knowledge and imagination."
]

keyword = 'and'

# PROCEDURAL STYLE


def highlight_keyword(sentences, keyword):
    for sentence in sentences:
        if keyword in sentence:
            word_list = sentence.split(' ')
            result = ' '.join([word.upper()
                               if keyword == word else word for word in word_list])
    return result


r = highlight_keyword(sentences, keyword)
print(r)

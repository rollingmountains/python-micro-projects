# sentences = [
#     "The sun rises in the east and sets in the west.",
#     "Python is a versatile programming language used for web development, data science, and automation.",
#     "Reading books can expand your knowledge and imagination."
# ]


# def keyword_highlight(lines, keyword):
#     result = []
#     for line in lines:
#         if keyword in line:
#             word_list = line.split(' ')
#             for index, word in enumerate(word_list):
#                 if word == keyword:
#                     word_list[index] = word.upper()
#             highlight_sentence = ' '.join(word_list)
#             result.append(highlight_sentence)

#     return (len(lines), len(result), result)


# total_sentences, matched_sentences, results = keyword_highlight(
#     sentences, keyword='and')
# print(
#     f'total_sentences = {total_sentences}\ntotal_matches = {matched_sentences}\nresult = {results}')


sentences = [
    "The sun rises in the east and sets in the west.",
    "Python is a versatile programming language used for web development, data science, and automation.",
    "Reading books can expand your knowledge and imagination."
]


def matching_line_factory(keyword):
    def detect_match(line):
        return True if keyword in line else False
    return detect_match


def highlight_word_factory(keyword):
    return lambda word: word.upper() if word == keyword else word


def transform_line(line, keyword):
    word_list = line.split(' ')
    transform = highlight_word_factory(keyword)
    return ' '.join(transform(word) for word in word_list)


def keyword_highlight(lines, keyword, *, case_sensitive=False):

    keyword_to_match = keyword.lower() if not case_sensitive else keyword

    detect = matching_line_factory(keyword_to_match)

    results = [transform_line(line, keyword_to_match)
               for line in lines if detect(line if case_sensitive else line.lower())]

    return results


r = keyword_highlight(sentences, keyword='reading')
print(r)

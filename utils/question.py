import nltk

print('Downloading Natural Language Toolkit (NLTK), please wait...')

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
# nltk.download('stanford')
# nltk.download()

print('Finished downloading NLTK')


class Question:

    _no = [
        'no',
        'nope',
        'not'
    ]

    _yes = [
        'yes',
        'ya',
        'yep',
        'yeah'
    ]

    def is_yes_response(self, text):
        if any(affirmative_string in text for affirmative_string in self._yes):
            return True
        return False

    def is_no_response(self, text):
        if any(no_string in text for no_string in self._no):
            return True
        return False

    def is_a_question(self, text):
        return True
        # tokens = nltk.word_tokenize(text)
        # pos_tokens = nltk.pos_tag(tokens)
        # chunked = nltk.chunk.ne_chunk(pos_tokens)
        # nltk.parse.stanford(text)
        # hello = "hello"

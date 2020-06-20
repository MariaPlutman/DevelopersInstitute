import re
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(THIS_FOLDER, 'Day_3.txt')


class Text:
    def __init__(self):
        with open(filepath, "r") as file:
            self.text = file.read().lower()

    def frequency(self, in_word):
        str1 = self.text.split()
        str2 = []
        for word in str1:
            if word == in_word:
                str2.append(word)
            for word in range(0, len(str2)):
                return 'Frequency of', str2[word],
                'is :', str1.count(str2[word])

    def most_common(self):
        return Counter(self.text.strip())

    def unique_words(self):
        unique = self.text.split()
        return set(unique)

    @classmethod
    def from_file(cls, txt_file):
        return cls(txt_file)


class TextModification(Text):
    def no_punctuation(self):
        self.text = self.text.translate(
            str.maketrans('', '', string.punctuation))
        return self.text

    def stop_words(self):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(self.text)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        return filtered_sentence

    def special_characters(self):
        return ''.join(e for e in self.text if e.isalnum())


def main():
    text = Text()
    print(text.frequency("has"))

    print(text.most_common())

    print(text.unique_words())

    text_mod = TextModification()
    text_mod.no_punctuation()
    print(text_mod.stop_words())

    text_mod.special_characters()


if __name__ == "__main__":
    main()

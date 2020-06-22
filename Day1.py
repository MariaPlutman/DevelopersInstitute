from googletrans import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
english_words = []
translator = Translator()
for word in french_words:
    translation = translator.translate(word, src="fr", dest="en").text
    english_words.append(translation)
my_dic = dict(zip(french_words, english_words))
print(my_dic)

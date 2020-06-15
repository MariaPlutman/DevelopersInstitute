class IsPalindrome:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


palindrome = IsPalindrome()
text = input('Please enter the word: ')

for character in text:
    palindrome.push(character)

reversed_text = ''
while not palindrome.is_empty():
    reversed_text = reversed_text + palindrome.pop()

if text == reversed_text:
    print(f'The {text} is a palindrome.')
else:
    print(f'The {text} is not a palindrome.')

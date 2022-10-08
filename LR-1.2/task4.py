import re


class File:
    def __init__(self, name):
        self.name = name
        self.words = 0
        self.sentences = 0
        self.symbols = 0
        try:
            data = open(self.name, 'r')
        except FileNotFoundError:
            raise FileNotFoundError('Cannot find file!')
        except IOError:
            raise IOError('Cannot open file!')
        data.close()

    def count_words(self):
        data = open(self.name, 'r')
        for line in data:
            self.words += len(re.findall(r'[A-Za-z]+', line))
        data.close()
        return self.words

    def count_sentences(self):
        data = open(self.name, 'r')
        for line in data:
            self.sentences += len(re.findall(r'\w+[.?!]+', line))
        data.close()
        return self.sentences

    def count_symbols(self):
        data = open(self.name, 'r')
        for line in data:
            self.symbols += len(line) - line.count(' ') - line.count('\n')
        data.close()
        return self.symbols

    def __str__(self):
        return f'Characters: {self.count_symbols()}\nWords: {self.count_words()}\nSentences: {self.count_sentences()}'


def main():
    f = File(r'C:\Users\User\Desktop\text.txt')
    print(f.__str__())


main()

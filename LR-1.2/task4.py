class File:
    def __init__(self, name):
        self.__name = name
        self.__sentence = 0
        self.__words = 0
        self.__chars = 0

    def start_count(self):
        with open(self.__name, 'r') as f:
            for line in f:
                w = line.split()
                self.__sentence += line.count('.')
                self.__words += len(w)
                self.__chars += len(line.replace(' ', ''))

    def show_result(self):
        print('Characters:', self.__chars)
        print('Words:', self.__words)
        print('Sentences:', self.__sentence)


def main():
    f = File(r'C:\Users\User\Desktop\text.txt')
    f.start_count()
    f.show_result()


main()

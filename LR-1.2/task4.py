class File:
    def __init__(self, name):
        # check if file exists
        self.__name = name
        self.__sentence = 0
        self.__words = 0
        self.__chars = 0

    def start_count(self):
        with open(self.__name, 'r') as f:
            for line in f:
                # words may be written a,b,c
                w = line.split()
                # the line ends with ! ... ?
                self.__sentence += line.count('.')
                self.__words += len(w)
                self.__chars += len(line.replace(' ', ''))

    def show_result(self):
        print('Characters:', self.__chars)
        print('Words:', self.__words)
        print('Sentences:', self.__sentence)


def main():
    # open in a class
    f = File(r'C:\Users\User\Desktop\text.txt')
    f.start_count()
    f.show_result()


main()

import math


def text_metrics():
    print('Which of the following would you like to do?')
    print('1. Check your GFI')
    print('2. Check your RES')
    print('3. Check your SMOG')
    print('4. Check your ARI')
    print('5. Quit')


def gfi():
    sentences = int(input('Please enter the number of sentences in the sample: '))
    words = int(input('Please enter the number of words in the sample: '))
    big_words = int(input('Please enter the number of big words in the sample: '))
    return 0.4 * ((words/sentences) + 100 * (big_words/words))


def res():
    sentences = int(input('Please enter the number of sentences in the sample: '))
    words = int(input('Please enter the number of words in the sample: '))
    syllables = int(input('Please enter the number of syllables in the sample: '))
    return 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)


def smog():
    big_words = int(input('Please enter the number of big words in the sample: '))
    a = (math.sqrt(big_words) / 10) * 10
    return math.floor((a + 9) / 10 + 3)


def ari():
    sentences = int(input('Please enter the number of sentences in the sample: '))
    words = int(input('Please enter the number of words in the sample: '))
    characters = int(input('Please enter the numver of characters in the sample: '))
    return 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43


if __name__ == '__main__':
    option = 0
    while True:
        text_metrics()
        option = int(input('Enter the number of your choice: '))
        if option == 1:
            gfi()
        elif option == 2:
            res()
        elif option == 3:
            smog()
        elif option == 4:
            ari()
        elif option == 5:
            print('Quitting')
        else:
            print('Option unavailable. Please choose an option displayed.')


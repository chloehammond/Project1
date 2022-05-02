import math


def text_metrics():
    print('Which of the following would you like to do?')
    print('1. Check your Gunning Fog Index')
    print('2. Check your Reading Ease Score')
    print('3. Check your SMOG Index Grade Level')
    print('4. Check your Automated Readability Index')
    print('5. Quit')


def gfi(sentences, words, big_words):
    gunning_fog_index = 0.4 * ((words/sentences) + 100 * (big_words/words))
    print(f'Gunning Fog Index: {gunning_fog_index:.2f}')


def res(sentences, words, syllables):
    reading_ease_score = 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
    print(f'Reading Ease Score: {reading_ease_score:.2f}')


def smog(big_words):
    a = (math.sqrt(big_words) / 10) * 10
    smog_index = math.floor((a + 9) / 10 + 3)
    print(f'SMOG Index Grade Level: {smog_index:.2f}')


def ari(sentences, words, characters):
    readability_index = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
    print(f'Automated Readability Index: {readability_index:.2f}')


if __name__ == '__main__':
    option = 0
    sentences = int(input('Please enter the number of sentences in the sample: '))
    words = int(input('Please enter the number of words in the sample: '))
    big_words = int(input('Please enter the number of big words in the sample: '))
    syllables = int(input('Please enter the number of syllables in the sample: '))
    characters = int(input('Please enter the number of characters in the sample: '))

    while option != 5:
        text_metrics()
        option = int(input('Enter the number of your choice: '))
        if option == 1:
            gfi(sentences, words, big_words)
        elif option == 2:
            res(sentences, words, syllables)
        elif option == 3:
            smog(big_words)
        elif option == 4:
            ari(sentences, words, characters)
        elif option == 5:
            print('Quitting')
        else:
            print('Option unavailable. Please choose an option displayed.')

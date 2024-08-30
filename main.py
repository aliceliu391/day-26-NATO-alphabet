import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

not_complete = True
while not_complete:
    word = input("Enter a word: ").strip().upper()
    try:
        word_list = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only numbers in the alphabet!")
    else:
        print(word_list)
        not_complete = False

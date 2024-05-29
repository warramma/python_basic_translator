#5-29-24

#build a translator that takes any phrase
#and replaces the vowels with the letter w
#and replaces spaces with new lines

def translate(phrase):
    translation=''
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + 'w'
        elif letter == ' ':
            translation = translation + '\n'
        else:
            translation = translation + letter
    return translation


print(translate(input('Enter a phrase: ')))
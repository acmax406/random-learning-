import string

def rotate_letter(letter,n):
    if letter.isupper():
        start= ord('A') # ord('A') gives the unicode of the letter A, so if the word starts with upper case then
                        #this unicode will be assigned to it
    if letter.islower():
        start = ord('a')

    x= ord(letter)-start
    i=((n+x) % 26)+start
    return chr(i)

def rotate_word(word,n):
    res=''
    for letter in word:
        res = res + rotate_letter(letter,n)
    return res

if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))
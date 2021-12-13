def palindrom(word):

    small_letters = word.lower()
    reverse_word = small_letters[::-1]

    if small_letters == reverse_word:
        print(True)
    else:
        print(False)

print(palindrom("Kajak"))




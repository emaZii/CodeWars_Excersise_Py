
"""
<summary>
    The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.

    Upper or lower case letter does not matter -- "eNglisH" is also correct.

    Return value as boolean values, true for the string to contains "English", false for it does not.

    Fundamentals

    level 8 kyu
</summary>
"""

def sp_eng(sentence):
    word = "english"
    if word in sentence.lower():
        return True
    else:
        return False
    


def main():
    sentence = "English"
    print(sp_eng(sentence))


if __name__ == "__main__":
    main()

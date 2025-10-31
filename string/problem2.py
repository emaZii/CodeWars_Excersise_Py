'''
<summary>
You are given the string "agrtertyfikfmroyrntbvsukldkfa". The logic is that you start from the a and make your way right. The next vowel is an e and it is the consecutive vowel, then i and so forth until you get to u. If you keep moving right you find a which happens to be the consecutive vowel. Return 6.
This is a slightly trickier example: you are given the string "erfaiekjudhyfimngukduo". As you move right you ignore all vowels until you get to the a, then ignore the rest until you get to the e, which is the consecutive vowel, and so forth until you get to the o. Return 4.
Note
For this kata, the vowels are a, e, i, o, u, in that order. y is not considered a vowel in this kata.

Good luck!

level : 8kyu
</summary>
'''


def get_the_vowels(word):
    vowels = 'aeiou'
    current_vowel_index = 0
    consecutive_count = 0
    for char in word:
        if char == vowels[current_vowel_index]:
            consecutive_count += 1
            current_vowel_index = (current_vowel_index + 1) % len(vowels)
    return consecutive_count


def main():
    str = "erfaiekjudhyfimngukduo"
    print(get_the_vowels(str))

if __name__ == '__main__':
    main()
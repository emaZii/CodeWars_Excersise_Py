'''
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

level : 6kyu
'''
def find_missing_letter(chars):
        for i in range(len(chars) - 1):
             if ord(chars[i + 1]) != ord(chars[i]) + 1:
                  return chr(ord(chars[i]) + 1)

def main():
    print(find_missing_letter("abcde"))
    print(find_missing_letter("lmno"))

if __name__ == "__main__":
    main()
'''
<summary>
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

level 8kyu
</summary>

'''

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    if boolean == False:
        return "No"

def main():
    print(bool_to_word(True))

if __name__ == "__main__":
    main()
'''
Write a function that removes the spaces from the string, then return the resultant string.

Examples (Input -> Output):

level:8kyu
'''


def no_space(x):
    return x.replace(" ", "")

def main():
    print(no_space("hello world"))


if __name__ == '__main__':
    main()
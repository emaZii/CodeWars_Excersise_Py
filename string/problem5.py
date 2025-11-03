'''
<summary>
    Complete the solution so that it returns true
    if the first argument(string) passed in ends with
    the 2nd argument (also a string).
    Examples:

    Inputs: "abc", "bc"
    Output: true

    Inputs: "abc", "d"
    Output: false

    level: 7kyu

</summary>
'''

def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False

def main():
    print(solution("abc", "d"))

if __name__ == '__main__':
    main()
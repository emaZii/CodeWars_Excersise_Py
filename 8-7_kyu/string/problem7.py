"""
<summary>
    Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

    Use conditionals to return the proper message:

    case	return
    name equals owner	'Hello boss'
    otherwise	'Hello guest'
    level  8kyu
</summary>
"""

def greet(name, owner):
    if name == owner:
        return f'Hello boss'
    else:
        return 	'Hello guest'


def main():
    greeting = "Hello boss"
    print(greet(greeting))

if __name__ == "__main__":
    main()
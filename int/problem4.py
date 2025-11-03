def multi_table(number):
    for i in range(10):
        result = i * number
        return f"{i} * {number} = {result}\n"

def main():
    print(multi_table(7))

if __name__ == '__main__':
    main()
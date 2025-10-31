'''
<summary>
In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.

More examples in the test cases.

Good luck!

Level: 7kyu
</summary>
'''

def repeats(arr):
    num = 0
    for data in arr:
        if arr.count(data) == 1:
            num += data
    return num

def main():
    lst = [4,5,7,5,4,8]
    print(repeats(lst))
    
if '__main__' == __name__:
     main()
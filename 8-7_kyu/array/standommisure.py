'''
Write a function that takes an integer array and returns its Stanton measure.

Examples
For [1, 4, 3, 2, 1, 2, 3, 2]:
1 appears 2 times → 2 appears 3 times → Stanton measure = 3.

For [1, 4, 1, 2, 11, 2, 3, 1]:
1 appears 3 times → 3 appears 1 time → Stanton measure = 1.

Level: 7kyu
'''

def stanton_measure(arr):
   return arr.count(arr.count(1))

def main():
    arr = [1, 4, 3, 2, 1, 2, 3, 2]
    print(stanton_measure(arr))

if __name__ == '__main__':
    main()
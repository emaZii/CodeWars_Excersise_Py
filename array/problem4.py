'''
I'm new to coding and now I want to get the sum of two arrays...
Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
level : 8kyu
'''

def array_plus_array(arr1, arr2):
    total = sum(arr1) + sum(arr2)
    return total

def main():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8, 9, 10]
    print(array_plus_array(arr1, arr2))

if __name__ == '__main__':
    main()
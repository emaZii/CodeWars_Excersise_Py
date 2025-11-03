'''
<summary>
    Create a function that returns the sum of the two lowest positive numbers
    given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

    For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

    [10, 343445353, 3453445, 3453545353453] should return 3453455.

    ArraysFundamentals

    Level 7kyu
</summaru>
'''


def sum_two_smallest_numbers(numbers):
    num1min = min(numbers)
    numberscopy = numbers.copy()
    numberscopy.remove(num1min)
    num2min = min(numberscopy)
    result = num1min + num2min
    return result
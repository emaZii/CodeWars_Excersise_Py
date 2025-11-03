"""
<summary>
    Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

    Return your answer as a number.
    FundamentalsStringsArrays

    level 8kyu

</summary>
"""

def sum_mix(arr):
    result = 0
    for num in arr:
        if isinstance(num, (int)):
            result += num
        if isinstance(num, (str)):
            result += int(num)
    return result
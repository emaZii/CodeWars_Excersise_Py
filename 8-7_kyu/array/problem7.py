"""
<summary>
    Write a function that returns both the minimum and maximum number of the given list/array.

    Examples (Input --> Output)
    [1,2,3,4,5] --> [1,5]
    [2334454,5] --> [5,2334454]
    [1]         --> [1,1]
    Remarks
    All arrays or lists will always have at least one element, so you don't need to check the length. Also, your function will always get an array or a list, you don't have to check for null, undefined or similar.

    Lists Arrays Fundamentals

    Level 7kyu
</summary>
"""

def min_max(lst):
    lst2 = []
    num_min = min(lst)
    max_num = max(lst)
    lst2.append(num_min)
    lst2.append(max_num)
    return lst2
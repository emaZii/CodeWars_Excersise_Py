'''
Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

level : 8kyu
'''


def count_positives_sum_negatives(arr):
    if arr is None or not arr:
        return []
    maxpositive = 0
    maxnegative = 0
    for positive in arr:
        if positive > 0:
            maxpositive += 1
    for negative in arr:
        if negative < 0:
            maxnegative += negative

    array  = [maxpositive, maxnegative]
    return array
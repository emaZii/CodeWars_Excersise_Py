"""
<usmmary>
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

FundamentalsStringsArrays

level 8kyu

</summary>
"""

def fake_bin(x):
    string = ''

    for s in x:
        if int(s) >= 5:
            s = "1"
            string += s
        else:
            s = '0'
            string += s
    return string
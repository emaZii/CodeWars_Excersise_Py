"""
<summary>
    Write a function to split a string and convert it into an array of words.

    Examples (Input ==> Output):
    "Robin Singh" ==> ["Robin", "Singh"]

    "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
    Arrays Strings Fundamentals

    Level: 8kyu
</summary>
"""

def string_to_array(s):
    if len(s)>0:
        x = s.split()
        return x
    else:
        return [""]



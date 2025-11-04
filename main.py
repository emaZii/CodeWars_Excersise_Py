name = 'geeks for geeks'
original_list = [1, 2, 3, 4, 5]
doubled_list = [(lambda x: x * 2)(x) for x in original_list]
#print(doubled_list)

string = "hello world"
uppercase_letters = [char.upper() for char in string if char.isalpha()]
#print(uppercase_letters)

list1 = [x for x in range(1, 21) if x % 2 == 0]
#print(list1)

chars =[]
for ch in 'TutorialsPoint':
    chars.append(ch)
#print(chars)

squares = [x*x for x in range(1, 21)]
#print(squares)

list_name = [1,1,2,34,4,5,6,7,]
list_name.sort(key=None, reverse=True)
#print(list_name)

list3 = [10,16,9,24,5]
list3.sort()
list3.reverse()
#print(list3)

numbers = [3,1,4,1,5,9,2,6,5,3,5]
sorted_numbers = sorted(numbers, reverse=True)
#print(sorted_numbers)


def myfunction(x):
    return x%10

list4 = [17,23,46,51,90]
list4.sort(key=myfunction)
print(list4)
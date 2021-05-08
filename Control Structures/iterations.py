my_list = [1, 2, 3, 6, 12]

for index, value in enumerate(my_list):
    print('The index is: ' + str(index) + ' and the element is: ' + str(value))

i = 0
while i < 10:
    print(i)
    i = i + 1

my_dict = {1: 'aaa', 2: 'bbb', 3: 'ccc', 4: 'ddd'}
for key in my_dict:
    print('These are the values ' + str(key) + ' alongside: ' + str(my_dict[key]))

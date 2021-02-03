# the following line reads the list from the input; do not modify it, please
my_numbers = [int(x) for x in input().split(" ")]
new_numbers = []
for i in range(len(my_numbers)):
    if my_numbers[i] % 2 == 0:
        new_numbers.append(my_numbers[i])
print(new_numbers)
# work with the variable 'my_numbers'
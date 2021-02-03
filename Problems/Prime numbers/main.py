prime_numbers = [
    number
    for number in range(2, 1001)
    if all(number % value != 0 for value in range(2, number))
]
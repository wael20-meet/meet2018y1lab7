def add_numbers(start, end):
    """
    this function should add
    all the numbers from start
    to end, including both
    write your code here
    """

    c = 0
    for number in range(start, end + 1):
        print(number)
        c = c + number
    print(c)
    return c
test1 = add_numbers(333, 777)
print(test1) 

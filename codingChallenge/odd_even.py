def find_even_numbers(start, end):
    even_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print("Even numbers within the range", start_range)

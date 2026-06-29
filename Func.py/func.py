def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = sum(numbers)
    count = len(numbers)
    average = total / count

    return average    

print(calculate_average([100, 200, 300, 400,500]))
print(calculate_average([50, 150, 250]))
print(calculate_average([]))
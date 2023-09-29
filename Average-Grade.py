counter = 0
total_sum = 0
amount = int(input())
counter = amount + counter
for counter in range(amount):
    grades = int(input())
    total_sum += grades
avg = round(total_sum/amount, 1)
print(f"Average: {avg}%")

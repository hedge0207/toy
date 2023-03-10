import random

N = 10000
same_birthday = 0
for _ in range(N):
    birthdays = []
    for i in range(23):
        birthday = random.randint(1,365)
        if birthday in birthdays:
            same_birthday += 1
            break
        else:
            birthdays.append(birthday)

print(same_birthday/N * 100)
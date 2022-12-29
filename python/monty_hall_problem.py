import random
import time

start = time.time()
correct = 0
cnt = 100000
for _ in range(cnt):
    door = ['goat', 'goat', 'car']
    random.shuffle(door)
    answer = door.index('car')
    select = random.randrange(3)

    door[answer] = False
    door[select] = False
    goat = door.index('goat')

    changed_select = 0
    for i in range(3):
        if i != select and i != goat:
            changed_select = i

    if changed_select == answer:
        correct += 1

print(correct/cnt)
print(time.time()-start)

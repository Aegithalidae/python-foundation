million = list(range(1, 1_000_001))
print(min(million))
print(max(million))
print(sum(million))

total = 0
for value in million:
    total = total + value
print(total)
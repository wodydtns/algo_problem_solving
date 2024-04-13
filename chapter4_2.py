n = int(input())
hour = 0
minute = 60
second = 60
count = 0
for i in range(hour + n + 1):
    for j in range(minute):
        for k in range(second):
            if "3" in str(i) or "3" in str(j) or "3" in str(k):
                count += 1
print(count)

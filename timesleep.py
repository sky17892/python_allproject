import time
for i in range(8):
    print(i)
    time.sleep(1)

def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1, 3, 5, 7, 9]
result = add(data)
print(result)
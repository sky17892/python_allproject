import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s" % i)

print("Start")
start = time.time()

for i in range(3):
    long_task()

end = time.time()
print("End")
print("걸리 시간: %.2f초" % (end - start))

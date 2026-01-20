import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")
start = time.time()

threads = []
for i in range(3):
    t = threading.Thread(target=long_task)
    threads.append(t) 

for t in threads:
    t.start()

for t in threads:
    t.join()

end = time.time()
print("End")
print("걸리 시간: %.2f초" % (end - start))

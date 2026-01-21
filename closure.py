#메서드 클로저
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter
    
counter1 = make_counter()

print(counter1())
print(counter1())
print(counter1())

counter2 = make_counter()

print(counter2())
print(counter2())
print(counter2())
print(counter2())

#클래스 클로저
class Counter:
    def __init__(self):
        self.count = 0
    def incmethod(self):
        self.count += 1
        return self.count
    
counter3 = Counter()

print(counter3.incmethod())
print(counter3.incmethod())
print(counter3.incmethod())
print(counter3.incmethod())
print(counter3.incmethod())

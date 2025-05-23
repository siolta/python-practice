import time
import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def simulate_line(self, till_show, max_time):
        pq = Queue()
        tix_sold = []

        for i in range(100):
            pq.enqueue("person" + str(i))

        t_end = time.time() + till_show
        now = time.time()
        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)

        return tix_sold


a_queue = Queue()
print(f"Queue is empty? {a_queue.is_empty()}")

for i in range(5):
    a_queue.enqueue(i)

print(f"Queue length: {a_queue.size()}")

for i in range(5):
    print(a_queue.dequeue())

print(f"Queue length: {a_queue.size()}")

queue = Queue()
sold = queue.simulate_line(5, 1)
print(f"Tickets sold: {sold}")

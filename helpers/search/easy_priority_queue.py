#!/usr/bin/python3

import itertools
import heapq

class EasyPriorityQueue:
    """ Priority queue that allows removal (which, shockingly,
        none of the built-in queues seem to permit).

        Written using the suggestions from:
        https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes"""

    REMOVED = '<removed-task>'     # placeholder for a removed item

    def __init__(self):
        self.pq = list()                    # list of entries arranged in a heap
        self.entry_finder = dict()          # mapping of items to entries
        self.counter = itertools.count()    # unique sequence count

    def push(self, item, priority):
        assert item not in self.entry_finder
        assert item != self.REMOVED

        count = next(self.counter)
        entry = [priority, count, item]

        self.entry_finder[item] = entry
        heapq.heappush(self.pq, entry)

    def pop(self):
        while len(self.pq) > 0:
            priority, count, item = heapq.heappop(self.pq)
            if item is not self.REMOVED:
                del self.entry_finder[item]
                return item
        raise KeyError('pop from an empty priority queue')

    def remove(self, item):
        entry = self.entry_finder.pop(item)
        entry[-1] = self.REMOVED

    def change_priority(self, item, new_priority):
        self.remove(item)
        self.push(item, new_priority)

    def __contains__(self, item):
        return item in self.entry_finder

    def __len__(self):
        return len(self.entry_finder)


if __name__ == "__main__":

    q = EasyPriorityQueue()
    q.push("a", 1)
    q.push("e", 5)
    q.push("b", 2)
    q.push("c", 3)

    q.remove("b")
    q.change_priority("a", 9)

    print("Contains a:", "a" in q, "; contains b:", "b" in q)
    print(len(q))
    print(q.pop(), q.pop(), q.pop())
    print(len(q))
import heapq

class PriorityQueue():
    def __init__(self):
        self._queue = []
        self._entry_finder = {}
        self._count = 0

    def add_item(self, item, priority=0):
        if item in self._entry_finder:
            self.remove_item(item)
        self._count += 1
        entry = [priority, self._count, item]
        self._entry_finder[item] = entry
        heapq.heappush(self._queue, entry)
    
    def remove_item(self, item):
        entry = self._entry_finder.pop(item)
        entry[-1] = "<removed-task>"

    def pop(self):
        while self._queue:
            priority, count, item = heapq.heappop(self._queue)
            if item != "<removed-task>":
                del self._entry_finder[item]
                return item
    
    def __len__(self):
        return len(self._queue)
            
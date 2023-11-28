import heapq

class PriorityQueue():
    """
    A class that implements a priority queue. Implementation is from the Python docs.
    """
    def __init__(self):
        """
        No arg constructor for the queue
        """
        self._queue = [] # private
        self._entry_finder = {} # private
        self._count = 0 # private

    def add_item(self, item, priority=0):
        """
        Adds a new item to the queue or updates the key of an existing one

        args:
            item (any): The item to be added to the queue
            priority= (int): Keyword argument used to update the key of an existing item
        """
        if item in self._entry_finder:
            self.remove_item(item)
        self._count += 1
        entry = [priority, self._count, item]
        self._entry_finder[item] = entry
        heapq.heappush(self._queue, entry)
    
    def remove_item(self, item):
        """
        Removes an item from the queue

        args:
            item (any): The item to be removed from the queue
        """
        entry = self._entry_finder.pop(item)
        entry[-1] = "<removed-task>"

    def pop(self):
        """
        Pops the first minimal element from the queue

        returns:
            item (any): The first minimal element of the queue
        """
        while self._queue:
            priority, count, item = heapq.heappop(self._queue)
            if item != "<removed-task>":
                del self._entry_finder[item]
                return item
    
    def __len__(self):
        """
        __len__ implementation, where len returns the length of the queue
        """
        return len(self._queue)
            
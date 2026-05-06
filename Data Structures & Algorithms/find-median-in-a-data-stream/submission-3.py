class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap
        

    def addNum(self, num: int) -> None:

        # Insert num into left heap by default
        heapq.heappush(self.left, -1 * num)

        # Case: left > right
        if self.left and self.right and -1 * self.left[0] > self.right[0]:
            heapq.heappush(self.right, -1 * heapq.heappop(self.left))
        
        # Case: right <= left
        if self.left and self.right and self.right[0] <= -1 * self.left[0]:
            heapq.heappush(self.left, -1 * heapq.heappop(self.right))

        # Case: different lengths of left and right
        while len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -1 * heapq.heappop(self.left))
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -1 * heapq.heappop(self.right))
        

    def findMedian(self) -> float:
        print("left: ", self.left, "  right: ", self.right)
        if len(self.left) > len(self.right):
            return float(-1 * self.left[0])
        return float((-1 * self.left[0] + self.right[0] ) / 2)
        
        
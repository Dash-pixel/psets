import random

class MaxHeap():
    def __init__(self, arr):
        self.heap = self.create(arr)

    def heapify_up(self, index):
        
        p_index = (index - 1)// 2

        if p_index < 0:
            return False

        if self.heap[index] > self.heap[p_index]:
            self.heap[p_index], self.heap[index] = self.heap[index], self.heap[p_index]
            return p_index
        
        else:
            return False

    def insert(self, item):
        self.heap.append(item)
        index = len(self.heap) - 1
        while index := self.heapify_up(index):
            continue


    def pop(self):

        to_return = self.heap[0]

        if len(self.heap) < 2:
            self.heap = []
            return to_return

        self.heap[0] = self.heap.pop()
        index = 0

        
        
        while True: #while the index kids are not none
            left = 2 * index + 1
            right = 2 * index + 2


            if left < len(self.heap) and self.heap[left] > self.heap[index] and (right == len(self.heap) or self.heap[left] > self.heap[right]):
                self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                index = left

            elif right < len(self.heap) - 1 and self.heap[right] > self.heap[index]:
                self.heap[index], self.heap[right] = self.heap[right], self.heap[index]
                index = right
            
            else:
                break

        return to_return


        # lets just exchange max with min -- do a while true?




    def peek(self):
        return self.heap[0]

    def create(self, arr):
        self.heap = arr
        for index in range((len(arr)-1), -1, -1):
            self.heapify_up(index)
        return self.heap


arr = MaxHeap([1])


import unittest

class TestHeap(unittest.TestCase):
    def test_pop(self):
        arr = MaxHeap([1, 3, 7, 2, 5, 4])
        self.assertEqual(arr.pop(), 7)
        self.assertEqual(arr.pop(), 5)
        self.assertEqual(arr.pop(), 4)
        self.assertEqual(arr.pop(), 3)
        self.assertEqual(arr.pop(), 2)
        self.assertEqual(arr.pop(), 1)

    def test_peek(self):
        arr = MaxHeap([1, 3, 7, 2, 5, 4])
        self.assertEqual(arr.peek(), 7)

    # def test_create(self):
    #     arr = MaxHeap([1, 3, 7, 2, 5, 4])
    #     self.assertEqual(arr.heap, [7, 5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()
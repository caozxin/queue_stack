class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    def __init__(self):
        self.linked_list = list()
        
    def enqueue(self, item):
        # write your code here
        self.linked_list.append(item)

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        # print(self.linked_list)
        if len(self.linked_list) == 0:
            return -1

        n = len(self.linked_list)

        if self.linked_list[0] is not None:
            result = self.linked_list[0]
            self.linked_list.remove(self.linked_list[0])
            return result



# new_queue = MyQueue()
# new_queue.enqueue(1)
# new_queue.enqueue(2)
# new_queue.enqueue(3)
# print(new_queue.dequeue())
# new_queue.enqueue(4)
# print(new_queue.dequeue())

new_queue = MyQueue()
new_queue.enqueue(10)
print(new_queue.dequeue())
print(new_queue.dequeue())
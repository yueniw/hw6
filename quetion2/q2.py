class Queue:
    inner_list = []
    counter = 0
    
    def enqueue(self, value):
        self.inner_list.append(value)
        
    def dequeue(self):
        if len(self.inner_list) < 1:
            return None
        return self.inner_list.pop(0)

    def delete(self, data):
        for i in range(len(self.inner_list)):
            tmp = self.dequeue()
            if (data != tmp):
                self.enqueue(tmp)      

obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)

obj.delete(7)
print(obj.dequeue()) # Should return 5
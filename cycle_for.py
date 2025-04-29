class MyIterable():
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyIterator(self.data)
    

class MyIterator():
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 1
        return val
    
if __name__ == "__main__":
    my_iterator = MyIterator([1,2,3])

    for i in my_iterator:
        print(i)

    for i in my_iterator:
        print(i)

    


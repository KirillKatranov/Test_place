class Square():
    def __init__(self, max_square):
        self.max_square = max_square
        self.current = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.max_square:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    squares = Square(5)
    for square in squares:
        print(square)

    for square in squares:
        print(square)

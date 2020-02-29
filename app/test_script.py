class Myclass:
    def __init__(self, num1, num2, list1, list2):
        self.num1 = num1
        self.num2 = num2
        self.list1 = list1
        self.list2 = list2
    
    def add_numbers(self):
        assert(type(self.num1) is int)
        assert(type(self.num2) is int)

        return (self.num1 + self.num2)
    
    def list_length(self):
        #assert that the length of the lists are equal
        assert(len(self.list1) == len(self.list2))

        return 1

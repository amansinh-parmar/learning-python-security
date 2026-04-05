class Math:
    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b
    
a = Math(5)
# print(a.num())
# a.add_to_num(7)
# print(a.add_to_num())
print(a.add(2,5))



'''
class Math:
    @staticmethod
    def add(a,b):
        return a + b

result = Math.add(5,2)
print(result)''' 
class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    # >> GETTER <<  method use with "@property"
    @property
    def ten_value(self):
        return 10 * self._value

    # >> SETTER <<  method use with "function_name.setter"
    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10

        # return 10 * self._value
    
obj1 = MyClass(10)
obj1.ten_value = 49
print(obj1.ten_value)
obj1.show()
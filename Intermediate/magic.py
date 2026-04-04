class Employee:
    name = "Jack"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
            return i
        
    def __str__(self):
        return f"This is '__str__' method."

    def __repr__(self):
        return f"This is '__repr__' method."

    def __call__(self, *args, **kwds):
        print(f"The Artist name is: {self.name}.")

        
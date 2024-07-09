class assignment:
    def __init__(self,score):
        self.score = score

p1 = assignment("100")
print(p1.score)


class Vegetable:
    type = "edible"
    def vegetablemethod(self):
        print("This is not a fruit")

broccoli = Vegetable()
broccoli.vegetablemethod()
print(broccoli.type)
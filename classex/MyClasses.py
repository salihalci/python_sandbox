class Car:

    def __init__(self, user_id):
        self.user_id=user_id
        print(self.user_id)

car2 = Car("abc")
print(car2.user_id)

car1 = Car()
print("MyCar!")


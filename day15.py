class UserInfo():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + " " + self.last_name

obj = UserInfo("sameer", "maharjan")
print(obj.full_name())
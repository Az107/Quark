from ProtoActions import  ActionsMaster, Input
class Actions(ActionsMaster):
    username = Input()
    password = Input()

    def login(self):
        print(self.username.value())
        if self.username.value() == "alb" and self.password.value() == "1234":
            self.fun("alert('loged!')")
        self.username.value("")
        self.password.value("")


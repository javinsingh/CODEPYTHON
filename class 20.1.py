class myclass:
    __privatevar = 27;
    def privmeth(self):
        print("im in class myclass")
    def hello(self):
        print("private varible value: ",myclass.__privatevar)
foo = myclass()
foo.hello()
foo.__privmeth
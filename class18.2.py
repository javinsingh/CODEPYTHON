class employee:
    def _init_(self):
        print("employee created")
    def _del_(self):
        print("deestructer called")
def create_obj():
    print("making object.......")
    obj = employee()
    print("function end")
    return obj
print("calling create_ obj function")
obj  = create_obj()
print("program end")
class Check(object):
    def __init__(self, fn):
       self._fn = fn

    def __call__(self, *args, **kwargs):
        print("login")
        self._fn()

@Check
def comment():
    print("Leave your commetns")

comment()
        



    


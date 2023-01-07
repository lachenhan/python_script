class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    # get property values
    @property  
    def get_size(self):
        return self.width, self.height

    # set property values
    @get_size.setter
    def get_size(self, size: tuple):
        self.width, self.height = size


r = Rectangle()
print(r.get_size)

r.get_size = (20, 40)
print(r.get_size)


    
class Rectangle(object):
    def __init__(self,width, height):
        self.width = width
        self.height = height

    # get property
    @property  # get property values
    def get_size(self):
        return self.width, self.height

    # change property
    @get_size.setter
    def get_size(self, size: tuple):
        self.width, self.height = size

    #delete property
    @get_size.deleter
    def get_size(self):
        del self.width
        del self.height


# get rectangle size
r = Rectangle(10,20)
print(r.get_size)

# set rectangle size
r.get_size = (20, 40)
print(r.get_size)

# delete rectangle size
# following code will get error, because width already being deleted.
del r.width
print(r.size)


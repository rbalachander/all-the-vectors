# instructions
# create a vector class
# that should...
# add vectors
# scale vector
# norm or len
# dot product
# override __str__ and __repr__
class Vector:
    def __init__(self, *nums):
        self.nums = nums

    def __str__(self):
        return "{}".format(self.nums)

    def __repr__(self):
        return self.__str__

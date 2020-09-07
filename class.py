class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        sort=sorted(self.__elements)
        self.maximumDifference=abs(sort[-1]-sort[0])
       
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

class Vector:
    def __init__(self,d):
        self._coords=[0]*d
    def __len__(self):
        return len(self_.coords)
    def __getitem__(self,j):
        return self._coords[j]
    def __setitem(self,j,val):
        self._coords[j]=val
    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError ("Dimension does not match! ")
            result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j]+self[j]
        return result
    def __eq__(self, other):
        return self._coords == other._coords
    def __ne__(self,other):
        return not self==other
        def __str__(self):
            return '<'+str(self._coords)+'>'
if __name__=='__main__':
    v = Vector(5)
    v[1]=23
    v[-1]=45
    print(v)
    u=v+v
    print(u)
    total=0
    for entry in v:
        total+=entry
    print(total)

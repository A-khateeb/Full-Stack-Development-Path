class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("Step cannot be 0")
        if stop is None:
            start , stop = 0, start
        self._length = max(0, ( stop - start + step-1) //step)
        self._start= start
        self._step= start

    def getlenth(self):
        return self._length

    def getitem(self , k):
        if k < 0:
            k+= len(self)
        if not 0 <= k < self._length:
            raise ("Index out of range!")
        return self._start+ k*self._step
if __name__ == '__main__':
    a2 = Range(1,140,2)
    a2.getlenth()

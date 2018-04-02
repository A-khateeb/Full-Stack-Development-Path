class SqeuenceIterator():
    def __init__(self, seq):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k+=1
        if(self._k < len(self._seq)):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(data):
        return self

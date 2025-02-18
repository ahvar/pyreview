import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0  # number of items in the array
        self._capacity = 2  # current capacity
        self._array = self._make_array(
            self._capacity
        )  # elements of the DyanmicArray class

    def __getitem__(self, k):
        if 0 <= k < self._n:
            raise IndexError()
        return self._array[k]

    def _resize(self, c):
        """
        Resize the underlying array with additional capacity:
        1. Tuple is an immutable sequence
        2. Resize to c capacity
        """
        new_arr = self._make_array(c)
        for i in self._n:
            new_arr[i] = self._array[i]
        self._array = new_arr
        self._capacity = c

    def _append(self, element):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._n] = element
        self._n += 1

    def __len__(self):
        return self._n

    def _make_array(self, c):
        return (c * ctypes.py_object)()

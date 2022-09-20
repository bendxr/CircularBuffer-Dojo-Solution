from exceptions import BufferEmptyException 
from exceptions import BufferFullException


class CircularBuffer:
    """
    A circular buffer, cyclic buffer or ring buffer is a data structure
    that uses a single, fixed-size buffer as if it were connected end-to-end.
    """

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__box = []

    def read(self):
        """
        Read the oldest data.
        Raises:
            BufferEmptyException: [nothing to read]
        Returns:
            [data]: [oldest data in box list]
        """

        if self.free() == self.__capacity:
          raise BufferEmptyException("Circular buffer is empty")
        return self.__box.pop(0)

      
    def write(self, data):
        """
        Write new data
        Args:
            data ([data]): [any type of data]
        Raises:
            BufferFullException: [can't write anymore box full]
        """

        if self.free() == 0:
            raise BufferFullException("Circular buffer is full")
        self.__box.append(data)


    def overwrite(self, data):
        """
        Overwrite data
        Args:
            data ([data]): [any type of data]
        """
        if self.free() > 0:
            self.write(data)
        else:
            self.read()
            self.write(data)

    def clear(self):
        """
        Clear everything in the box
        """
        self.__box = []

    def capacity(self):
      return self.__capacity

    def free(self):
      return (self.__capacity - len(self.__box))

    def print(self):
      print("internal state = {}".format(self.__box))
    

    
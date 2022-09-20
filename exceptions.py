class BufferFullException(BufferError):
    """
    Exception raised when CircularBuffer is full.    
    message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """
    Exception raised when CircularBuffer is empty.
    message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message

        

          


        

          
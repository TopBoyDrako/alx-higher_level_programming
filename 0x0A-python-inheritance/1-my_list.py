class MyList(list):
    """
    MyList class inherits from the list class.

    Public instance method:
        def print_sorted(self): prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        print(sorted(self))

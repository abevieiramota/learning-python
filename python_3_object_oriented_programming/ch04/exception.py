class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super(EvenOnly, self).append(integer)

def no_return():
    print 'entrou'
    raise Exception("sempre lança")
    print 'nunca printa'

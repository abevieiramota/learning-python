# -*- encoding: utf-8 -*-
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

def do_throw(do):

    if do:
        raise Exception("sou uma exceçao")

def fluxo_excecao(do):

    print 'entrei'
    try:
        do_throw(do)
    except Exception:
        print 'capturada'
    else:
        print 'nenhuma exceçao capturada'
    finally:
        print 'finally'

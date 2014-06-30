#-*- encoding: utf-8 -*-
class Pessoa(object):

    def __dont_call_me(self):
        print "não me chama {}".format("Porra!")



if __name__ == "__main__":

    p = Pessoa()
    p._Pessoa__dont_call_me()

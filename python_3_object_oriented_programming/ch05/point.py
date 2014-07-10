class Point(object):

    def _set_name(self, name):
        self._name = name

    def _get_name(self):
        print self._name
        return self._name

    name = property(_get_name, _set_name)

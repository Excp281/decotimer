class Keys:
    def __init__(self):
        self.lst = {}

    def set(self, key, value):
        if key in self.lst.keys():
            raise ValueError("Duplicate key: %s" % key)
        else:
            self.lst.update({key: value})

    def get(self, key):
        if key not in self.lst.keys():
            raise ValueError("Key not found: %s" % key)
        else:
            return self.lst[key]

    def delete(self, key):
        if key not in self.lst.keys():
            raise ValueError("Key not found: %s" % key)
        else:
            del self.lst[key]


keys = Keys()
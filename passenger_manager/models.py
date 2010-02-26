import os
import shelve

DB_FILE = os.path.join(os.path.dirname(__file__), "data.db")

class Connection(object):
    def __init__(self):
        self.connection = shelve.open(DB_FILE, writeback=True)
    
    def store(self, key, object, autosync=True):
        for k in self.connection:
            if self.connection[k] == object:
                del self.connection[k]
        
        self.connection[key] = object
        
        if autosync:
            self.sync()
    
    def delete(self, key, autosync=True):
        del self.connection[key]
        
        if autosync:
            self.sync()
    
    def sync(self):
        self.connection.sync()
    
    def close(self):
        self.connection.close()
    
    def __getitem__(self, key):
        self.connection[key]
    
    def __setitem__(self, key, value):
        self.connection[key] = value

connection = Connection()


class Host(object):
    def __init__(self, **kwargs):
        fields = [
            "project_folder",
            "host_aliases",
            "hostname",
            "dev_environment",
            "environment_variables"
        ]
        
        for f in fields:
            self.__dict__[f] = kwargs.get(f)

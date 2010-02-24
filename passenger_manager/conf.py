import os, sys
import re
from passenger_manager.exceptions import *

class Singleton(object):
    __instance = None
    
    # Singleton implementation
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance


class HostsParser(Singleton):
    def __init__(self):
        if sys.platform in ["linux", "darwin"]:
            self.hosts_path = os.environ.get("HOSTALIASES", "/etc/hosts")
        
        if not os.path.exists(self.hosts_path):
            raise HostsFileNotFound(("The Hosts file (%s) could not be located. Please specify one in " + \
                                    "HOSTALIASES environment variable") % self.hosts_path)
        self.hosts = set()
    
    def load_hosts(self):
        in_passenger = False
        for line in open(self.hosts_path, "r"):
            if line == "#### INIT PASSENGER PANE CONFIGURATION - DO NOT MODIFY\n":
                in_passenger = True
                continue
                
            if line == "#### END OF PASSENGER PANE CONFIGURATION\n":
                break
            
            if in_passenger:
                host, aliases = [part.strip() for part in line.split(" ", 1)]
                self.hosts.update(aliases.split(" "))

    def write_hosts(self, hosts=None):
        pass
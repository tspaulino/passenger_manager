import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "")))

from passenger_manager.conf import *

class TestSingleton(unittest.TestCase):
    def testSingularity(self):
        # Assert if all singleton instances has the same Object ID (Memory address)
        self.assertTrue(id(Singleton()) == id(Singleton()))

class TestHostsParser(unittest.TestCase):
    def setUp(self):
        os.environ['HOSTALIASES'] = os.path.join(os.path.dirname(__file__), "hosts_test")
        self.hosts_parser = HostsParser()
    
    def testHostsList(self):
        self.hosts_parser.load_hosts()
        self.assertEqual(len(self.hosts_parser.hosts), 3)


if __name__ == "__main__":
    unittest.main()

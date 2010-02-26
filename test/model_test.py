import unittest

from passenger_manager.models import *

class HosTestCase(unittest.TestCase):
    def testConnection(self):
        h = Host(hostname="test.local", project_folder="/tmp")
        self.assertEquals(h.hostname, "test.local")
        self.assertEquals(h.project_folder, "/tmp")

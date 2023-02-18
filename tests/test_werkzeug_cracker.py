from werkzeug_cracker import Werkzeug_Cracker
from queue import Queue
from . import *

def test_run():
   cracker = Werkzeug_Cracker(test_hash, test_words, 4)
   assert cracker.run() == True  

def test_init_worker():
    cracker = Werkzeug_Cracker(test_hash, test_words, 4)
    assert cracker.init_workers() == True

from werkzeug.security import check_password_hash
from progress.bar import IncrementalBar
from queue import Queue

import threading
import sys
import os
import argparse
import textwrap

__version__ = "1.0"
__author__ = "Anataar"

class Werkzeug_Cracker(threading.Thread):

    def __init__(self, hash, password_lst, workers):
        super().__init__()
        self.hash = hash[0]
        self.password_lst = password_lst
        self.workers = workers
        self._stop_event = threading.Event()
        self.bar = IncrementalBar('Countdown', max = password_lst.qsize())
        self.start()

    def init_workers(self):
        events = []

        ## Start Workers
        for i in range(self.workers):
            event = threading.Thread(target=self.brute)
            events.append(event)
            events[-1].start()

    ## Stop workers
    def stop(self):
        self._stop_event.set()
        self.bar.finish()
    
    ## Return bool if workers should stop or not
    def stopped(self):
        return self._stop_event.is_set()

    def brute(self):

        ## While the Queue isn't empty
        while not self.password_lst.empty() and self.stopped() != True:
            password = self.password_lst.get()
            self.bar.next()
            
            ## Will check if the password match
            if check_password_hash(self.hash, password) == True:
                self.stop()
                print(f"\nPassword found: {password}")
        sys.exit(0)


    def run(self):
        self.init_workers()


if __name__ == "__main__":

    ## Menu
    parser = argparse.ArgumentParser(description='Werkzeug hash cracker', formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent('''
    Example:
            werkzeug_cracker.py -p [hash] -w [wordlist] -t [threads]'''))

    parser.add_argument('-p','--password', help='load hash file')
    parser.add_argument('-w','--wordlist', help='load wordlist file')
    parser.add_argument('-t','--threads', help=f'number of threads, default={os.cpu_count()}', type=int, default=os.cpu_count())
    args = parser.parse_args()

    ## If no args
    if not args.password or not args.wordlist:
        print(parser.format_help())

    else:
        ## Open the hash file
        with open(args.password,"r") as hash:
            hash =  hash.read().split()
        
        ## Open the wordlist
        with open(args.wordlist,"r", encoding="latin-1") as wordlist:

            raw_words = wordlist.read().split()
            
            ## Initialize the Queue
            words = Queue()

            ## Increment the Queue with passwords of the wordlist
            for word in raw_words:
                words.put(word)

            
        ## Initialize
        Werkzeug_Cracker(hash, words, args.threads)

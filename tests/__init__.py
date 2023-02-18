from queue import Queue

## Open the hash file
with open("../example/hash.txt","r") as hash:
    test_hash =  hash.read().split()
 

## Open the wordlist
with open("../example/wordlist.txt","r", encoding="latin-1") as wordlist:

    raw_words = wordlist.read().split()
    
    ## Initialize the Queue
    test_words = Queue()

    ## Increment the Queue with passwords of the wordlist
    for word in raw_words:
        test_words.put(word)
    

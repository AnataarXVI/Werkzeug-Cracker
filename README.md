<a target="_blank" href="https://img.shields.io/badge/platform-linux-success.svg" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/platform-linux-success.svg">
</a>
<a target="_blank" href="https://img.shields.io/badge/platform-windows-success.svg" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/platform-windows-success.svg">
</a>
<a target="_blank" href="https://img.shields.io/badge/version-1.0.0-yellow" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/version-1.0.0-yellow">
</a>
<a href="https://www.python.org/" rel="nofollow">
    <img src="https://img.shields.io/badge/python-3.10-red">
</a>

Werkzeug Cracker
=========

Werkzeug Cracker is being developped by [@Anataar](https://github.com/AnataarXVI)


Installation & Usage
------------

```bash
git clone https://github.com/AnataarXVI/werkzeug_cracker.git
cd werkzeug_cracker
pip3 install -r requirements.txt
```

Options
------------

```bash
usage: werkzeug_cracker.py [-h] [-p PASSWORD] [-w WORDLIST] [-t THREADS]

Werkzeug hash cracker

options:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
                        load hash file
  -w WORDLIST, --wordlist WORDLIST
                        load wordlist file
  -t THREADS, --threads THREADS
                        number of threads, default=15

Example:
        werkzeug_cracker.py -p [hash] -w [wordlist] -t [threads]
```

How to use
------------

```bash
python3 werkzeug_cracker.py -p hash.txt -w wordlist.txt
```

Threads
------------

The thread number **(-t | --threads)** reflects the number of separated brute force processes. The more you increase the number of threads, the more the brute force will increase its speed. By default, the number of threads is 15, but you can increase it if you want to speed up the progress.

```bash
python3 werkzeug_cracker.py --password hash.txt --wordlist wordlist.txt -t 20
```

Licence
------------

Copyright (C) Anataar (anataar@protonmail.com)

License: GNU General Public License, version 3

Contributing
------------

If you liked the project, feel free to share it. I'm open to any suggestions for improvement.
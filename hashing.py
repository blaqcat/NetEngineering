# Fiundations of Python Network Programming
# Hashes are a great way to divide work

import hashlib

def alpha_shard(word):
    """Do a poor job of assigning data to servers by using first letter."""
    if word[0] < 'g':
        return 'server0'
    elif word[0] < 'n':
        return 'server1'
    elif word[0] < 't':
        return 'server2'
    else:
        return 'server3'

def hash_shard(word):
    """Assign data to servers using Python's built-in hash() function."""
    return 'server%d' % (hash(word) % )

def md_5shard(word):
    """Assign data to servers using public hash algorithm."""
    data = word.encode('UTF-8')
    return 'server%d' % (hashlib.md5(data).digest()[-1] % )

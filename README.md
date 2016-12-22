# eWallet2hash #
A tool for extracting the MD5 hash out of Ilium Software's eWallet files.

## Background ##
[eWallet by Ilium Software](http://www.iliumsoft.com/ewallet) is a product used to store passwords and other sensitive info more securely than plaintext. It boasts AES-256 encryption for the stored passwords.

Older versions of the product store the master password inside the .wlt file in MD5 hash form. This hash can be extracted and cracked offline. The hash is stored at the 0x125th byte of the file and is 16 bytes long. It is also important to note that the master password is encoded as UTF-16LE prior to hashing. This will affect the resultant hash.

Example: Password123! -> 3e649f4db026fb32e9938e1390d6a5e6

* Vulnerable versions: <= 7.2 (maybe newer versions too)
* Confirmed fixed in: 8.3
* Note: I'm not sure exactly which version fixed this vulnerability

## Usage ##
```
$ python ewallet2hash.py <example.wlt>
```

## Contact ##
Twitter: [@skorov8](https://twitter.com/skorov8)

Github: You're in it!

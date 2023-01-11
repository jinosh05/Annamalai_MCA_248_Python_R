import hashlib
import os
cwd = os.getcwd()


def find_hash(filename):
    # Create a hash Object
    h_o = hashlib.sha1()
    # open the data in binary mode
    with open(filename, 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h_o.update(chunk)
            # return the hex representation of digestr
            return h_o.hexdigest()


imgPath = os.path.join(cwd, 'image.jpg')
message = find_hash(imgPath)
print(message)

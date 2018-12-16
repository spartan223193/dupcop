import os
import sys
import hashlib

def hashfile(fpath):
    fhash = hashlib.sha1()
    with open(fpath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            fhash.update(chunk)
    return fhash.hexdigest()

def main():
    for dirpath, dirnames, files in os.walk(os.path.normpath(sys.argv[1])):
        for f in files:
            if "{}.html".format(f) in files:
                html_path = os.path.join(dirpath, "{}.html".format(f))
                norm_path = os.path.join(dirpath, f)
    
                html_hash = hashfile(html_path)
                norm_hash = hashfile(norm_path)

                if html_hash == norm_hash:
                    print("Removing {}".format(html_path))
                    os.remove(html_path)

if __name__ == '__main__':
    main()


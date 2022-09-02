import hashlib

filename = input("Nombre del archivo")
md5_hash = hashlib.md5()
with open(filename, "rb") as f:
    for byte_block in iter(lambda: f.read(4096), b""):
        md5_hash.update(byte_block)
    print(md5_hash.hexdigest() )


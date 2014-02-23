
def hsh(h):
    import hashlib

    for r in range(1000000):
        h = hashlib.sha384(str(h)).hexdigest()

    return h
    
for x in range(1000,1050):
	print hsh(x)


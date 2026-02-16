import base64

b64 = "S1lJXwIXSR0mDE0BTjALXExeTBsmBBdfDgEmDBVcTR0NXAEbBA=="
ct = base64.b64decode(b64)

known = b"2600{"  # on suppose que le message commence par ça
key = bytes([c ^ p for c, p in zip(ct[:len(known)], known)])

def xor_repeat(data, key):
    out = bytearray()
    for i, b in enumerate(data):
        out.append(b ^ key[i % len(key)])
    return bytes(out)

pt = xor_repeat(ct, key)
print(pt.decode(errors="ignore"))
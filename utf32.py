# Module for UTF-32 encoding

BIG_ENDIAN = 0
LITTLE_ENDIAN = 1

UTF32_MAXIMUM_CODEPOINT = 0xffffffff


def utf32_encode(codepoint, endianes=BIG_ENDIAN):
    """ Encode unicode codepoint in UTF-32 encoding"""
    assert 0 <= codepoint <= UTF32_MAXIMUM_CODEPOINT
    encoded_symbol = bytearray()
    d = codepoint
    while d != 0:
        d, m = divmod(d, 256)
        if endianes == BIG_ENDIAN:
            encoded_symbol.insert(0, m)
        else:
            encoded_symbol.append(m)
    for _ in range(4 - len(encoded_symbol)):
        if endianes == BIG_ENDIAN:
            encoded_symbol.insert(0, 0)
        else:
            encoded_symbol.append(0)
    return encoded_symbol

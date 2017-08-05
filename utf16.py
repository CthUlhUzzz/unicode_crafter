# Module for UTF-16 encoding

from .unicode import compute_surrogates_codepoints

UTF16_MAXIMUM_CODEPOINT = 1112063

BIG_ENDIAN = 0
LITTLE_ENDIAN = 1

MAXIMUM_WORD_CODEPOINT = 0xffff


def encode_word(codepoint, endianes):
    """ Encode 2-byte word """
    assert 0 <= codepoint <= MAXIMUM_WORD_CODEPOINT
    encoded_word = bytearray()
    d = codepoint
    while d != 0:
        d, m = divmod(d, 256)
        if endianes == BIG_ENDIAN:
            encoded_word.insert(0, m)
        else:
            encoded_word.append(m)
    for _ in range(2 - len(encoded_word)):
        if endianes == BIG_ENDIAN:
            encoded_word.insert(0, 0)
        else:
            encoded_word.append(0)
    return encoded_word


def utf16_encode(codepoint, endianes=BIG_ENDIAN):
    """ Encode unicode codepoint in UTF-16 encoding """
    result = b''
    assert 0 <= codepoint <= UTF16_MAXIMUM_CODEPOINT
    encoded_symbol = b''
    if codepoint <= 0xffff:
        encoded_symbol += encode_word(codepoint, endianes)
    else:
        for surrogate in compute_surrogates_codepoints(codepoint):
            encoded_symbol += encode_word(surrogate, endianes)
    result += encoded_symbol
    return result

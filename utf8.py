# Module for UTF-8 encoding

from collections import OrderedDict

UTF8_MASKS = {2: b'\xc0\x80',
              3: b'\xe0\x80\x80',
              4: b'\xf0\x80\x80\x80',
              5: b'\xf8\x80\x80\x80\x80',
              6: b'\xfc\x80\x80\x80\x80\x80'}

UTF8_MAXIMUM_CODEPOINTS = OrderedDict(((127, 1),
                                       (2047, 2),
                                       (65535, 3),
                                       (2097151, 4),
                                       (67108863, 5),
                                       (2147483647, 6)))

UTF8_MAXIMUM_CODEPOINT = 2147483647


def get_minimum_length(codepoint):
    """ Compute minimal count of bytes for encoding """
    for max_codepoint in UTF8_MAXIMUM_CODEPOINTS:
        if codepoint <= max_codepoint:
            return UTF8_MAXIMUM_CODEPOINTS[max_codepoint]


def construct_utf_8_symbol_mask(codepoint, length):
    """ construct mask for encoding codepoint """
    assert length >= 2
    mask = bytearray()
    d = codepoint
    while d != 0:
        d, m = divmod(d, 64)
        mask.insert(0, m)
    for _ in range(length - len(mask)):
        mask.insert(0, 0)
    return mask


def utf8_encode(codepoint, length=None):
    """ Encode unicode codepoint in UTF-16 encoding with length """
    encoded_symbol = b''
    if length == 1:
        encoded_symbol += bytes([codepoint])
    else:
        symbol_mask = construct_utf_8_symbol_mask(codepoint, length)
        for i in range(length):
            encoded_symbol += bytes([UTF8_MASKS[length][i] + symbol_mask[i]])
    return encoded_symbol

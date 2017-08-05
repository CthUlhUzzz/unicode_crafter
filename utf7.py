# Module for UTF-7 encoding

from base64 import b64encode

from utf16 import utf16_encode, UTF16_MAXIMUM_CODEPOINT

DIRECT_CHARACTERS = '\'(),-./:?'
UTF7_MAXIMUM_CODEPOINT = UTF16_MAXIMUM_CODEPOINT


def utf7_encode(codepoints, direct_characters=DIRECT_CHARACTERS):
    assert '+' not in direct_characters
    result_str = b''
    for i in codepoints:
        to_encode_str = []
        # if codepoint <= 127
        if i <= 0x7f:
            # if char not '+' and not in direct_characters
            if i != 0x2b and chr(i) not in direct_characters:
                to_encode_str.append(i)
            else:
                result_str += chr(i).encode('ascii')
        else:
            if to_encode_str:
                result_str += b'+' + b64encode(utf16_encode(to_encode_str)).rstrip(b'=') + b'-'
                to_encode_str = []

        if to_encode_str:
            result_str += b'+' + b64encode(utf16_encode(to_encode_str)).rstrip(b'=') + b'-'
        return result_str

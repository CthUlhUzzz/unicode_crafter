LOW_SURROGATES_MASK = 0xd800
HIGH_SURROGATES_MASK = 0xdc00

BOM_SYMBOL = 0xfeff

SURROGATES_RANGE = range(0xd800, 0xe000)

MAXIMUM_PYTHON_CODEPOINT = 0x10ffff


def compute_surrogates_codepoints(codepoint):
    surrogates = []
    d = codepoint - 65536
    assert 0 <= d <= 1048576
    while d != 0:
        d, m = divmod(d, 1024)
        surrogates.insert(0, m)
    for _ in range(2 - len(surrogates)):
        surrogates.insert(0, 0)
    surrogates[0] += LOW_SURROGATES_MASK
    surrogates[1] += HIGH_SURROGATES_MASK
    assert 0xd800 <= surrogates[0] <= 0xdbff and 0xdc00 <= surrogates[1] <= 0xdfff
    return surrogates

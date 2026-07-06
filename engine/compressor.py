import zlib


def compress_data(data):
    return zlib.compress(
        data,
        level=9
    )


def decompress_data(data):
    return zlib.decompress(
        data
    )
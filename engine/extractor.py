SIGNATURE = b"FILEFUSION_START"


def extract_file(file_path, output_path):

    with open(
        file_path,
        "rb"
    ) as f:

        data = f.read()


    position = data.find(
        SIGNATURE
    )


    if position == -1:
        raise Exception(
            "No hidden file found"
        )


    start = (
        position +
        len(SIGNATURE)
    )


    size = int.from_bytes(
        data[start:start+8],
        "big"
    )


    zip_start = start + 8


    hidden = data[
        zip_start:
        zip_start + size
    ]


    with open(
        output_path,
        "wb"
    ) as out:

        out.write(hidden)


    return output_path
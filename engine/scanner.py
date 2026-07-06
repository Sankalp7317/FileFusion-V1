import io
import json
import zipfile

from engine.crypto import decrypt_data
from engine.compressor import decompress_data



SIGNATURE=b"FILEFUSION_V6"



def scan_file(
        file,
        password
):


    with open(
        file,
        "rb"
    ) as f:

        data=f.read()



    index=data.find(
        SIGNATURE
    )



    if index==-1:

        raise Exception(
            "No FileFusion data found"
        )



    start=index+len(
        SIGNATURE
    )



    salt=data[
        start:start+16
    ]



    size_start=start+16



    size=int.from_bytes(

        data[
        size_start:
        size_start+8
        ],

        "big"
    )



    encrypted=data[

        size_start+8:
        size_start+8+size

    ]



    decrypted=decrypt_data(

        encrypted,
        password,
        salt

    )



    original=decompress_data(
        decrypted
    )



    archive=zipfile.ZipFile(

        io.BytesIO(
            original
        )

    )



    metadata=json.loads(

        archive.read(
            "filefusion_metadata.json"
        )

    )



    return metadata
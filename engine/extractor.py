import io
import json
import zipfile

from engine.crypto import decrypt_data
from engine.compressor import decompress_data



SIGNATURE=b"FILEFUSION_V6"



def extract_file(
        file,
        folder,
        password,
        progress=None
):


    if progress:
        progress(10)



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
            "Not a FileFusion file")



    if progress:
        progress(30)



    start=index+len(
        SIGNATURE
    )



    salt=data[
        start:
        start+16
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



    if progress:
        progress(55)



    decrypted=decrypt_data(

        encrypted,
        password,
        salt

    )



    original=decompress_data(
        decrypted
    )



    zip_data=zipfile.ZipFile(

        io.BytesIO(
            original
        )

    )



    metadata=json.loads(

        zip_data.read(

            "filefusion_metadata.json"

        )

    )



    print(
        metadata
    )



    zip_data.extractall(
        folder
    )



    if progress:
        progress(100)


    return metadata
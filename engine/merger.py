from engine.crypto import encrypt_data
from engine.compressor import compress_data
from engine.packer import pack_path


SIGNATURE=b"FILEFUSION_V6"



def merge_files(
        video,
        hidden,
        output,
        password,
        progress=None
):


    if progress:
        progress(10)


    data=pack_path(
        hidden
    )


    if progress:
        progress(35)


    data=compress_data(
        data
    )


    if progress:
        progress(55)



    salt,encrypted=encrypt_data(
        data,
        password
    )


    if progress:
        progress(75)


    with open(output,"wb") as out:


        with open(video,"rb") as v:

            while chunk:=v.read(1024*1024):

                out.write(chunk)



        out.write(
            SIGNATURE
        )

        out.write(
            salt
        )


        out.write(
            len(encrypted)
            .to_bytes(
                8,
                "big"
            )
        )


        out.write(
            encrypted
        )


    if progress:
        progress(100)
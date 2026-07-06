import os
import zipfile
import tempfile
import json
from datetime import datetime



def get_size(path):

    if os.path.isfile(path):

        return os.path.getsize(
            path
        )


    total=0


    for root,dirs,files in os.walk(path):

        for file in files:

            total+=os.path.getsize(

                os.path.join(
                    root,
                    file
                )

            )


    return total




def pack_path(path):


    temp=tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".zip"
    )


    temp.close()



    metadata={

        "name":os.path.basename(path),

        "type":
            "folder"
            if os.path.isdir(path)
            else "file",

        "size":get_size(path),

        "created":datetime.now()
        .strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "version":"FileFusion V6"

    }



    with zipfile.ZipFile(

        temp.name,
        "w",
        zipfile.ZIP_DEFLATED

    ) as zipf:



        zipf.writestr(

            "filefusion_metadata.json",

            json.dumps(
                metadata,
                indent=4
            )

        )



        if os.path.isfile(path):


            zipf.write(

                path,

                os.path.basename(path)

            )



        else:


            folder=os.path.basename(
                path
            )


            for root,dirs,files in os.walk(path):


                for file in files:


                    full=os.path.join(
                        root,
                        file
                    )


                    rel=os.path.relpath(

                        full,

                        os.path.dirname(
                            path
                        )

                    )


                    zipf.write(

                        full,
                        rel

                    )



    with open(
        temp.name,
        "rb"
    ) as f:

        data=f.read()



    os.remove(
        temp.name
    )



    return data
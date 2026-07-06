from pathlib import Path


SIGNATURE = b"FILEFUSION_START"


def merge_files(video_path, zip_path, output_path):

    with open(output_path, "wb") as output:

        with open(video_path, "rb") as video:
            output.write(video.read())


        output.write(SIGNATURE)


        with open(zip_path, "rb") as archive:

            data = archive.read()

            size = len(data)

            output.write(
                size.to_bytes(
                    8,
                    "big"
                )
            )

            output.write(data)


    return output_path
import sys
import os



def resource_path(path):

    try:

        base_path=sys._MEIPASS


    except Exception:


        base_path=os.path.abspath(
            "."
        )


    return os.path.join(
        base_path,
        path
    )
import json
import os


FILE = "filefusion_history.json"



def load_history():

    if not os.path.exists(FILE):

        return {
            "merged": [],
            "extracted": []
        }


    with open(FILE,"r") as f:

        return json.load(f)




def save_history(history):

    with open(FILE,"w") as f:

        json.dump(
            history,
            f,
            indent=4
        )




def add_history(
        category,
        path
):

    history=load_history()


    if path in history[category]:

        history[category].remove(
            path
        )


    history[category].insert(
        0,
        path
    )


    history[category]=history[category][:10]


    save_history(
        history
    )
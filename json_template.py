import json
import os
import pprint

#This is the template to create a JSON file readable by the code and that contains the needed information
#of a music. I do make these by hand and after save the file using the last two lines

"""for arquivo in os.listdir("./"):
    with open(arquivo, "r") as info:
        try:
            musica = json.load(info)
        except:
            continue
        pprint.pprint(musica)
exit()"""

json_data = {
"name": "Name of the music here",
"artist": "Guns N’ Roses",
"album": "Name of the album which contains the music here",
"cover": False,
"cover_info":
    {
    "artist": "if song is a cover, name of the original artist"
    "links": ["links to original content"]
    }
"links": ["links to listen to the music"],
"lyrics": """break every verse with a \n""",
"combinations": ["some parts of the lyrics that can have more than one verse"]
}

with open(f"{json_data['name']}.json", "w") as file:
    file.write(json.dumps(json_data))

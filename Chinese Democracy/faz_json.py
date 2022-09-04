import json
import os
import pprint

json_data = {
"name": "Prostitute",
"artist": "Guns N’ Roses",
"album": "Chinese Democracy",
"cover": False,
"links": ["https://open.spotify.com/track/7oSmXhr5DtJ6GLX8tABkyY" ,"https://youtube.com/watch?v=QELsjWL5WeU"],
"lyrics":
"""Seems like forever and a day
Please be kind
I’ve done all I should
I won’t ask of you What I would not do
Oh, I saw the damage in you
I had to pull through
Oh, I, I got a message for you
What would you say If I told you that I’m to blame?
And what would you do If I had to deny your name?
Where would you go if I told you "I love you"
I told you when I found you
If there were doubts you Should be careful and unafraid
Perversion and pain
""",
"combinations": [
"If my intentions are misunderstood\nPlease be kind",
"If my intentions are misunderstood\nPlease be kind\nI’ve done all I should",
"I won’t ask of you\nWhat I would not do\nOh, I saw the damage in you",
"Why would they\nTell me to please those\nThat laugh in my face\nWith all of the reasons\nThey’ve taught\nFall over themselves\nTo give way, oh yeah",
"Why would they\nTell me to please those\nThat laugh in my face",
"It’s not a question\nWhether my heart is true\nStreamlined\nI had to pull through",
"Give what you have\nFor what you might lose",
"What would you say\nIf I told you that I’m to blame?\nAnd what would you do\nIf I had to deny your name?",
"Where would you go if I told you\n\"I love you\"\nAnd then walk away? Oh yeah",
"What would you say\nIf I told you that I’m to blame?\nAnd what would you do\nIf I had to deny your name?\nWhere would you go if I told you\n\"I love you\"\nAnd then walk away?",
"N’ who should I turn to\nIf not for the ones\nThat you would not save?",
"I told you when I found you\nIf there were doubts you\nShould be careful and unafraid\nNow\nThey surround you",
"Is love that you fed by\nPerversion and pain",
"So if my affections\nAre misunderstood\nAnd you decide\nI’m up\nTo no good\nDon’t ask me to\nEnjoy them\nJust for you",
"Don’t ask me to\nEnjoy them\Just for you",
"Ask yourself\nWhat I would choose",
"Ask yourself\nWhat I would choose\nTo prostitute myself\nTo live with fortune and shame",
"When you should\nHave turned to the hearts\nOf the ones\nThat you could not save, oh now",
"I told you when I found you\nAll that amounts too\nIs love that you fed by\nPerversion and pain"
]
}

with open(f"{json_data['name']}.json", "w") as file:
    file.write(json.dumps(json_data))

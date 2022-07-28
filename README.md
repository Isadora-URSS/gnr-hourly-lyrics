# Guns N' Roses Hourly Lyrics
Disclaimer: I'M NOT, BY ANY WAY, RELATED OR AFFILIATED TO THE GUNS N' ROSES BAND, AND I WOULD FREELY REMOVE MY APP FROM RUNNING IF NEEDED TO DO SO.

This repo contains the code for the Twitter bot @gnrhourlybot. This bot posts some random verses
from Guns N' Roses musics into the Twitter plataform. Since this project was started in a recent
time, only lyrics from their album Appetite for Destruction are supported, but all their musics
(even the ones from Chinese Democracy) will be added into the future.

#### Running and Forking
If you,by any reason, wants to run a copy of this bot, maybe with different lyrics, here is the
informations you need:
The required libs for running this are `requests`, `schedule` and optionally `python_dotenv`. You
will also need an app with elevated acess on the Twitter plataform, since the endpoints used for
posting the tweets here are protected fromthe standart acess level of the API. (I think there are
alternatives tho, but I didn't explore them)

Music lyrics and metadata are stored in json files, since this is the best way I found to mantain them.
You can find a file with a template here in the repo under the name of `json_template`.

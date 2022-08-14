# Guns N' Roses Hourly Lyrics
Disclaimer: I'M NOT, BY ANY WAY, RELATED OR AFFILIATED TO THE GUNS N' ROSES BAND, AND I WOULD FREELY REMOVE MY APP FROM RUNNING IF NEEDED TO DO SO. THE OPINIONS FOUND IN VERSES DOESN'T NECESSARELY REFLECTS MY OPINION.

This repo contains the code for the Twitter bot @gnrhourlybot. This bot posts some random verses
from Guns N' Roses musics into the Twitter plataform. Please feel free to post a issue or make a
pull request with any code or lyrics change that you think it's pertinent.

## Album Coverage - Roadmap

- [x] Appetite for Destruction

- [x] G N' R Lies

- [x] Use Your Illusion I

- [x] Use Your Illusion II

- [ ] Chinese Democracy

- [ ] The Spaghetti Incident?

- [ ] Leaked songs and demos

#### Running and Forking
If you,by any reason, wants to run a copy of this bot, maybe with different lyrics, here is the
informations you need:
The required libs for running this are `requests`, `schedule` and optionally `python_dotenv`. You
will also need an app with elevated acess on the Twitter plataform, since the endpoints used for
posting the tweets here are protected from the standard acess level of the API. (I think there are
alternative endpoints tho, but I didn't explore them)

Music lyrics and metadata are stored in json files, since this is the best way I found to mantain them.
You can find a file with a template here in the repo under the name of `json_template`.

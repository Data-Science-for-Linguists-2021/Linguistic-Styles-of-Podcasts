# Linguistic-Styles-of-Podcasts
Abby Caffas  |  abc81@pitt.edu  |  Spring 2021

### Welcome to my Data Science for Linguists Term Project! 
In this project, I hoped to gather linguistic data through analysis of podcast transcripts, and compare stylistic differences across multiple human-inferred attributes (such as genre, rating, format, etc.).  Using Scrapy, I was able to extract episode transcripts from 20 different podcasts:
- [This American Life](https://www.thisamericanlife.org/archive) - _731 episodes_
- [Radiolab](https://www.wnycstudios.org/podcasts/radiolab) - _192 episodes_
- [Welcome to Nightvale](http://www.nightvalepresents.com/transcripts) - _168 episodes_
- [Move Your DNA](https://www.nutritiousmovement.com/category/podcast-transcripts/) - _104 episodes_
- [The Allusionist](https://www.theallusionist.org/transcripts) - _97 episodes_  ***
- [Bullseye with Jesse Thorn](https://maximumfun.org/transcripts/) - _63 episodes_
- [My Brother, My Brother, and Me](https://maximumfun.org/transcripts/) - _32 episodes_
- [Sawbones](https://maximumfun.org/transcripts/) - _30 episodes_
- [One Bad Mother](https://maximumfun.org/transcripts/) - _29 episodes_
- [Wonderful](https://maximumfun.org/transcripts/) - _29 episodes_
- [Friendly Fire](https://maximumfun.org/transcripts/) - _28 episodes_
- [The Greatest Generation](https://maximumfun.org/transcripts/) - _28 episodes_
- [Judge John Hodgman](https://maximumfun.org/transcripts/) - _28 episodes_
- [Shmanners](https://maximumfun.org/transcripts/) - _28 episodes_
- [NeoScum](https://neoscum.com/transcriptions) - _20 episodes_
- [The Adventure Zone](https://maximumfun.org/transcripts/) - _19 episodes_
- [The Flophouse](https://maximumfun.org/transcripts/) - _16 episodes_
- [Switchblade Sisters](https://maximumfun.org/transcripts/) - _14 episodes_
- [You're Wrong About](https://www.buzzsprout.com/1112270) - _13 episodes_
- [Unlocking Us](https://brenebrown.com/unlockingus/) - _12 episodes_

[Access my spiders here](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/tree/main/spiders).
Though I developed a working Scrapy module, I was unable to use data scraped for the following podcasts for copyright reasons (I did not receive a response for my request to use the data):
- 99% Invisible
- Freakonomics
- Lore
- On Being
- StoryCorps


[Access my main dataframe here](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/blob/main/data.ipynb), as well as [one that I was able to parse out host speech from](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/blob/main/data.ipynb) thanks to consistent text formatting and [one to be used for linear regression measuring language change over time](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/blob/main/this_american_life.ipynb) at a later date.  


[Access my machine learning models here](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/tree/main/Machine%20Learning), as well as the [resulting figures](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/tree/main/Figures).  

NOTE:  This is my first foray into machine learning, data science, web scraping, and text processing.  All findings and analysis are for exploratory purposes only.  In the future, I intend to use this data for sociolinguistic discourse analysis and syntax parsing.

Thank you for visiting my term project!  Feel free to leave feedback in my [guestbook](https://github.com/Data-Science-for-Linguists-2021/Class-Lounge/blob/main/guestbooks/guestbook_abby.md)
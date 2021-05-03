Abby Caffas
Ling 1340
Final report


**(sidenote:  Hi Na-Rae. I'm sorry, but my main jupyter notebook, data.ipynb, does not have a table of contents and links.  Initially, I followed the directions for linking and had it working and cleaned up the dataframe for about 2 hours, then made sure to save it SEVERAL TIMES locally.  I committed my changes, and when I went to open it again, everything I did was gone.  So I'm really sorry about that, but I simply can't spend another hour on cleaning and organizing.)

## 1.  Introduction

As of April 2021, there are 48 million podcast episodes available across several different platforms, including Spotify, iTunes, and Pocket Casts.  The popularity of podcasts has skyrocketed within the last 10 years, and I hav personally found them to be a very reliable source of comfort throughout the coronavirus pandemic.  No matter your interests, you can find a podcast that is uniquely suited to you.  Because of the amazing genre- and topic-range available with podcasts -- and also because they are free to access if you have a phone or an internet connection -- I think that podcasting will become a very integral part of everyone's lives in the year to come.

I chose podcasts as my subject not only because they serve as a pressure-free simulation of human interaction for the socially awkward like me, but also because they, or at least specific genres, seem to most reflect casual, free-flowing conversation.  Though I really would have liked to compare linguistic styles of podcasts with corpora of real-life, unfiltered conversation, the fact that this project was my first foray into data science, machine learning, data organization, and web scraping meant that most of my time was spent solving syntactic riddles, parsing data frames, fighting with regular expressions, and figuring out how to work on Pitt's center for research computing.  I will most likely expand on this project in the future with an aim in making some sociolinguistic discoveries, but I did manage to uncover some interesting correlations between textual features in podcast transcripts.

I completed this project in three main steps.  First, I used Scrapy to extract transcript text from podcast websites.  Then, I built a dataframe with descriptive, human-assigned target features, lexical features, and about 50 non-lexical features.  Then, I exported the dataframe to the center for research computing to allow for fast processing of large swaths of data in machine learning models.  Overall, my dataframe contained about 1500 episodes with upwards of 10 million individual tokens, so a lot of processing power was an absolute must.

## 2.  Dataset and Analysis

Overall, there are a disappointingly small amount of podcasts with official transcripts available, compared to how many total podcasts are out there.  However, I was able to scrape 1500+ episodes, parsed down to about 1400 because the text didn't come through.  Using scrapy, I attempted to extract the podcast name, year released, episode title, episode number, and transcript text in order to use as target variables.  However, only about 520 episodes had years in the transcript html, and about 1/3 didn't have an episode number.  That was somewhat disappointing because I wanted to train a model to track language change over time - but the sample set just wasn't large enough (also, the episodes that did have a year were mostly 2020, not enough to contrast any values).  

Also, podcasts that did have transcripts available frequently had far fewer than I thought they would.  Podcasts with an episode backlog of 500+ only have about 50 transcripts, for instance.  With the exception of This American Life, which goes above and beyond in providing consistent and accessible transcripts, all of the transcripts suffered from inconsistent formatting and just overall lack of data.  After scrapping a few spiders because of copyright issues, here were my episode counts:

![Episode counts](Figures/episode_counts.png)


One podcast network, Maximum Fun, had several of their podcast transcripts only as embedded pdfs.  I found a very useful library called pdfplumber, but it would not install in Anaconda.  I was able to use Scrapy to pickle the pdf download links, then download each pdf with a for loop in IDLE - saving it to "current pdf" , then using pdfplumber to extract the text and save it to a csv along with the podcast name.  This took a lot of time, but I thought it was important, considering that the pdfs had consistent formatting that would later allow me to parse hosts (see [this dataframe](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/blob/main/mcelroy_podcasts.ipynb)).  

After getting the basics - text, episode, podcast, episode title, and year - I manually made a dictionary of descriptive features that could be used as targets.  Among them were genre, format, # of hosts, etc.  I combined my manual feature dictionary with each podcast's year and episode.  After that, I did a bit of cleaning with regex.  I used spacy's tokenizer, which cleaned up the text pretty well.  Using the tokens, I extracted about 50 non-lexical features, many of which I didn't think would be very helpful in terms of classification, but I figured I would add them all in because why not?  Features included token count, average token length, TTR, average kband, part of speech frequency, average sentence length, part of speech length, pronoun frequency, frequency of several common verb lemmas, spacy's entity counts, opinion count (pronoun plus optional auxiliary plus the lemma think or feel), and prepositions per sentence (I think that this is a good reflection of sentence complexity).  In doing this, I made sure to minimize .maps that performed functions on the entire data frame.  For example, for the average part of speech length column, I iterated over the Tokens once, saving each pos length in a list of dictionary values with the POS as the key, and saved the entire dictionary as its own column.  Then, I did a kind of "get dummies" function, where each item in the dictionary was averaged out and got its own column, making it a usable column of floats.  I think this saved a lot of processing power.

## 3.  Machine Learning models

I separated the main dataframe into three separate dataframes: targets, lexical features, and non-lexical (numerical) features, and saved them as separate csvs.  I used scp to send those files to the crc, where I could (somewhat) easily and quickly try out A LOT of machine learning.  See my [figures](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/tree/main/Figures) and [machine learning code](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/tree/main/Machine%20Learning).  I tried both classification and regression models to predict podcast, year, rating, genre, topic, format, and host number.  While some of the results were surprising, some made complete sense.

The tfidf podcast classifier scored 100%, which is not surprising at all.  I did not redact "giveaway" terms like host names and podcast name, so the most informative features ended up being those obvious terms.  However, the regression classifier performed extremely well, at about a 98% accuracy.  I don't really have an explanation for that performance, as I didn't test each non-lexical feature's correlation against podcast.  

Both the year classifier and regressor performed horribly, at around 22%.  This was surprising, considering that it could have just guessed "2020" for all episodes and done better than 22%.  

Even with the data incredibly weighted in favor of This American Life, the other models performed very well, with all of the other targets achieving a 70%+ accuracy.  Considering the small sample size, though, features likely don't reflect properties of the actual target variable (i.e. genre), but of the podcast itself, since there were only one or two podcasts per target.  

Using linear regression, I tested each non-lexical feature against rating, results can be found [here](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/tree/main/Figures/non-lexical_features/rating_correlation).  The highest correlation values were only about 50-60%, and the features were verb length (as in how many letters on average a verb is), and exclamation frequency.  

## 4. Conclusion

This project proved to be extremely difficult.  Though I didn't make any true stylistic discoveries, I think the results so far are promising and the data gathered so far will provide a good foundation for further exploration.  I hope that more podcast transcripts will become available soon so that I can use a wider sample and perform a more accurate and complete analysis.  I think that, knowing I know now, what took me 50+ hours to complete will now only take me about 10, so things will be much easier going forward.  



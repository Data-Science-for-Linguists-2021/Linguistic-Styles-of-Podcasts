### Progress Report

### **1st Progress Report** - **03/04/21**

Data so far . . . 
- Maximum Fun Network (plaintext only, haven't gotten transcripts that are embedded pdfs yet)
- This American Life
- Welcome to Nightvale
- Move Your DNA
- Freakonomics
- Lore
- On Being
- 99% Invisible
- Story Corps

While this isn't a lot compared to my overall plan, most of my time was spent learning how to write spiders.  Now that I know how, I think I can realistically use 20-30 more podcasts.  I'm still going ahead with the original plan, but the data won't be quite as exhaustive as I originally planned - there will be two podcasts per genre.  I still need to find a way to scrape ratings from the apple podcasts website so they can be used for analysis.  An issue that I only just now realized is that poorly-rated podcasts don't tend to have transcripts, so the margins for rating differences may not be viable anyway.   I'll likely just analyze genre style differences.

I made a few very dirty csv files.  I'm getting reacquainted with regex - once I feel more comfortable with it, I'll incorporate regex selectors in the spider and try to filter out some of the ugliness.  I also have to change the way I saved all of the scraped data - it's done correctly in the "Invisible" ipynb in the folder "spiders". 

*Data Sharing*
After running the text through a parser, I'll be able to find what stylistic differences exist between genres.  I'd like to train a classifier based on the features I uncover, then run some made-up sentences through it.  I'll also make charts that show differences between genres, similar to Homework 2.


### **2nd Progress Report** - **03/22/21**
I have 11 clean dataframes - one dataframe for each podcast - with clean text and title information.  Some podcasts had date and episode# metadata that I was
able to scrape, so those columns are included when applicable.  I'm still working on cleaning the data from the maximum fun website, as some of the podcasts
have their transcripts as embedded pdfs.  Spiders can be found [here](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/tree/main/spiders).

Even without the Maximum Fun data, however, I have 1302 episodes total, which I have compiled into a multindexed dataframe (found [here](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/blob/main/data.ipynb)).  I'm going to do all the analysis in this consolidated dataframe, including 
all of the basic measurements included in Homework 2 (token count, word length, sentence length, etc), with some extra measurements like amount of "wh-" questions, 
host-to-host speaking ratio, etc.  I'd also like to revisit the nltk chartparser to break down sentence-structure tendencies, but that seems like a longshot as
of right now because I need a big refresher on that topic.

I'll then create a parsed-down dataframe with the averages of each podcast, along with podcast-specific labels like format, # of hosts, apple podcasts rating, 
and genre (also according to apple podcasts).  I don't have enough data to be able to pick out genre differences (only 1 or 2 of each genre), but I'll be 
able to run regression models on the data with rating as a target variable.  In compiling all this data, I came up with the idea of also possibly being able 
to extract the style/numbers of a certain hosts (i.e. Ira Glass from This American Life because there are a TON of those transcripts) and see if they have
certain episodes where their style changes dramatically (maybe they're talking about a subject that makes them particularly uncomfortable, or they're trying to sound cool because they have a young guest, etc etc). 

**Copyright**
I've applied a GNU general public license to my data/project.

- 99% Invisible
	-"In Your use of the Service, You will not . . . Use web crawlers, web robots, web scutters, ants, automatic indexers, bots, worms, and other such devices 	   in connection with the Service; provided, however, that general purpose Internet search engines and non-commercial public archives that use tools to 	   gather information for the sole purpose of displaying hyperlinks to the Service are granted a limited exception from the foregoing exclusion, provided    	   that they do so from a stable IP address or range of IP addresses using an easily-identifiable agent"   
	- I'm going to contact 99% Invisible to see if I can get authorization to use their material.  But until then, I'll move all the data to a private repo
- This American Life
	- "The Application must point directly to the Content as linked to and contained within our RSS feeds, and must not copy audio files to be hosted or served 	   by other servers. Without separate written permission, the Application may not pull or display any data or content apart from that included in the RSS 	   	   feeds - for example, the Application may not present images from our website, alternate logos, or program or episode descriptions written by a third 	   	   party." 
	- A lot about not using the material for promotional purposes or advertising, but otherwise I am okay to use the material as long as I don't alter the 	  	  content
- Lore
	- The official Lore website just says, "copyright (c) 2015-2021 Aaron Mahnke and *Lore*.  All rights reserved."  The transcripts, however, were written
	   and posted by a third party who attributes the content to Aaron Mahnke and Lore.  Am I violating the copyright by using those transcripts?
	- Move the data to a private repo until clarified
- On Being
	- "Except as otherwise provided herein, none of this Content may be used, copied, reproduced, distributed, republished, downloaded, modified, displayed, 	   posted, or transmitted in any form or by any means, including, but not limited to electronic, mechanical, photocopying, recording, or otherwise, without 	   our express, prior written permission."
	- That's pretty straightforward.  To a private repo awaiting permission it goes . . .
- Radiolab
	- "You may copy and print content for your personal, noncommercial use only, provided that you include all copyright and other notices contained in the 	  content and that you do not modify the content."
	- I modified the scraped text by removing the messy html tags, but otherwise left the content unmodified.
- [Story Corps](https://archive.storycorps.org/terms-of-use/)
	- All rights reserved.  Move to private.
- Unlocking Us
	- Prompt that appears when opening a transcript: "No one is authorized to copy any portion of the podcast content or use Brené Brown’s name, image or 	  likeness for any commercial purpose or use, including without limitation inclusion in any books, e-books, book summaries or synopses, or on a 
	  commercial website or social media site (e.g., Facebook, Twitter, Instagram, etc.) that offers or promotes your or another’s products or services."
	- I am okay to use this data, since I am not using it for commerical use
- Freakonomics
	- "All contents © 2021 Freakonomics, LLC. All rights reserved."
	- to a private repo . . . .
- No copyright information available online for the following:
	- Maximum Fun Network (the [terms and conditions](https://maximumfun.org/terms-conditions/) page is all in latin . . .)
	- Move Your DNA
	- Welcome to Nightvale
	- You're Wrong About


### **3rd Progress Report** - **04/13/2021**
I found another podcast with transcripts (Neoscum) and added it to the [consolidated dataframe](https://github.com/Data-Science-for-Linguists-2021/Linguistic-Styles-of-Podcasts/blob/main/data.ipynb).  Unfortunately, the transcripts were all fan-made and in Google documents in a Google drive, so I had to manually copy-paste the text (removing apostrophes and line breaks along the way) for 20 episodes.  It wasn't too time-consuming.

I dropped transcripts from the dataframe whose text is shorter than 6,500 characters, which kept all podcasts that were scraped correctly.

I spent about two hours doing the spacy tutorial on DataCamp, and I have a pretty good grasp of the basics. I'm using spacy's medium English model, but tokenizing still takes about 20 minutes.  I've tried many times to pickle the dataframe and transfer it to crc with no success (refer to the question in Teams), but I don't mind waiting the 20 minutes (I never have trouble finding something else to work on).

I made a dataframe with categorical data and non-lexical features, then joined it to the consolidated dataframe (to do this, I had to un-multi-index the text-ful dataframe, which was a bit of a headache).  The non-lexical features I chose were: hosts (regular hosts are a whole number, .5 represents a podcast that regularly has a guest on), genre-topic (originally just genre, but I didn't think that covered enough), scripted/unscripted, Fiction/Non, Format (interview, chat, etc), and rating.  I knew that all of the ratings would be relatively high - above 4.0 - but they're actually all above 4.6 on itunes.  This teeny-tiny margin likely won't allow me to be able to make claims about what makes a podcast "successful" raings-wise.  I'll run the model many times using different categorical aspects as targets and use get dummies to use other ones as features.

So far, text features that I could extract and add to the dataframe are: 
- Tokens = scrapy-parsed
- Top50 = 50 most commonly-occurring tokens
- Token_count = overall length of transcript including punctuation and anything that spacy's tokenizer considered a token
- Token_lengths = tuple with (str, int) as token, length.  Punctuation and non-alpha strings excluded
- Avg_token_len = average alpha token length over entire transcript
- TTR = this is a pure, uncorrected-for-length TTR.  I figured that if each transcript is over 6500 characters, there won't be a length issue. 
- kband = tuple with (str, int) as token-lemma, kband.  I was unsure if using the lemma is better, but my thinking is that it will be a more accurate reflection of rare-word use, since it's just the meaty-meaning-aspect of the word being rated
- Avg_kband = self-explanatory at this point.  Weighed against whole transcript.
- Bigrams = list of bigram tuples - only alpha strings
- Bigram_top25 = top 25 most common bigrams.  I was hoping this would help me find and parse the host's name
- POS = list of tuples: (token, POS)
- POS_freq = dictionary of percentage of entire transcript that each POS comprises
- Noun_freq, verb_freq, Adj_freq, Adv_freq = "dummified" stats from the POS_freq dictionary
- POS_length = dictionary containing average letter-length of nouns, verbs, adverbs, and adjectives
- Avg_noun_len, Avg_verb_len, Avg_adj_len, Avg_adv_len = "dummified" stats from teh POS_length dictionary
* will likely remove POS_freq and POS_length columns, just used them to make the other columns so that map() could just copy the info from the already-existing dictionary rather than run a function on every row for each POS
- verb_lemmas = top 20 verbs and what percentage of total verb occurrence they make up
- sentence_toks = nltk's sent tokenizer
- sentence_length = tuple (sentence, int).  Used nltk, so punctuation is excluded

Planning on adding:
- entity count using spacy's token.ent_ attribute
- "conversation hog" = percentage that each host talks
- probably more POS_freqs - include interjections, conjunctions, prepositions, etc
- favorite punctuation (I'm assuming that interview-formatted transcripts will win on the ? frequency) weighed against transcript length
- sweariness - make a dictionary of swear words and count-em, also make a dictionary of pseudo swear words (e.g. darn, fudge, shoot) and count em

Dataframe stats:
- podcasts (19):
	- This American Life           732
	- Radiolab                     261
	- Welcome to Nightvale         170
	- Move Your DNA                108
	- Bullseye with Jesse Thorn     63
	- MBMBaM                        32
	- Sawbones                      30
	- One Bad Mother                29
	- Wonderful                     29
	- Shmanners                     28
	- The Greatest Generation       28
	- Judge John Hodgman            28
	- Friendly Fire                 28
	- NeoScum                       20
	- The Adventure Zone            19
	- The Flophouse                 16
	- Switchblade Sisters           14
	- You're Wrong About            13
	- Unlocking Us                  12
Total of 1584 rows
18270894 tokens


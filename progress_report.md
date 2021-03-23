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
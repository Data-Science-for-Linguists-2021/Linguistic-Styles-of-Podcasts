# 3/4 - 1st Progress Report

## Data so far . . . 
### - Maximum Fun Network (plaintext only, haven't gotten transcripts that are embedded pdfs yet)
### - This American Life
### - Welcome to Nightvale
### - Move Your DNA
### - Freakonomics
### - Lore
### - On Being
### -99% Invisible
### -Story Corps

### While this isn't a lot compared to my overall plan, most of my time was spent learning how to write spiders.  Now that I know how, I think I can realistically use 20-30 more podcasts.  I'm still going ahead with the original plan, but the data won't be quite as exhaustive as I originally planned - there will be two podcasts per genre.  I still need to find a way to scrape ratings from the apple podcasts website so they can be used for analysis.  An issue that I only just now realized is that poorly-rated podcasts don't tend to have transcripts, so the margins for rating differences may not be viable anyway.   I'll likely just analyze genre style differences.

### I made a few very dirty csv files.  I'm getting reacquainted with regex - once I feel more comfortable with it, I'll incorporate regex selectors in the spider and try to filter out some of the ugliness.  I also have to change the way I saved all of the scraped data - it's done correctly in the "Invisible" ipynb in the folder "spiders". 

## Data Sharing
### After running the text through a parser, I'll be able to find what stylistic differences exist between genres.  I'd like to train a classifier based on the features I uncover, then run some made-up sentences through it.  I'll also make charts that show differences between genres, similar to Homework 2.
Project Plan
Make a primary DataFrame with the following columns: Podcast name, rating, network, 
	format (storytelling, chat, interview, news, gameplay, etc), # of (regular) hosts,
	and genre.  I'll try to use the iTunes rankings and stick to a release timeframe of 5 years.

Make secondary DataFrames for each podcast with the columns: episode title, release year, length (minutes), 
	and content (transcript).  Use nltk functions - word tokenize, sent tokenize, TTR, k-band, 
	word-length, tree parsing, POS annotation and implement vectors (I'm not sure in what 
	way to apply them yet) on episode titlesand transcripts.

Use the statistics library to test for correlation (i.e. Does a higher/lower TTR affect rating?
	Do comedy podcasts have more words per minute than educational ones?  Is there a linguistic
	style change from year to year?).

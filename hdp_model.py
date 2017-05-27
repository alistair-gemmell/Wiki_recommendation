import gensim

def return_model(new, update):
	# To Do: Work out a way to maybe update the topic list, or would I have to redownload the entire corpus and redo this every time?

	if new:
		# Take in the current Wikipedia article list from local disk
		# load id->word mapping (the dictionary), one of the results of step 2 above
		id2word = gensim.corpora.Dictionary.load_from_text('wiki_en_wordids.txt')
		# Load corpus iterator
		mm = gensim.corpora.MmCorpus('wiki_en_tfidf.mm')

		# Find the topics contained within the wikipedia articles, load these into my recommender
		hdp = gensim.models.hdpmodel.HdpModel(mm, id2word)

		# Save the model to disk so that we don't need to go through all this palava again
		hdp.save('hdp.model')
	else:
		# Load model from disk
		hdp = load('hdp.model')

	return hdp
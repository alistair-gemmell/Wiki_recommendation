import gensim
import logging

def return_model(method, topics=None, new=False):
	# To Do: Work out a way to maybe update the topic list, or would I have to redownload the entire corpus and redo this every time?

	defined_models = ('lda', 'hdp')
	if method not in defined_models:
		logging.error("Please specify one of the defined models ({0})".format(defined_models))

	if new:
		# Take in the current Wikipedia article list from local disk
		# load id->word mapping (the dictionary), one of the results of step 2 above
		id2word = gensim.corpora.Dictionary.load_from_text('wiki_en_wordids.txt')
		# Load corpus iterator
		mm = gensim.corpora.MmCorpus('wiki_en_tfidf.mm')

		# Find the topics contained within the wikipedia articles, load these into my recommender
		if method == 'lda':
			topic_model = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=topics, update_every=1, chunksize=10000, passes=1)
		elif method == 'hdp':
			if topics:
				logging.info("Number of topics have been specified for HDA -- ignoring this")
			topic_model = gensim.models.hdpmodel.HdpModel(corpus=mm, id2word=id2word)

		# Save the model to disk so that we don't need to go through all this palava again
		topic_model.save('{0}.model'.format(method))
	else:
		# Load model from disk
		topic_model = load('{0}.model'.format(method))

	return topic_model
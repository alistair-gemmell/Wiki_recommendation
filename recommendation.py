import hdp_model

import logging
import numpy
import os.path

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Get the topic models for the article list we have on disk
topic model = topic_model.return_model(method='lda', topics=400, new=False)

# If previous preferences have been saved, load them in, otherwise initialise randomly
if os.path.isfile('preferences'):
	preferences = load('preferences')
else:
	preferences = numpy.matrix(num_topics)

# Create a shortlist of recommendations, trying to give a selection of different topics

# To Do
# Other characteristics of articles that might be relevant
# E.g. Is it a starred article, the length

# Introduce an element of chance, to try and stop a re-inforcmement of previous recommendations

# Produce a recommendation of an article based on previous likes
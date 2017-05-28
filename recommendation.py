import topic_model

import logging
import numpy as np # Use this for the moment, maybe look at pandas in future?
import os.path

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Get the topic models for the article list we have on disk
num_topics = 400
topic model = topic_model.return_model(method='lda', topics=num_topics, new=False)

# If previous preferences have been saved, load them in, otherwise initialise randomly
if os.path.isfile('preferences'):
	preferences = load('preferences')
else:
	preferences = np.zeros(num_topics)

# Create a shortlist of recommendations, trying to give a selection of different topics
# To Do: FInd out how to find a list of the articles with their topics linked - preferably linking URL and human-readable title as well for nice presentation
num_recommendations = 20
# A dot product or something here to find the most similar 20 articles?  Need to filter this so that we don't recommend all the same thing!
# Look up how to do this with numpy
recommended_articles = preferences .* article_list[num_recommendations]

print(recommended_articles)

# To Do
# Other characteristics of articles that might be relevant
# E.g. Is it a starred article, the length

# Introduce an element of chance, to try and stop a re-inforcmement of previous recommendations

# Produce a recommendation of an article based on previous likes
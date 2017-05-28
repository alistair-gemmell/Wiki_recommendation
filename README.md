# Wiki_recommendation
A perhaps overly ambitious attempt to use Machine Learning to recommend new Wikipedia articles to me.

**This is currently completely metacode / untested, as it turns out getting the data to download is non-trivial and it crashes repeatedly**

Long term plan is to use topics, article length, whether or not the article has one of those gold stars etc to produce recommendations, with an element of random chance to prevent re-inforcing behaviour of this only suggesting an increasingly narrow range of topics.  It would also be nice to consider the topics of articles when making recommendations, so that you don't get a list of articles all on very similar topics (which would be a problem when you've only specified a few articles you like).  Maybe base initial recommendations on the ones that Wikipedia thinks are good?

Also would like to find a way to update on the fly -- so that new topics from Wikipedia can be folded into the set-up and included in the recommendations.  Long term, it would be nice if this could allow for new topics to emerge, but I don't know if there is a way to do this without recreating the entire model list.  Currently I'm writing this for Latent Dirichlet Allocation, as I've used that before.  This requires me to set the number of topics, which is a limitation, but currently allows  me to initialise matrices with the right number of topic vectors.  I think Wikipedia has enough training data for Hierarchical Dirichlet Process to be a viable method, but that means that I don't know how many topics to intialise the recommendation algorithms with, which would be a problem.  I also don't know how feasible it is to re-formulate those.

The current problem is that the Wikipedia download is huge and takes time to run over (the file that gensim recommends isn't the same as the torrents I can find), so I can't test this until I successfully manage to download it.  In the future I can see if they do a delta that I could maybe fold in?

Another nice thing would be making a web API so that you can add view the results easily, and perhaps immediately say yes or no to a new articles so that the preferences can be updated quicker

'''
Created on 2015. 5. 28.

@author: HJJeong
'''

from FeatureSelection.AuthorSimilarity import AuthorSimilairty
from FeatureSelection.AffiliationSimilarity import AffiliationSimilarity

class Feature:
    feature_dim = 2
    
    def __init__(self):
        pass
    
    def get_feature_vector(self, author_id, paper_id):
        authorSimilarity = AuthorSimilairty()
        affiliationSimilarity = AffiliationSimilarity()
        jaccard_sim = authorSimilarity.get_author_name_sim(author_id)
        affiliation_sim = affiliationSimilarity.getAffiliationSimilarity(author_id)
        
        feature_X = []
        feature_Y = []
        
        feature_X.append([jaccard_sim, affiliation_sim])
        feature_Y.append(1)
        return feature_X, feature_Y
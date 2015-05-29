'''
Created on 2015. 5. 28.

@author: HJJeong
'''
from FeatureSelection.FileProcessor import FileProcessor
from FeatureSelection.AuthorSimilarity import AuthorSimilairty
from FeatureSelection.AffiliationSimilarity import AffiliationSimilarity

if __name__ == '__main__':
    fileProcessor = FileProcessor()
    train_author_id_list = fileProcessor.get_train_author_id_list()
    authorSimilarity = AuthorSimilairty()
    affiliationSimilarity = AffiliationSimilarity()
    
    jaccard_sim = 0.0
    for author_id in train_author_id_list:
        jaccard_sim = authorSimilarity.get_author_name_sim(author_id)
        affiliationsim = affiliationSimilarity.getAffiliationSimilarity(author_id)
    #print 'final jaccard_sim'+str(jaccard_sim)
    print 'aff sim'+str(affiliationsim)
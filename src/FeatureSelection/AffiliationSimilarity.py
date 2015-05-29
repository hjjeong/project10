'''
Created on 2015. 5. 28.

@author: HJJeong
'''
from FeatureSelection.JaccardSimilarity import JaccardSimilarity
from FeatureSelection.FileProcessor import FileProcessor

class AffiliationSimilarity(JaccardSimilarity):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        JaccardSimilarity.__init__(self)
        
    def getAffiliationSimilarity(self, author_id):
        fileProcessor = FileProcessor()
        affiliation_from_author = fileProcessor.get_affiliation_from_author(author_id)
        affiliation_from_author_paper = fileProcessor.get_affiliation_from_authorpaper(author_id)
        jaccard_sim = -1.0
        print 'aff_author '+affiliation_from_author+'len: '+str(len(affiliation_from_author))
        print 'aff_author_paper '+affiliation_from_author_paper+'len: '+str(len(affiliation_from_author_paper))
        jarccardSimilarity = JaccardSimilarity()
        if len(affiliation_from_author)!=0 or len(affiliation_from_author_paper)!=0:
            print 'a'
            jaccard_sim = jarccardSimilarity.compute_jaccard_sim(affiliation_from_author, affiliation_from_author_paper)
        return jaccard_sim
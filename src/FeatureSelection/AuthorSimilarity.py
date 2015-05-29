'''
Created on 2015. 5. 28.

@author: HJJeong
'''
from FeatureSelection.FileProcessor import FileProcessor
from FeatureSelection.JaccardSimilarity import JaccardSimilarity

class AuthorSimilairty(JaccardSimilarity):
    '''
    input: test author-paper pair
    output: matched author, similarity
    
    select first name
    switched name compare
    '''  
    trainfilepath = "D:\workspaceCouseWalk\author.csv"
    testfilepath = "D:\workspaceCouseWalk\author.csv"
    def __init__(self):
        JaccardSimilarity.__init__(self)
        
    def switch_author_name(self,author_name):
        author_split = author_name.split()
        switch_author_name = ""
        for i in range(len(author_split)):
            switch_author_name += author_split[len(author_split)-i-1]
            if i != len(author_split)-1:
                switch_author_name +=' '      
        return switch_author_name
    
    def abbreviate_author_name(self, author_name):
        #Alice Oh -> A. Oh
        author_name_split = author_name.split()
        #print 'author_name_split'+str(author_name_split)
        abbreviated_name = ""
        if len(author_name_split[0].split('.')[0]) != 1 and len(author_name_split[1].split('.')[0]) != 1:
            abbreviated_name+=author_name_split[0][0]
            abbreviated_name+='.'
            abbreviated_name+=' '
            for i in range(len(author_name_split[1])):
                abbreviated_name+=author_name_split[1][i]
        else:
            abbreviated_name = author_name    
        return abbreviated_name
    
    def get_author_name_sim(self,author_id):
        #train author id return -> how to match train_author_name
        fileProcessor = FileProcessor()
        name_from_author = fileProcessor.get_name_from_author(author_id)
        #print 'name_from_author:'+str(name_from_author)
        name_from_author_paper = fileProcessor.get_name_from_authorpaper(author_id)
        #print 'name_from_author_paper:'+str(name_from_author_paper)
        switched_name_from_author = self.switch_author_name(name_from_author)
        #print 'switched_name_from_author:'+str(switched_name_from_author)
        switched_name_from_author_paper = self.switch_author_name(name_from_author_paper)
        #print 'switched_name_from_author_paper:'+str(switched_name_from_author_paper)
        abb_name_from_author = self.abbreviate_author_name(name_from_author)
        #print 'abb_name_from_author:'+str(abb_name_from_author)
        abb_name_from_author_paper = self.abbreviate_author_name(name_from_author_paper)
        #print 'abb_name_from_author_paper:'+str(abb_name_from_author_paper)
        abb_swithced_name_from_author = self.abbreviate_author_name(switched_name_from_author)
        #print 'abb_swithced_name_from_author:'+str(abb_swithced_name_from_author)
        abb_swithced_name_from_author_paper = self.abbreviate_author_name(switched_name_from_author_paper)
        #print 'abb_swithced_name_from_author_paper:'+str(abb_swithced_name_from_author_paper)
        jarccardSimilarity = JaccardSimilarity()
        
        jaccard_sim = []
        jaccard_sim.append(jarccardSimilarity.compute_jaccard_sim(abb_name_from_author, abb_name_from_author_paper))
        jaccard_sim.append(jarccardSimilarity.compute_jaccard_sim(abb_name_from_author, abb_swithced_name_from_author_paper))
        jaccard_sim.append(jarccardSimilarity.compute_jaccard_sim(abb_name_from_author_paper, abb_swithced_name_from_author))
        jaccard_sim.append(jarccardSimilarity.compute_jaccard_sim(abb_swithced_name_from_author,abb_swithced_name_from_author_paper))
        print 'jaccard sim[0]'+str(jaccard_sim[0])
        print 'jaccard_sim[1]'+str(jaccard_sim[1])
        print 'jaccard_sim[2]'+str(jaccard_sim[2])
        print 'jaccard_sim[3]'+str(jaccard_sim[3])
        return max(jaccard_sim)
        
        
        
                
            
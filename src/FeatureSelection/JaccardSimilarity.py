'''
Created on 2015. 5. 28.

@author: HJJeong
'''

class JaccardSimilarity:
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    
    def compute_jaccard_sim(self, source, target):
        intersection_len = 0.0
        if(len(source)<len(target)):
            min = source
        else:
            min = target
             
        for i in range(len(min)):
            if target[i] == source[i]:
                intersection_len = intersection_len+1
        union_len = len(source)+len(target)-intersection_len
        return intersection_len/union_len
    

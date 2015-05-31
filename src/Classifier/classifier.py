import numpy as np
np.random.seed(0)

from sklearn.ensemble import RandomForestClassifier
from FeatureSelection.FileProcessor import FileProcessor
from FeatureSelection.Feature import Feature

def computeMAP(forest):
    fValid = open("../../data/Valid.csv", 'r')
    fValidSol = open("../../data/ValidSolution.csv", 'r')
    # read out the first headline from each database, and then ignore
    fValid.readline();
    fValidSol.readline();

    N, MAP = 0, 0; 
    feature = Feature()
    while 1:
        ValidLine = fValid.readline()
        ValidSolLine = fValidSol.readline()
        if not ValidLine: break
        
        N+=1
        v = ValidLine.replace(',', ' ').strip('\n').split(' ')[:-1]
        vs = ValidSolLine.replace(',', ' ').strip('\n').split(' ')[:-1]

        # cast types of attributes from strings to integers
        v = [int(v[i]) for i in range(len(v))]
        vs = [int(vs[i]) for i in range(1,len(vs))]

        # if denominator of AveP formula is 0, just set AveP to 0 and continue on
        if len(v)==1 or len(vs)==0:
            continue
      
        # construct feature matrix of size [n_samples X n_features
        # and then run it with random_forest to produces probabilities
        X = [feature.get_feature_vector(v[0],v[i]) for i in range(1, len(v))]
        Y = forest.predict_proba(X)

        # combine the output probabilities with original paperlist as tuples,
        # and then sort them from higher probabilities to lower
        tuples = [(v[i+1], Y[i]) for i in range(len(Y))]
        sorted(tuples, key=lambda x: x[1], reverse=True)

        k = 1
        Avep = 0.
        for i in range(len(tuples)):
            if tuples[i][0] in vs:
                Avep += float(k)/i
                k+=1
        Avep /= min(len(tuples), len(vs))
        MAP += Avep

    return MAP/N

if __name__ == "__main__":
    # initialize random_forest classifier with given parameters (parameter tuning needed)
    feature = Feature()
    forest = RandomForestClassifier(n_estimators=10)

    # X is a feature matrix of size [n_samples, n_features]
    # Y is a output matrix of size [n_samples, n_outputs]

    fileProcessor = FileProcessor()
    #fileProcessor.get_author_id_list()
    train_author_list = fileProcessor.get_train_author_id_list()
    Y = []
    for i in range(len(train_author_list)):
        author_id = train_author_list[i]
        confirmed_paper_id_list= fileProcessor.get_train_confirmedpaper_id_list(author_id)
        for paper_id in confirmed_paper_id_list:
            X = feature.get_feature_vector(author_id, paper_id)
            Y.append(1)
        deleted_paper_id_list = fileProcessor.get_train_deleteedpaper_id_list(author_id)
        for deleted_id in deleted_paper_id_list:
            X+=feature.get_feature_vector(author_id, deleted_paper_id_list)
            Y.append(-1)
    #print X
    #print Y
    # have the classifier learn from inputs and outputs, say X and Y
    forest.fit(X, Y)
    print 'train done'
    # after having finished learning, examine the accuracy of classifier using MAP metric
    map_score = computeMAP(forest)
    print 'map_score: '+str(map_score)
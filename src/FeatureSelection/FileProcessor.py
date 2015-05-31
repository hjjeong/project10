'''
Created on 2015. 5. 28.

@author: HJJeong
'''

import csv
from pip._vendor.distlib.util import CSVReader

class FileProcessor:
    '''
    classdocs
    '''
    paper_conference_journal_filepath = "../../data/Paper.csv"
    author_filepath = "../../data/Author.csv"
    train_filepath = "../../data/Train.csv"
    valid_filepath = "../../data/Valid.csv"
    author_paper_filepath = "../../data/PaperAuthor.csv"
    
    def __init__(self):
        '''init'''
        
    def get_author_id_list(self):
        author_file = open(self.author_filepath)
        csvReader = csv.reader(author_file) 
        author_id_list = []
        next(csvReader)
        for row in csvReader:
            author_id_list.append(row[0])
        #for line in author_file.read().splitlines():
        #    line_split = line.split(',')
        #    author_id_list.append(line_split[0])
        
        author_file.close()
        return author_id_list
    
    def get_train_author_id_list(self):
        train_file = open(self.train_filepath)
        csvReader = csv.reader(train_file)
        train_author_id_list = []
        next(csvReader)
        for row in csvReader:
            train_author_id_list.append(row[0])
        #for line in train_file.read().splitlines():
        #    line_split = line.split(',')
        #    train_author_id_list.append(line_split[0])
        train_file.close()
        return train_author_id_list
       
    def get_train_data_list(self):
        train_file = open(self.train_filepath)
        train_data_list = []
        csvReader = csv.reader(train_file)
        next(csvReader)
        for row in csvReader:
            train_data_list.append(row)
        #print 'train data:' +str(train_data_list)
        #for line in train_file.read().splitlines():
        #    line_split = line.split(',')
        #    train_data_list.append(line_split)
            
        train_file.close()
        return train_data_list
            
    def get_train_confirmedpaper_id_list(self, author_id):
        train_file = open(self.train_filepath)
        train_paper_list = []
        csvReader = csv.reader(train_file)
        next(csvReader)
        for row in csvReader:
            if author_id == row[0]:
                train_paper_list = row[1].split()
                
        #for line in train_file.read().splitlines():
        #    line_split = line.split(',')
        #    if author_id == line_split[0]: #compare author_id with author_id in train database
        #        train_paper_list = line_split[1].split()
        train_file.close()
        #print 'confirmed paper id: '+str(train_paper_list)
        return train_paper_list
    
    def get_train_deleteedpaper_id_list(self, author_id):
        train_file = open(self.train_filepath)
        train_paper_list = []
        csvReader = csv.reader(train_file)
        next(csvReader)
        for row in csvReader:
            if author_id == row[0]:
                train_paper_list = row[2].split()
        
        train_file.close() 
        #print 'deleted paper id: '+str(train_paper_list)
        return train_paper_list
           
    def get_valid_paper_id_list(self, author_id):
        valid_file = open(self.valid_filepath)
        valid_paper_list = []
        csvReader = csv.reader(valid_file)
        next(csvReader)
        for row in csvReader:
            if author_id == row[0]:
                valid_paper_list = row[1].split()
        
        #for line in valid_file.read().splitlines():
        #    line_split = line.split('#')
        #    if author_id == line_split[0]: #compare author_id with author_id in train database
        #        valid_paper_list = line_split[1].split()
        valid_file.close()    
        return valid_paper_list
    
    def get_name_from_author(self, author_id):
        author_file = open(self.author_filepath)
        author_name = []
        csvReader = csv.reader(author_file)
        next(csvReader)
        for row in csvReader:
            if author_id == row[0]:
                author_name = row[1]
                 
        #for line in author_file.read().splitlines():
        #    line_split = line.split('#')
        #    if author_id == line_split[0]:
        #        author_name = line_split[1]
        author_file.close()       
        return author_name        
    
    def get_name_from_authorpaper(self, author_id):
        author_paper_file = open(self.author_paper_filepath)
        author_paper_name=[]
        csvReader = csv.reader(author_paper_file)
        next(csvReader)
        for row in csvReader:
            if author_id == row[1]:
                author_paper_name = row[2]
        
        #for line in author_paper_file.read().splitlines():
        #    line_split = line.split('#')
        #    print 'line_split: '+str(line_split)
        #    if author_id == line_split[1]:
        #        author_paper_name = line_split[2]
        #        cnt = cnt+1
        author_paper_file.close()
        return author_paper_name
    
    def get_affiliation_from_author(self, author_id):
        author_file = open(self.author_filepath)
        author_affiliation = []
        csvReader = csv.reader(author_file)
        next(csvReader)
        for row in csvReader:
            if author_id == row[0]:
                author_affiliation = row[2]
                
        #for line in author_file.read().splitlines():
        #    line_split = line.split('#')
        #    if author_id == line_split[0]:
        #        author_affiliation = line_split[2]
        author_file.close()       
        return author_affiliation        
    
    def get_affiliation_from_authorpaper(self, author_id):
        author_paper_file = open(self.author_paper_filepath)
        author_paper_affiliation=[]
        #cnt = 0
        csvReader = csv.reader(author_paper_file)
        next(csvReader)
        for row in csvReader:
            if author_id == row[1]:
                author_paper_affiliation = row[3]
        
        
        #for line in author_paper_file.read().splitlines():
        #    line_split = line.split('#')
        #    if author_id == line_split[1]:
        #        author_paper_affiliation = line_split[3]
        #        cnt = cnt+1
        author_paper_file.close()
        return author_paper_affiliation        
            
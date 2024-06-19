from exceptions import (
    TypePopulationSample,
    ValuePopulationSample,
)
import random
import pandas as pd
from collections import Counter
import numpy as np


class Population:

    def __init__(self, collection:list|dict=None, columns:list=None, index:list=None) -> None:
        '''
        A set of pepole or things that we want to study one or more characteristics about them is called a population.
        ===
        input:
        1. collection -> (list or dict)
            collection form number, string and ... which are in to list or dict
        2. columns -> (list)
            name of columns ...
        3. index -> (list)
            index for row. ...
        '''
        self._collection = collection if collection else None
        self._columns = columns if columns else []
        self._index = index if index else []


    def sample(self, n: int) -> list|dict|set:
        '''
        A part of the population that is selected according to criteria and can be studied instead of sudying  the entire population is called a sample of the population
        ===
        input:
        1. n -> (int)
            number samples
        '''
        lenght = len(self._collection)
        type_ = type(self._collection)
        if n > lenght:
            raise ValuePopulationSample(f'The number of samples requested is greater than the lenght of your total.your lenght collection = {lenght} and your samples requested = {n}')
        elif type_ == list:
            random_sample = random.sample(self._collection, n)
            return random_sample
        elif type_ == dict:
            random_sample = dict(random.sample(sorted(self._collection.items()), n))
            return random_sample
        elif type_ == set:
            random_sample = set(random.sample(sorted(self._collection), n))
            return random_sample
        raise TypePopulationSample(f'Please check your collection type!!! your collection type must be list, dictionary or set.your type collection = {type_}')


    def __repr__(self):
        str_ = ""
        if self._collection is None or self._columns is None or self._index is None:
            str_ += f"Empty Population\n"
            str_ += f"Columns: {self._columns}\n"
            str_ += f"Index : {self._index}\n"
            return str_
        return f'{self._collection}'


class Statics:

    def __init__(self, collection:list) -> None:
        self.collection = collection

    def frequency_table(self, n_category:int=None):
        
        tf = pd.DataFrame()

        if n_category == None:
            tf["xi"] = [x for x in set(self.collection)] 
            tf["fi"] = [x for x in Counter(self.collection).values()] 
            tf["vi"] = [round(x/len(self.collection), 2) for x in tf["fi"]]
            tf["gi"] = np.cumsum(tf["fi"])
            tf["si"] = [round(x/len(self.collection), 2) for x in tf["gi"]]
            return tf
        

        else:
            category_list = []
            xi = []
            fi = []
    
            d = 1
            a = min(self.collection)-d/2
            b = max(self.collection)-d/2
            k = n_category
            r = b - a
            l = r/k
    
            for i in range(n_category):
                category_list.append(f"{a}-{round(a+l,1)}")
                xi.append(a+round(a+l,1)/len(self.collection))
                fi.append(len([x for x in filter(lambda x:x>a and x<a+l,self.collection)]))
                a=round(a+l,1)
    
    
    
            tf["category"] = category_list
            tf["xi"] = xi
            tf["fi"] = fi
            tf["vi"] = [round(x/len(self.collection), 2) for x in tf["fi"]]
            tf["gi"] = np.cumsum(tf["fi"])
            tf["si"] = [x/len(self.collection) for x in tf["gi"]]
        
            return tf
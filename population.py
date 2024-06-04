from exception import (
    TypePopulationSample,
    ValuePopulationSample,
)
import random



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

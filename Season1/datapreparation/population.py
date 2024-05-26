import random

class BaseException(ValueError):
         pass

class NValue(BaseException):
         pass

class TypeValue(BaseException):
         pass


class Population:
    def __init__(self, collection: list|dict|set):
        '''
        A set of pepole or things that we want to study one or more characteristics about them is called a population.
        ===
        input:
        1. collection -> (list or dict or set)
            collection form number, string and ... which are in to list or dict or set
        '''
        if type(collection) == int or type(collection) == str:
            raise TypeValue(f"you cant create pupulation from {type(collection)} object. you shold give list,dict,set or a collection for input to population class")
        self._collection = collection


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
            raise NValue(f'The number of samples requested is greater than the lenght of your total.your lenght collection = {lenght} and your samples requested = {n}')
        elif type_ == list:
            random_sample = random.sample(self._collection, n)
            return random_sample
        elif type_ == dict:
            random_sample = dict(random.sample(sorted(self._collection.items()), n))
            return random_sample
        elif type_ == set:
            random_sample = set(random.sample(sorted(self._collection), n))
            return random_sample
        raise TypeValue(f'Please check your collection type!!! your collection type must be list, dictionary or set.your type collection = {type_}')


    def __repr__(self):
        _str = ""
        _str += f'{self._collection}'
        return _str

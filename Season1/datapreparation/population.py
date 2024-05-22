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
            raise Exception(f"you cant create pupulation from {type(collection)} object. you shold give list,dict,set or a collection for input to population class")
    self._collection = collection


    def sample(self):
    '''
    A part of the population that is selected according to
    criteria and can be studied instead of sudying  the entire
    population is called a sample of the population
    '''
        pass


    def __repr__(self):
        _str = ""
        _str += f'{self._collection}'
        return _str

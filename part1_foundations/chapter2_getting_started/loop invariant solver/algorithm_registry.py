from typing import Dict, Type, Callable
from algorithm import Algorithm, AlgorithmState

class AlgorithmRegistry:
    _algorithms: Dict[str, Type[Algorithm]] = {}                    # algorithm name -> algorithm class
    _invariants: Dict[str, Callable[[AlgorithmState], bool]] = {}   # algorithm name -> invariant
    
    @classmethod                                                    # decorator
    def register(cls, invariant: Callable[[AlgorithmState], bool]): # invariant is a function that takes an AlgorithmState and returns a bool
        def wrapper(algorithm_class: Type[Algorithm]):              # algorithm_class is a class that inherits from Algorithm
            name = algorithm_class.__name__                         # get the name of the algorithm class
            cls._algorithms[name] = algorithm_class                 # register the algorithm class
            cls._invariants[name] = invariant                       # register the invariant
            return algorithm_class                                  # return the algorithm class
        return wrapper                                              # return the wrapper function
    
    @classmethod                                                    # decorator
    def get_algorithm(cls, name: str) -> Type[Algorithm]:           # name is a string that represents the name of the algorithm   
        return cls._algorithms[name]                                # return the algorithm class
    
    @classmethod                                                    # decorator
    def get_invariant(cls, name: str) -> Callable[                  # name is a string that represents the name of the algorithm
        [AlgorithmState], bool]:                                    # return a function that takes an AlgorithmState and returns a bool
        return cls._invariants[name]                                # return the invariant
    
    @classmethod                                                    # decorator
    def list_algorithms(cls) -> list[str]:                          # return a list of strings
        return list(cls._algorithms.keys())                         # return the keys of the _algorithms dictionary

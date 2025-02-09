from typing import Dict, Type, Callable
from algorithm import Algorithm, AlgorithmState

class AlgorithmRegistry:
    _algorithms: Dict[str, Type[Algorithm]] = {}
    _invariants: Dict[str, Callable[[AlgorithmState], bool]] = {}
    
    @classmethod
    def register(cls, invariant: Callable[[AlgorithmState], bool]):
        """Decorator to register an algorithm and its invariant"""
        def wrapper(algorithm_class: Type[Algorithm]):
            name = algorithm_class.__name__
            cls._algorithms[name] = algorithm_class
            cls._invariants[name] = invariant
            return algorithm_class
        return wrapper
    
    @classmethod
    def get_algorithm(cls, name: str) -> Type[Algorithm]:
        return cls._algorithms[name]
    
    @classmethod
    def get_invariant(cls, name: str) -> Callable[[AlgorithmState], bool]:
        return cls._invariants[name]
    
    @classmethod
    def list_algorithms(cls) -> list[str]:
        return list(cls._algorithms.keys())

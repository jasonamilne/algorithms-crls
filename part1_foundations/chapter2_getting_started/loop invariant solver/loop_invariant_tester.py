from typing import Any, Callable, List, Optional
from dataclasses import dataclass
from algorithm import Algorithm, AlgorithmState

@dataclass
class LoopState:
    """Represents the state of a loop at any given iteration"""
    iteration: int
    searched_elements: List[Any]
    current_element: Any
    remaining_elements: List[Any]
    found_value: bool = False

class LoopInvariantTester:
    def __init__(self, algorithm: Algorithm, invariant_check: Callable[[AlgorithmState], bool]):
        self.algorithm = algorithm
        self.invariant_check = invariant_check
        self.current_state = None
        
    def check_initialization(self) -> bool:
        """Check if loop invariant holds before first iteration"""
        self.current_state = self.algorithm.initialize()
        return self.invariant_check(self.current_state)
        
    def check_maintenance(self, iteration: int) -> bool:
        """Check if loop invariant holds after each iteration"""
        self.current_state = self.algorithm.step(iteration)
        return self.invariant_check(self.current_state)
        
    def check_termination(self) -> bool:
        """Check if loop invariant holds after loop completion"""
        return self.invariant_check(self.current_state)

    def is_complete(self) -> bool:
        """Check if algorithm has completed"""
        return self.algorithm.is_complete(self.current_state)

def linear_search_invariant(state: LoopState) -> bool:
    """Specific invariant check for linear search"""
    return state.value not in state.searched_elements

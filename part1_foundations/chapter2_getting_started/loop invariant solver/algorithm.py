from abc import ABC, abstractmethod
from typing import Any, List
from dataclasses import dataclass

@dataclass
class AlgorithmState:
    """Generic state representation for any algorithm"""
    iteration: int                                                  # Add iteration to state
    processed_elements: List[Any]                                   # Add processed_elements to state
    current_element: Any                                            # Add current_element to state
    remaining_elements: List[Any]                                   # Add remaining_elements to state
    target: Any                                                     # Add target to state
    result: Any = None                                              # Add result to state

class Algorithm(ABC):
    """Abstract base class for algorithms that can be tested"""
    
    @abstractmethod
    def initialize(self) -> AlgorithmState:
        """Initialize algorithm state"""
        pass
    
    @abstractmethod
    def step(self, iteration: int) -> AlgorithmState:
        """Perform one step of the algorithm"""
        pass
    
    @abstractmethod
    def is_complete(self, state: AlgorithmState) -> bool:
        """Check if algorithm has completed"""
        pass

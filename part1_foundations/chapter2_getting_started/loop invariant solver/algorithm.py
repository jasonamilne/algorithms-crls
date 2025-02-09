from abc import ABC, abstractmethod
from typing import Any, List
from dataclasses import dataclass

@dataclass
class AlgorithmState:
    """Generic state representation for any algorithm"""
    iteration: int
    processed_elements: List[Any]
    current_element: Any
    remaining_elements: List[Any]
    target: Any  # Add target to state
    result: Any = None

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

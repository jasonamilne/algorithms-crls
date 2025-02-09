from algorithm import Algorithm, AlgorithmState
from algorithm_registry import AlgorithmRegistry
from typing import List, Any

@AlgorithmRegistry.register(
    invariant=lambda state: (
        # Target found: must be in processed elements
        (state.result is not None and 
         state.processed_elements[state.result] == state.target) or
        # Target not found: must not be in processed elements
        (state.result is None and 
         state.target not in state.processed_elements)
    )
)
class LinearSearch(Algorithm):
    """Linear search algorithm that finds a target value in an array.
    
    Loop Invariant:
    - If target is found, it must be in processed elements at the correct index
    - If target is not found, it must not be in any of the processed elements
    """
    
    def __init__(self, array: List[Any], target: Any) -> None:
        """Initialize linear search with array and target value."""
        self.array = array
        self.target = target
        self.current_pos = 0
        self.processed = []  # Use list instead of set to maintain order
        
    def initialize(self) -> AlgorithmState:
        """Initialize linear search with empty processed list."""
        self.processed = []
        self.current_pos = 0
        
        return AlgorithmState(
            iteration=0,
            processed_elements=[],
            current_element=self.array[0] if self.array else None,  # Show first element
            remaining_elements=self.array[1:],  # Rest of elements
            target=self.target,
            result=None
        )
        
    def step(self, iteration: int) -> AlgorithmState:
        """Perform one step of linear search."""
        if self.current_pos >= len(self.array):
            return AlgorithmState(
                iteration=iteration,
                processed_elements=self.processed.copy(),
                current_element=None,
                remaining_elements=[],
                target=self.target,
                result=None
            )
            
        current = self.array[self.current_pos]
        result = None
        
        # Add current element to processed list
        self.processed.append(current)
        
        if current == self.target:
            result = self.current_pos
            self.current_pos = len(self.array)  # Force termination
        else:
            self.current_pos += 1
            
        return AlgorithmState(
            iteration=iteration,
            processed_elements=self.processed.copy(),
            current_element=current,
            remaining_elements=self.array[self.current_pos:],
            target=self.target,
            result=result
        )

    def is_complete(self, state: AlgorithmState) -> bool:
        """Check if linear search is complete."""
        return state.result is not None or self.current_pos >= len(self.array)

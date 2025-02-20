from algorithm import Algorithm, AlgorithmState
from algorithm_registry import AlgorithmRegistry
from typing import List, Any, Optional

@AlgorithmRegistry.register(
    invariant=lambda state: (
        # Target found: must be in processed elements at correct position
        (state.result is not None and state.processed_elements[state.result] == state.target) or
        # Target not found: must maintain binary search property
        (state.result is None and 
         state.target not in state.processed_elements and  # haven't missed the target
         (len(state.remaining_elements) > 0 or            # either still searching
          all(x < state.target or x > state.target       # or have ruled out all elements
              for x in state.processed_elements)))
    )
)
class BinarySearch(Algorithm):
    """Binary search algorithm that finds a target value in a sorted array.
    
    Loop Invariant:
    - If target is found, it must be in processed elements at the correct index
    - If target is not found:
      1. All processed elements must be either less than or greater than target
      2. Target must be in remaining elements if it exists in array
      3. When remaining elements is empty, we must have processed some elements
    """
    
    def __init__(self, array: List[Any], target: Any) -> None:
        """Initialize binary search with sorted array and target value."""
        self.array = sorted(array)                                  # Sort the array
        self.target = target                                        # Set the target
        self.left = 0                                               # Set the left index to 0
        self.right = len(array) - 1                                 # Set the right index to the length of the array minus 1
        self.processed = set()                                      # Initialize the processed set

    def initialize(self) -> AlgorithmState:
        """Initialize binary search with empty processed set."""
        self.processed = set()                                      # Initialize the processed set
        mid = (self.left + self.right) // 2                         # Calculate the mid index
        
        return AlgorithmState(
            iteration=0,                                            # Set the iteration to 0
            processed_elements=[],                                  # Set the processed elements to an empty list
            current_element=self.array[mid],                        # Set the current element to the mid element
            remaining_elements=self.array[:mid]+self.array[mid+1:], # Set the remaining elements to the array excluding the mid element
            target=self.target,                                     # Set the target
            result=None                                             # Set the result to None
        )
        
    def step(self, iteration: int) -> AlgorithmState:
        """Perform one step of binary search."""
        if self.left > self.right:
            return AlgorithmState(
                iteration=iteration,
                processed_elements=sorted(list(self.processed)),
                current_element=None,
                remaining_elements=[],
                target=self.target,
                result=None
            )
            
        mid = (self.left + self.right) // 2
        current = self.array[mid]
        result = None
        
        # Add current element and appropriate range to processed set
        self.processed.add(current)
        
        if current == self.target:
            result = mid
            self.left = self.right + 1  # Force termination
        elif current < self.target:
            self.processed.update(self.array[self.left:mid])
            self.left = mid + 1
        else:
            self.processed.update(self.array[mid+1:self.right + 1])
            self.right = mid - 1
            
        next_mid = None if self.left > self.right else (self.left + self.right) // 2
        
        return AlgorithmState(
            iteration=iteration,
            processed_elements=sorted(list(self.processed)),
            current_element=self.array[next_mid] if next_mid is not None else None,
            remaining_elements=self.array[self.left:self.right + 1],
            target=self.target,
            result=result
        )

    def is_complete(self, state: AlgorithmState) -> bool:
        """Check if binary search is complete."""
        return state.result is not None or self.left > self.right

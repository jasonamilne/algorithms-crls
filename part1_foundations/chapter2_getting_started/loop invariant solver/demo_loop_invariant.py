from loop_invariant_tester import LoopInvariantTester
from algorithm_registry import AlgorithmRegistry
# Import algorithms to register them
import linear_search
import binary_search

def demonstrate_algorithm(array: list, target: int, algorithm_name: str):
    """Run tests and display results for a given algorithm"""
    print(f"\nTesting {algorithm_name}: Find {target} in {array}")      # Print the algorithm name and test case
    print("-" * 50)                                                     # Print a line of dashes
    
    algorithm_class = AlgorithmRegistry.get_algorithm(algorithm_name)   # Get the algorithm class
    invariant = AlgorithmRegistry.get_invariant(algorithm_name)         # Get the invariant for the algorithm
    
    algorithm = algorithm_class(array, target)                          # Initialize the algorithm
    tester = LoopInvariantTester(algorithm, invariant)                  # Initialize the tester
    
    # Check initialization
    init_result = tester.check_initialization()                         # Check the initialization    
    print(f"Initialization: {'✓' if init_result else '✗'}")            # Print if the initialization holds
    
    # Check maintenance
    iteration = 0                                                       # Initialize the iteration
    while not tester.is_complete():                                     # While the algorithm is not complete
        maint_result = tester.check_maintenance(iteration)              # Check the maintenance
        state = tester.current_state                                    # Get the current state
        print(f"\nIteration {iteration}:")                              # Print the iteration
        print(f"  Previously processed: {state.processed_elements}")    # Print the previously processed elements
        print(f"  Current element: {state.current_element}")            # Print the current element
        print(f"  Remaining elements: {state.remaining_elements}")      # Print the remaining elements
        print(f"  Invariant holds: {'✓' if maint_result else '✗'}")    # Print if the invariant holds
        iteration += 1                                                  # Increment the iteration
    
    # Check termination
    term_result = tester.check_termination()                            # Check the termination
    print(f"\nTermination: {'✓' if term_result else '✗'}")             # Print if the termination holds
    state = tester.current_state                                        # Get the current state
    if state.result is not None:                                        # If the result is not None
        print(f"  Found {target} at index {state.result}")              # Print the result
    else:                                                               # Otherwise
        print(f"  {target} not found in array")                         # Print that the target was not found

if __name__ == "__main__":                                              # If the script is run directly
    test_cases = [                                                      
        ([1, 3, 70, 4], 70),                                            # Middle
        ([1, 3, 70, 4], 1),                                             # First
        ([1, 3, 70, 4], 5),                                             # Not found
    ]
    
    # Run tests for all registered algorithms
    for algorithm_name in AlgorithmRegistry.list_algorithms():          # For each algorithm
        print(f"\n{algorithm_name.upper()} TESTS")                      # Print the algorithm name
        print("=" * (len(algorithm_name) + 6))                          # Print a line of equal signs
        for array, target in test_cases:                                # For each test case
            demonstrate_algorithm(array, target, algorithm_name)        # Run the test case

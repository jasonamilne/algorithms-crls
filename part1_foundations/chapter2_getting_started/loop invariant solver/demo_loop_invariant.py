from loop_invariant_tester import LoopInvariantTester
from algorithm_registry import AlgorithmRegistry
# Import algorithms to register them
import linear_search
import binary_search

def demonstrate_algorithm(array: list, target: int, algorithm_name: str):
    """Run tests and display results for a given algorithm"""
    print(f"\nTesting {algorithm_name}: Find {target} in {array}")
    print("-" * 50)
    
    algorithm_class = AlgorithmRegistry.get_algorithm(algorithm_name)
    invariant = AlgorithmRegistry.get_invariant(algorithm_name)
    
    algorithm = algorithm_class(array, target)
    tester = LoopInvariantTester(algorithm, invariant)
    
    # Check initialization
    init_result = tester.check_initialization()
    print(f"Initialization: {'✓' if init_result else '✗'}")
    
    # Check maintenance
    iteration = 0
    while not tester.is_complete():
        maint_result = tester.check_maintenance(iteration)
        state = tester.current_state
        print(f"\nIteration {iteration}:")
        print(f"  Previously processed: {state.processed_elements}")
        print(f"  Current element: {state.current_element}")
        print(f"  Remaining elements: {state.remaining_elements}")
        print(f"  Invariant holds: {'✓' if maint_result else '✗'}")
        iteration += 1
    
    # Check termination
    term_result = tester.check_termination()
    print(f"\nTermination: {'✓' if term_result else '✗'}")
    state = tester.current_state
    if state.result is not None:
        print(f"  Found {target} at index {state.result}")
    else:
        print(f"  {target} not found in array")

if __name__ == "__main__":
    test_cases = [
        ([1, 3, 70, 4], 70),  # middle
        ([1, 3, 70, 4], 1),   # first
        ([1, 3, 70, 4], 5),   # not found
    ]
    
    # Run tests for all registered algorithms
    for algorithm_name in AlgorithmRegistry.list_algorithms():
        print(f"\n{algorithm_name.upper()} TESTS")
        print("=" * (len(algorithm_name) + 6))
        for array, target in test_cases:
            demonstrate_algorithm(array, target, algorithm_name)

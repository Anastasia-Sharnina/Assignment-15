def rod_cutting(prices, n):
    # Base case: if the length of the rod is 0, no profit can be made
    if n == 0:
        return 0, []

    max_value = float('-inf')
    best_cut = 0

    # Iterate through all possible first cuts
    for i in range(1, n + 1):
        if i <= len(prices):  # Ensure we don't go out of bounds for prices
            current_value, _ = rod_cutting(prices, n - i)
            current_value += prices[i - 1]  # Include the price of the current cut

            # Update max_value and best_cut if a better option is found
            if current_value > max_value:
                max_value = current_value
                best_cut = i

    return max_value, best_cut


def reconstruct_cuts(prices, n):
    cuts = []
    while n > 0:
        max_profit, best_cut = rod_cutting(prices, n)
        cuts.append(best_cut)
        n -= best_cut
    return cuts


# Main function to handle user input and output results
if __name__ == "__main__":
    # User input for rod length and prices
    rod_length = int(input("Enter the length of the rod (in inches): "))
    prices_input = input("Enter the array of prices (comma-separated): ")
    
    # Convert input string to a list of integers
    prices = list(map(int, prices_input.split(',')))

    # Calculate maximum profit
    max_profit, _ = rod_cutting(prices, rod_length)

    # Reconstruct recommended cuts
    recommended_lengths = reconstruct_cuts(prices, rod_length)

    # Output results
    print(f"The maximum obtainable value is: {max_profit}")
    print(f"Recommended lengths to cut: {recommended_lengths}")
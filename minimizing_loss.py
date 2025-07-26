def find_min_loss(prices):
    """
    Finds the minimum loss when buying and selling a house.
    
    Args:
        prices: List of prices for consecutive years
        
    Returns:
        tuple: (buy_year, sell_year, min_loss)
    """
    min_loss = float('inf')
    buy_year = sell_year = -1
    
    # Create a list of (price, year) tuples
    price_years = [(price, year + 1) for year, price in enumerate(prices)]
    
    # Sort prices in descending order
    price_years.sort(reverse=True, key=lambda x: x[0])
    
    # Find the minimum loss where buy year > sell year
    for i in range(len(price_years)):
        for j in range(i + 1, len(price_years)):
            # Check if buy year is after sell year
            if price_years[i][1] > price_years[j][1]:
                loss = price_years[i][0] - price_years[j][0]
                if 0 <= loss < min_loss:
                    min_loss = loss
                    buy_year = price_years[i][1]
                    sell_year = price_years[j][1]
    
    return (buy_year, sell_year, min_loss)

def find_min_loss_optimized(prices):
    """
    More optimized version of find_min_loss using a single pass.
    """
    min_loss = float('inf')
    buy_year = sell_year = -1
    
    # Track the maximum price seen so far
    max_prices = {}
    
    for year, price in enumerate(prices, 1):
        for prev_year, prev_price in list(max_prices.items()):
            if prev_price > price:  # Potential loss
                loss = prev_price - price
                if 0 <= loss < min_loss:
                    min_loss = loss
                    buy_year = prev_year
                    sell_year = year
        
        # Update the maximum price for this year
        max_prices[year] = price
    
    return (buy_year, sell_year, min_loss if min_loss != float('inf') else 0)

# Example usage
if __name__ == "__main__":
    # Test case 1
    prices1 = [20, 15, 7, 2, 13]
    buy1, sell1, loss1 = find_min_loss(prices1)
    print(f"Prices: {prices1}")
    print(f"Buy in year {buy1}, sell in year {sell1} with a loss of {loss1}")
    
    # Test case 2: No possible loss
    prices2 = [1, 2, 3, 4, 5]
    buy2, sell2, loss2 = find_min_loss(prices2)
    print(f"\nPrices: {prices2}")
    if loss2 == float('inf'):
        print("No possible loss")
    else:
        print(f"Buy in year {buy2}, sell in year {sell2} with a loss of {loss2}")
    
    # Test case 3: Multiple possible losses
    prices3 = [30, 10, 20, 5, 15, 25]
    buy3, sell3, loss3 = find_min_loss_optimized(prices3)
    print(f"\nPrices: {prices3} (using optimized function)")
    print(f"Buy in year {buy3}, sell in year {sell3} with a loss of {loss3}")

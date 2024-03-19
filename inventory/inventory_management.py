def sort_products(products: list, sort_key: str, ascending: bool) -> list:
    """
    Function return list of dictionaries sorted accordinly to sort_key provided as parameter 
    and ascending or descending order in this sort_key
    :param products: List of dictionaries
    :param sort_key: Key name in dictionary by which sorting is performed
    :param ascending: Bool value for ascending or descending sorting order, e.g if False 
    then sorting order is ascending
    :return: Sorted list of dictionaries
    """
    sorted_products = sorted(products, key=lambda x: x[sort_key], reverse= not ascending)
    return sorted_products

if __name__ == "__main__":
    #Given data structure
    products = [
        {"name": "Product A", "price": 100, "stock": 5},
        {"name": "Product B", "price": 200, "stock": 3},
        {"name": "Product C", "price": 50, "stock": 10}
    ]
    sort_key = "price"
    ascending = False

    # Calling function to sort products
    sorted_products = sort_products(products, sort_key, ascending)

    # Printing sorted products
    for product in sorted_products:
        print(product)

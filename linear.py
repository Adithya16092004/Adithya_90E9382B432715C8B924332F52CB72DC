def linear_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices


products = ["apple", "banana", "apple", "orange", "apple"]
target = "apple"
result = linear_product(products, target)
print(result)  

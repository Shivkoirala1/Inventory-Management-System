def read_product_file(file_path):
    """Reads the product file and returns a list of product dictionaries."""
    products = []  
    try:
        with open(file_path, "r") as file:  
            for line in file:
                data = line.strip().split(", ")  
                if len(data) == 5:  
                    product = {
                        "name": data[0],
                        "brand": data[1],
                        "quantity": int(data[2]),
                        "cost_price": float(data[3]),
                        "origin": data[4]
                    }
                    products.append(product)  
        return products
    except FileNotFoundError:
        print("Error: Product file not found!")
        return []
    except Exception as e:
        print("Error:", e)
        return []



# Test reading function 
# This function reads the content of the text file
if __name__ == "__main__":
    products = read_product_file("products.txt")
    print("Available Products:\n*********************************************")
    for product in products:
        print(f"{product['name']} ({product['brand']}) \nStock: {product['quantity']},\nCost Price: Rs.{product['cost_price']} ,\nOrigin: {product['origin']}")
        print("*********************************************")
def apply_pricing_policy(products):
    """Applies a 200% markup on cost price to set selling prices."""
    for product in products:
        product["selling_price"] = product["cost_price"] * 2  
    return products

def process_sale(products, product_name, quantity_requested):
    """Processes the sale, applies the 'Buy 3, Get 1 Free' policy, updates stock."""
    for product in products:
        if product["name"].lower() == product_name.lower():
            if quantity_requested > product["quantity"]:
                print("Error: Not enough stock available!")
                return None
            
            free_items = quantity_requested // 3  
            total_items_given = quantity_requested + free_items
            total_cost = quantity_requested * product["selling_price"]  

            product["quantity"] -= total_items_given  

            return {
                "name": product["name"],
                "brand": product["brand"],
                "quantity_requested": quantity_requested,
                "free_items": free_items,
                "total_cost": total_cost
            }
    
    print("Error: Product not found!")
    return None
def restock_product(products, product_name, quantity_added, new_cost_price=None):
    """Restocks a product, updates stock count and (optional) cost price."""
    for product in products:
        if product["name"].lower() == product_name.lower():
            product["quantity"] += quantity_added  # Increase stock
            if new_cost_price is not None:  # Update cost price if provided
                product["cost_price"] = new_cost_price
                product["selling_price"] = new_cost_price * 2  # Apply markup
            return product
    
    print("Error: Product not found!")
    return None
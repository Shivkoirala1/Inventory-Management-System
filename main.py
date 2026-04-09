from read import read_product_file
from operation import apply_pricing_policy, process_sale, restock_product
from write import generate_invoice, generate_restock_invoice

# Load product data
product_list = read_product_file("products.txt")
product_list = apply_pricing_policy(product_list)



def main():
    """Main function to handle transactions."""
    while True:
        print("\nWelcome to WeCare Store!")
        print("1. Show Products")
        print("2. Buy a Product")
        print("3. Restock Products")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Available Products:\n*********************************************")
            for product in product_list:
                print(f"{product['name']} ({product['brand']}) \nStock: {product['quantity']},\nCost Price: Rs.{product['cost_price']} ,\nOrigin: {product['origin']}")
                print("*********************************************")
        elif choice == "2":
            customer_name = input("Enter customer name: ")
            product_name = input("Enter product name to buy: ")
            quantity_requested = int(input("Enter quantity to buy: "))

            transaction_details = process_sale(product_list, product_name, quantity_requested)

            if transaction_details:
                generate_invoice(customer_name, transaction_details)

        elif choice == "3":
            vendor_name = input("Enter supplier/vendor name: ")
            product_name = input("Enter product name to restock: ")
            quantity_added = int(input("Enter quantity to add: "))
            new_cost_price = input("Enter new cost price (or press Enter to keep current price): ")
            new_cost_price = float(new_cost_price) if new_cost_price else None

            restocked_product = restock_product(product_list, product_name, quantity_added, new_cost_price)

            if restocked_product:
                generate_restock_invoice(vendor_name, [restocked_product])

        elif choice == "4":
            print("Exiting program. Have a great day!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

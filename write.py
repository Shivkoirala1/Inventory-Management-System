import datetime

def generate_invoice(customer_name, transaction_details):
    """Generates an invoice for the transaction."""
    invoice_filename = f"invoice_{customer_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(invoice_filename, "w") as invoice:
        invoice.write(f"Customer: {customer_name}\n")
        invoice.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        invoice.write(f"Product: {transaction_details['name']} ({transaction_details['brand']})\n")
        invoice.write(f"Quantity Purchased: {transaction_details['quantity_requested']}\n")
        invoice.write(f"Free Items Given: {transaction_details['free_items']}\n")
        invoice.write(f"Total Amount: {transaction_details['total_cost']} Rs\n")
    
    print(f"Transaction successful! Invoice saved as {invoice_filename}")

def generate_restock_invoice(vendor_name, restocked_products):
    """Generates an invoice for restocking products from a supplier."""
    invoice_filename = f"restock_invoice_{vendor_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(invoice_filename, "w") as invoice:
        invoice.write(f"Vendor: {vendor_name}\n")
        invoice.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        total_amount = 0
        for product in restocked_products:
            invoice.write(f"Product: {product['name']} ({product['brand']})\n")
            invoice.write(f"Quantity Restocked: {product['quantity']}\n")
            invoice.write(f"Cost Price per Unit: {product['cost_price']} Rs\n")
            invoice.write(f"Subtotal: {product['quantity'] * product['cost_price']} Rs\n\n")
            total_amount += product["quantity"] * product["cost_price"]
        
        invoice.write(f"Total Amount: {total_amount} Rs\n")

    print(f"Thank you for restocking the product from us! Products successfully restocked {invoice_filename}")
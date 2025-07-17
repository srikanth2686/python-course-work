pharmacy_name = str(input("Enter Pharmacy Name: "))
location = str(input("Enter Location: "))
contact_number = int(input("Enter Contact Number: "))
product_name = str(input("Enter Product/Service Name: "))
price = float(input("Enter Price (or type 'Varies'): "))
categories = input("Enter Categories : ").split()    # list
stock_details = tuple(input("Enter the stock available :").split(","))  #tuple
discount_percentage = float(input("Enter Discount : "))   #float
features_input = input("Enter Features (comma-separated): ")
product_features = set(input("Enter the product features:").split(","))  #set
supplier_name = input("Enter Supplier Name: ").strip()
supplier_phone = input("Enter Supplier Contact Number: ").strip()
supplier_location = input("Enter Supplier Location: ").strip()
supplier_details = {
    "name": supplier_name,       #dict
    "phone": supplier_phone,
    "location": supplier_location
}
pharmacy_details = {
    "pharmacy_name": pharmacy_name,
    "location": location,
    "contact_number": contact_number,
    "product_name": product_name,
    "price": price,
    "categories": categories,
    "stock_details": stock_details,
    "discount": discount_percentage,
    "product_features": product_features,
    "supplier_details": supplier_details
}

# Output Section
print("Apollo Pharmacy Product Details:")
print("Pharmacy Name:", pharmacy_name)
print("Location:", location)
print("Contact Number:", contact_number)
print("Product/Service Name:", product_name)
print("Price:", price)
print("Categories:", categories)
print("Stock Details (Available, Sold):", stock_details)
print("Discount :", discount_percentage)
print("Features:", product_features)
print("Supplier Details:", supplier_details)
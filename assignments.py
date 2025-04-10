# Assignment 1

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent/100)
        final_price = price - discount_amount
        return final_price 
    else: 
        return price 
    

    # Assignment 2

    def calculate_discount(price, discount_percent):
        if discount_percent >= 20:
            return price - (price * discount_percent /100)
        return price
    try: 
        price = float(input("Enter the price: "))
        discount_percent = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(price, discount_percent)

        if discount_percent >= 20:
           print(f"The final price after discount is: {final_price:.2f}")
        else:
           print(f"The final price is: {final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")
    

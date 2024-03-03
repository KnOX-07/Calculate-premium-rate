# Accepting input for health status, age, location, and gender
health = input("Enter health status(excellent/poor): ").lower()
age = int(input("Enter age: "))
location = input("Enter location(city/village): ").lower()
gender = input("Enter gender(male/female): ").lower()

# Determining insurance eligibility, premium rate, and maximum insured amount
if health == "excellent" and 25 <= age <= 35 and location == "city" and gender == "male":
    premium_rate = 4  # Rs. 4 per thousand
    max_insured_amount = min(200000, premium_rate * 1000)  # Policy amount cannot exceed Rs. 2 lakhs
    print(f"The person is eligible for insurance.\nPremium rate: Rs. {premium_rate}/thousand\nMaximum insured amount: Rs. {max_insured_amount}")
  
elif health == "excellent" and 25 <= age <= 35 and location == "city" and gender == "female":
    premium_rate = 3  # Rs. 3 per thousand
    max_insured_amount = min(100000, premium_rate * 1000)  # Policy amount cannot exceed Rs. 1 lakh
    print(f"The person is eligible for insurance.\nPremium rate: Rs. {premium_rate}/thousand\nMaximum insured amount: Rs. {max_insured_amount}")
  
elif health == "poor" and 25 <= age <= 35 and location == "village" and gender == "male":
    premium_rate = 6  # Rs. 6 per thousand
    max_insured_amount = min(10000, premium_rate * 1000)  # Policy amount cannot exceed Rs. 10,000
    print(f"The person is eligible for insurance.\nPremium rate: Rs. {premium_rate}/thousand\nMaximum insured amount: Rs. {max_insured_amount}")
else:
    print("The person is not eligible for insurance.")

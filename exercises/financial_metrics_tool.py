# Defines the tool
def calculate_operating_margin (revenue, operating_income):
  #Checks for invalid input
  if revenue <= 0:
    return {"error": "Revenue must be greater than zero."}
# Performs the calculation
  margin = operating_income / revenue

  return {
    "revenue": revenue,
    "operating_income": operating_income,
    "operating_margin_percent": round(margin * 100, 2)
  }
# Returns the structured results
company_data = calculate_operating_margin(100000, 15000)

print(company_data)

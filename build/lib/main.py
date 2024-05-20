def taxRate(grossAmt):
    if grossAmt < 300000:
        return 0
    elif grossAmt < 600000:
        return int((grossAmt/100) * 5)
    elif 600000 < grossAmt < 20000000:
        return int((grossAmt - 600000)/10) + 15000
    else:
        return int(((grossAmt - 20000000)/100)*25) + 155000

def calculateTaxed(yearlyTax):
    taxes["monthly_tax"] = int(yearlyTax / 12)
    taxes["per_day"] = int(taxes["monthly_tax"] / 30)
    taxes["11_month_tax"] = int(taxes["monthly_tax"] * 11)

def calculateJune():
    nextRent = int((stats["monthly_rent"]/10) + stats["monthly_rent"]) ; extras["next_rent"] = nextRent
    nextRentTax = taxRate(nextRent*12) ; extras["next_rent_tax"] = nextRentTax ; newRentPerDay = nextRentTax/(12*30) ; extras["next_rent_tax_per_day"] = newRentPerDay
    
    taxes["june_only"] = int(round((taxes["per_day"] * 12) + (newRentPerDay * 18), 0))

def calculateActualTax():
    taxes["actual_yearly_tax"] = int(round(taxes["11_month_tax"] + taxes["june_only"], 0))

def calculateStats():
    stats["monthly_rent_taxed"] = stats["monthly_rent"] - taxes["monthly_tax"]
    stats["taxed_rent_per_day"] = int(stats["monthly_rent_taxed"] / 30)
    stats["yearly_rent_taxed"] = int(round(stats["yearly_rent"] - taxes["actual_yearly_tax"], 0))

def display():
    print()
    print("===================================")
    print("STATISTICS")
    print("===================================")
    print("Monthly Rent\t\t", stats["monthly_rent"])
    print("Yearly Rent\t\t", stats["yearly_rent"])
    print("Monthly Rent After Tax\t", stats["monthly_rent_taxed"])
    print("Yearly Rent After Tax\t", stats["yearly_rent_taxed"])
    print("Taxed Rent Per Day\t", stats["taxed_rent_per_day"])
    print("===================================")

    print("TAXES")
    print("===================================")
    print("Tax Per Day\t\t", taxes["per_day"])
    print("Monthly Tax\t\t", taxes["monthly_tax"])
    print("11 Months Tax\t\t", taxes["11_month_tax"])
    print("June Tax\t\t", taxes["june_only"])
    print("Total Tax\t\t", taxes["actual_yearly_tax"])
    print("===================================")

    print("EXTRAS")
    print("===================================")
    print("Next Rent\t\t", extras["next_rent"])
    #print("Next Rent Yearly Tax\t", extras["next_rent_tax"])
    print("Next Rent Per Day Tax\t", extras["next_rent_tax_per_day"])
    print("===================================")

stats = {  
    "monthly_rent": None,
    "yearly_rent": None,
    "monthly_rent_taxed": None,
    "yearly_rent_taxed": None,
    "taxed_rent_per_day": None
}

taxes = {
    "per_day": None,
    "monthly_tax": None,
    "11_month_tax": None,
    "june_only":None,
    "actual_yearly_tax": None
}

extras = {
    "next_rent": None,
    "next_rent_tax": None,
    "next_rent_tax_per_day": None,

}

if __name__ == "__main__":
    
    stats["monthly_rent"] = int(input("\nEnter Monthly Rent: ")) ; stats["yearly_rent"] = stats["monthly_rent"] * 12
    yearlyTax = taxRate(stats["yearly_rent"])
    
    calculateTaxed(yearlyTax)
    calculateJune()
    calculateActualTax()
    
    calculateStats()
    
    #print(stats,end="\n\n")
    #print(taxes,end="\n\n")
    #print(extras,end="\n\n")

    display()
    
    input("Press enter and exit")

    '''
    print("\n")
    
    print(yearlyTax,end="\n\n")
    print(stats,end="\n\n")

    
    print(taxes,end="\n\n")

    
    print(stats,end="\n\n")
    '''
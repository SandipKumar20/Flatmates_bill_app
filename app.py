from flat import Bill, Flatmate
from reports import PdfReport

bill_amount = float(input("Enter the bill amount: "))
bill_period = input("Enter the bill period: E.g. October 2022: ")

your_name = input("Enter your name: ")
your_days = int(input(f"Enter the number of days {your_name} stayed in the house during the bill period: "))

flatmate_name = input("Enter your flatmate's name: ")
flatmate_days = int(input(f"Enter the number of days {flatmate_name} stayed in the house during the bill period: "))

the_bill = Bill(amount=bill_amount, period=bill_period)
you = Flatmate(name=your_name, days_in_house=your_days)
flatmate = Flatmate(name=flatmate_name, days_in_house=flatmate_days)

print(f"{you.name} pays: ", you.pays(bill=the_bill, flatmate=flatmate))
print(f"{flatmate.name} pays: ", flatmate.pays(bill=the_bill, flatmate=you))

# Generate and open pdf
pdf_report = PdfReport(filename=f"{the_bill.period}_Report.pdf")
pdf_report.generate(flatmate1=you, flatmate2=flatmate, bill=the_bill)
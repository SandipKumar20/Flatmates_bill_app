import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about flatmates such as
    their names, their due amount and the period of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()
        # Add image
        pdf.image("files/house.png", w=30, h=30)
        # Add title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
        # Add period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=48, txt="Period:", border=0)
        pdf.cell(w=150, h=48, txt=bill.period, border=0, ln=1)
        # Add name and amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill=bill, flatmate=flatmate2), 2)), border=0, ln=1)
        # Add name and amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill=bill, flatmate=flatmate1), 2)), border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)

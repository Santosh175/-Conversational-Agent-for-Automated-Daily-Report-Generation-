from Data_Extraction import extract_sales_data # for test purpose
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import matplotlib.pyplot as plt


# Generate report
def generate_report(df):
    try:
        # Create a PDF object
        doc = SimpleDocTemplate("todays_sales_report.pdf", pagesize=A4 )
        # Add title
        styles = getSampleStyleSheet()
        title = Paragraph("Sales Report", styles['Heading1'] )

        
        # Select only the Order Number, Product Line, Deal Size columns
        df = df[["ORDERNUMBER", "PRODUCTLINE", "DEALSIZE"]]
        
        # Limit the number of rows to 10
        df = df.head(34)
        
        # Add title
        styles = getSampleStyleSheet()
        title = Paragraph("Sales Report", styles['Heading1'])
        title.hAlign = 'CENTER'  # Center the title horizontally
        title.vAlign = 'BOTTOM'  # Align the title to the bottom
        
        # Add data in tabular form
        data = [
            df.columns.tolist(),
            *df.values.tolist()
        ]
        table = Table(data)
        table_style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ])
        table.setStyle(table_style)
        
        # Add analysis chart
        plt.figure(figsize=(5,4 ))  # Adjusted figure size
        plt.bar(df['PRODUCTLINE'], df['DEALSIZE'])
        plt.xlabel('Product Line')
        plt.ylabel('Deal Size')
        plt.title('Deal Size by Product Line')
        plt.tight_layout()  # Adjusted layout to fit the plot
        plt.savefig('chart.png', bbox_inches='tight')
        chart = Image('chart.png')
                
        # Build the report
        report = [title, table, chart]
        doc.build(report)

        print("Report generating.....")
    except Exception as e:
        print(f"Error generating report: {e}")

#  Test part

'''# Main program
def main():
    file_path = "Sample Sales Data- Interns task.xlsx"  # Replace with your file path
    df = extract_sales_data(file_path)
    
    if df is not None:
        generate_report(df)

if __name__ == "__main__":
    main()'''
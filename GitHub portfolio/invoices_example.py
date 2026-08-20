import os
from contextlib import chdir
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import date
from pathlib import Path





#CHANGE MEEEE!!!!!

gig_date= "01-08-2026"
gig_description="Wedding"
items=[[f'Example Band Performance 120 mins {gig_date}',1500],
       ['Equipment hire',400],
       ["Trumpet McHorn travel costs (fuel)", 41.63],
       ["Alex Alto travel costs (trains)", 48.19],
       ["Dr. U. M. Sticks travel costs (trains)",30.05],
       ["Bass Fish travel costs (trains)", 26.60],
       ["Iris Creighton travel costs (fuel)", 40],
       ["Mick Singh travel costs (fuel)", 35],
       ["Tom Bone travel costs (trains)", 36],
       ["Deposit Received 27/07/2026", -500]
       ]

name="Bride and Groom"
address="123 Fake Street\nCambridge, UK\nCB2 1TQ"
invoice_number=18



###########################################################################
###########################################################################

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
total=sum(item[1] for item in items)

file_name = f"Band Invoices {gig_description} {gig_date}.pdf"

canvas = Canvas(file_name)
textobject = canvas.beginText()

margin_size=30

def_font_size=16
top_margin=842-margin_size
left_column=margin_size
right_column=400
subheader=480
right_margin=595-margin_size


#logo
logo_size=95
if os.path.exists('IMG_0778.jpeg'):
    canvas.drawImage(image='IMG_0778.jpeg', x=465, y=top_margin-logo_size, width=logo_size, height=logo_size, mask=None)
else:
    print("Warning: 'IMG_0778.jpeg' logo image not found in running directory.")

#header
header_font_size=38
canvas.setFont('Helvetica', header_font_size)
canvas.drawString(left_column, top_margin-header_font_size, 'Band Name')

#address
address_begin_line = top_margin-header_font_size-45
textobject.setTextOrigin(left_column, address_begin_line)
textobject.setFont('Helvetica', def_font_size)
textobject.textLines(f"Iris Creighton\nTrinity College\nCambridge, UK\nCB2 1TQ")
textobject.textLine("")
textobject.textLine(f"Bill to:")
textobject.textLine("")
textobject.setFont('Helvetica-Bold', def_font_size)
textobject.textLine(f"{name}")
textobject.setFont('Helvetica', def_font_size)
textobject.textLines(f"{address}")



#invoice number and date
textobject.setTextOrigin(right_column, 675)
textobject.setFont('Helvetica', 32)
textobject.textLine('Invoice')
textobject.setTextOrigin(right_column, 645)
textobject.setFont('Helvetica-Bold', def_font_size)
textobject.textOut('Invoice')
textobject.setFont('Helvetica', def_font_size)
textobject.textLine(f' No. {invoice_number}')
textobject.setFont('Helvetica-Bold', def_font_size)
textobject.textOut('Date:')
textobject.setFont('Helvetica', def_font_size)
textobject.textLine(f' {d1}')

#subheader
canvas.setFont('Helvetica-Bold', def_font_size)
canvas.drawString(left_column, subheader, "Description")
canvas.drawString(right_column, subheader,"Fee (£)")
canvas.line(left_column-10, subheader-15,right_margin, subheader-15)

def itemise(start_y,w0,w1):
    styles = getSampleStyleSheet()
    description_style = ParagraphStyle(
            'ItemDescription',
            parent=styles['Normal'],
            fontSize=def_font_size,
            leading=def_font_size
        )

    price_style = ParagraphStyle(
            'ItemPrice',
            parent=styles['Normal'],
            alignment=2, # 2 corresponds to TA_RIGHT
            fontSize=def_font_size,
            leading=def_font_size
        )

    table_content=[]
    for item,price in items:
        table_content.append([Paragraph(item, description_style),
            Paragraph(f"{price:.2f}", price_style)])

    invoice_table = Table(table_content, colWidths=[w0, w1])
    invoice_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Clean spacing between rows
        ('TOPPADDING', (0, 0), (-1, -1), 6)
    ]))

    table_width, table_height = invoice_table.wrap(w0+w1, 400)
    invoice_table.drawOn(canvas, left_column-6, start_y-table_height)

    return start_y-table_height

bottom_line = itemise(subheader-20,400,100)-15


canvas.line(left_column-10, bottom_line,right_margin, bottom_line)

#my bank details
textobject.setTextOrigin(left_column, bottom_line-30)
textobject.setFont('Helvetica-Bold', def_font_size)
textobject.textLine('Payment Details:')
textobject.setFont('Helvetica', def_font_size)
textobject.textLines('Name: Iris Creighton\nCode: 01-02-03\nAccount Number: 12345678')

#total
canvas.setFont('Helvetica-Bold', def_font_size)
canvas.drawString(right_column, bottom_line-30-2.5*def_font_size, "Total:")
canvas.setFont('Helvetica', def_font_size)
canvas.drawRightString(right_margin, bottom_line-30-2.5*def_font_size, f"£{total:.2f}")
canvas.line(right_column-3, bottom_line-30-2.5*def_font_size-4,right_margin+3, bottom_line-30-2.5*def_font_size-4)

textobject.setFont('Helvetica', 10)
textobject.setTextOrigin(left_column, margin_size)
textobject.textLine("Payment to be received no later than 7 days from the date of issue.")


canvas.drawText(textobject)


with chdir(os.path.join(Path.home(),"invoices")):
    canvas.save()
print(f"Successfully saved: {file_name}")
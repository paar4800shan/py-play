import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import datetime

doc = SimpleDocTemplate("form_letter2.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
Story=[]
logo = "d:\\1.png"
magName = "Pythonista"
issueNum = 12
subPrice = "99.00"
limitedDate = datetime.today().strftime('%Y-%m-%d')
freeGift = "tin foil hat"

formatted_time = time.ctime()
full_name = "Wells Fargo Tech Spotlight"
address_parts = ["66/1 Raidurga Village, Serilingampalli", "Hyderabad", "Telangana 500008"]
'''
im = Image(logo)
Story.append(im)

'''
l1 = Paragraph('line 1', styles["Normal"])
l2 = Paragraph('line 2', styles["Normal"])
data= [(l1, l2)]
t = Table(data, [250, 250])
t.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'TOP')
            ]))
im = Image('d:\\wf.jpeg',hAlign="LEFT")
Story.append(im)
Story.append(t)





styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
ptext = '%s' % formatted_time

Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))

# Create return address
ptext = '%s' % full_name
Story.append(Paragraph(ptext, styles["Normal"]))       
for part in address_parts:
    ptext = '%s' % part.strip()
    Story.append(Paragraph(ptext, styles["Normal"]))   

Story.append(Spacer(1, 12))
ptext = 'Dear Client'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))

ptext = 'We would like to welcome you to our subscriber base for %s Magazine! \
        You will receive %s issues at the excellent introductory price of $%s. Please respond by\
        %s to start receiving your subscription and get the following free gift: %s.' % (magName, 
                                                                                                issueNum,
                                                                                                subPrice,
                                                                                                limitedDate,
                                                                                                freeGift)
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))


ptext = 'Thank you very much and we look forward to serving you.'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))
ptext = 'Sincerely,'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 48))
ptext = 'Wells Fargo CCIBT Team'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
doc.build(Story)
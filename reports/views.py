from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from survey.models import SurveyResponse
import datetime

# --- Custom header/footer ---
def add_page_number(canvas, doc):
    canvas.saveState()
    page_num = canvas.getPageNumber()
    canvas.setFont('Helvetica', 8)
    canvas.drawRightString(19*cm, 1*cm, f"Page {page_num}")
    canvas.restoreState()

@login_required
def generate_report(request):
    data = SurveyResponse.objects.filter(user=request.user).last()
    if not data:
        return HttpResponse("No survey data found.")

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mental_health_report.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)

    # --- Styles ---
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='TitleCenter', parent=styles['Title'], alignment=1, spaceAfter=12))
    styles.add(ParagraphStyle(name='SectionHeader', parent=styles['Heading1'], textColor=colors.HexColor('#0d6efd'), spaceBefore=6, spaceAfter=6))
    styles.add(ParagraphStyle(name='NormalJustify', parent=styles['Normal'], spaceAfter=4, leading=12))
    styles.add(ParagraphStyle(name='TableHeader', parent=styles['Normal'], alignment=1, fontSize=10, textColor=colors.white))

    content = []

    # --- Cover / Report Header ---
    content.append(Paragraph("🧠 Student Mental Health Report", styles['TitleCenter']))
    content.append(Paragraph(f"Student: {request.user.username}", styles['NormalJustify']))
    content.append(Paragraph(f"Date: {datetime.datetime.now().strftime('%d %b %Y')}", styles['NormalJustify']))
    content.append(Spacer(1, 6))  # reduced spacer height

    # --- Basic Info ---
    content.append(Paragraph("Basic Information", styles['SectionHeader']))
    basic_info_data = [
        ['Field', 'Details'],
        ['Gender', dict(data.GENDER_CHOICES).get(data.gender)],
        ['Age Group', dict(data.AGE_CHOICES).get(data.age_group)],
        ['Study Year', dict(data.STUDY_CHOICES).get(data.study_year)],
        ['University Type', dict(data.UNIVERSITY_CHOICES).get(data.university_type)],
        ['Living Place', dict(data.LIVING_CHOICES).get(data.living_place)],
    ]
    table = Table(basic_info_data, hAlign='LEFT', colWidths=[6*cm, 9*cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d6efd')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.gray),
        ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
    ]))
    content.append(table)
    content.append(Spacer(1, 6))  # smaller spacing

    # --- Lifestyle Summary ---
    content.append(Paragraph("Lifestyle Summary", styles['SectionHeader']))
    lifestyle_data = [
        ['Field', 'Details'],
        ['Sleep Hours', dict(data.SLEEP_CHOICES).get(data.sleep_hours)],
        ['Device Usage', dict(data.DEVICE_CHOICES).get(data.device_usage)],
        ['Breakfast Habit', dict(data.FOOD_CHOICES).get(data.breakfast)],
        ['Addictions', dict(data.ADDICTION_CHOICES).get(data.addiction)],
    ]
    table = Table(lifestyle_data, hAlign='LEFT', colWidths=[6*cm, 9*cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d6efd')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.gray),
        ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
    ]))
    content.append(table)
    content.append(Spacer(1, 6))

    # --- Mental Health Indicators ---
    content.append(Paragraph("Mental Health Indicators", styles['SectionHeader']))
    mental_data = [
        ['Field', 'Details'],
        ['Interest Level', dict(data.MENTAL_CHOICES).get(data.interest)],
        ['Anxiety Level', dict(data.MENTAL_CHOICES).get(data.anxiety)],
        ['Social Feeling', dict(data.SOCIAL_CHOICES).get(data.social_feeling)],
        ['Self Rating', dict(data.SELF_CHOICES).get(data.self_rating)],
    ]
    table = Table(mental_data, hAlign='LEFT', colWidths=[6*cm, 9*cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d6efd')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.gray),
        ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
    ]))
    content.append(table)
    content.append(Spacer(1, 6))

    # --- Risk Assessment ---
    content.append(Paragraph("Risk Assessment", styles['SectionHeader']))
    content.append(Paragraph(f"Risk Level: <b>{data.risk_level}</b>", styles['NormalJustify']))
    content.append(Paragraph(f"Score: <b>{data.score}</b>", styles['NormalJustify']))
    content.append(Spacer(1, 6))

    # --- Recommendations ---
    content.append(Paragraph("Recommendations", styles['SectionHeader']))
    if data.risk_level == "High":
        advice = "⚠️ High risk detected. Immediate consultation with a counselor or trusted person is recommended."
    elif data.risk_level == "Medium":
        advice = "⚠️ Moderate stress detected. Maintain healthy habits and monitor your mental health."
    else:
        advice = "✅ Your mental health condition appears stable. Keep up the good habits."

    content.append(Paragraph(advice, styles['NormalJustify']))

    # --- Build PDF ---
    doc.build(content, onFirstPage=add_page_number, onLaterPages=add_page_number)

    return response
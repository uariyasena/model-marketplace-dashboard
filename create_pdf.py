from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas

# Apex colors
APEX_NAVY = colors.HexColor('#002060')
APEX_BLUE = colors.HexColor('#0066CC')
APEX_BRIGHT_BLUE = colors.HexColor('#3B82F6')
APEX_SKY_BLUE = colors.HexColor('#00B0F0')
APEX_AMETHYST = colors.HexColor('#802CC0')
APEX_AMETHYST_PINK = colors.HexColor('#EC0075')
APEX_GREEN = colors.HexColor('#28A745')
APEX_GOLD = colors.HexColor('#FBBF24')

def create_pdf():
    doc = SimpleDocTemplate("Model_Marketplace_Framework.pdf", pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    Story = []
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=APEX_NAVY,
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=APEX_BLUE,
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )

    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=APEX_AMETHYST,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=6
    )

    # PAGE 1: Cover Page
    Story.append(Spacer(1, 2*inch))
    Story.append(Paragraph("APEX CLEARING", title_style))
    Story.append(Paragraph("Model Marketplace", ParagraphStyle(
        'Subtitle',
        parent=styles['Heading2'],
        fontSize=20,
        textColor=APEX_AMETHYST_PINK,
        alignment=TA_CENTER,
        spaceAfter=20
    )))
    Story.append(Spacer(1, 0.3*inch))
    Story.append(Paragraph("Business Framework & Implementation Guide", ParagraphStyle(
        'Subtitle2',
        parent=styles['BodyText'],
        fontSize=14,
        textColor=APEX_BLUE,
        alignment=TA_CENTER,
        spaceAfter=20
    )))
    Story.append(Spacer(1, 1*inch))
    Story.append(Paragraph("Version 1.1 | March 2026", ParagraphStyle(
        'Version',
        parent=styles['BodyText'],
        fontSize=10,
        textColor=colors.grey,
        alignment=TA_CENTER
    )))
    Story.append(PageBreak())

    # PAGE 2: What is Model Marketplace?
    Story.append(Paragraph("What is Model Marketplace?", heading_style))
    Story.append(Paragraph(
        "Model Marketplace is Apex Clearing's centralized platform that enables investment advisors to discover, "
        "subscribe to, and implement third-party investment models directly within Ascend Workstation.",
        body_style
    ))
    Story.append(Spacer(1, 0.1*inch))

    Story.append(Paragraph("Core Functionality", subheading_style))
    Story.append(Paragraph(
        "<b>What it does:</b><br/>"
        "• Provides a curated marketplace of vetted investment models from institutional providers<br/>"
        "• Enables one-click subscription to professional asset allocation strategies<br/>"
        "• Automatically delivers model updates from providers to subscribed clients<br/>"
        "• Integrates subscribed models directly into Apex Rebalancer as ready-to-use portfolio goals<br/><br/>"

        "<b>Why it matters:</b><br/>"
        "• Saves advisors time by eliminating manual model building<br/>"
        "• Provides access to institutional-grade strategies<br/>"
        "• Keeps portfolios automatically aligned with provider updates<br/>"
        "• Differentiates Apex correspondents in competitive marketplace",
        body_style
    ))
    Story.append(Spacer(1, 0.2*inch))

    Story.append(Paragraph("Key Value Propositions", subheading_style))
    value_props = [
        ["Centralized Access", "Browse and subscribe to vetted third-party models in one location"],
        ["Streamlined Implementation", "Seamless integration with Ascend Rebalancer for portfolio management"],
        ["Automated Updates", "Model providers push updates directly to subscribed clients"],
        ["Compliance Built-In", "Terms & conditions acceptance workflow at platform and provider levels"],
        ["Scalable Growth", "Positioned as competitive differentiator for Apex correspondents"]
    ]

    t = Table(value_props, colWidths=[1.5*inch, 4*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), APEX_BLUE),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    Story.append(t)
    Story.append(Spacer(1, 0.2*inch))

    Story.append(Paragraph("How Model Marketplace Connects to Rebalancer", subheading_style))
    Story.append(Paragraph(
        "<b>The Integration:</b><br/>"
        "Model Marketplace and Rebalancer work as an integrated ecosystem. When an advisor subscribes to a model "
        "in Model Marketplace, that model automatically becomes available as a 'Goal' in Rebalancer.<br/><br/>"

        "<b>The Workflow:</b><br/>"
        "1. <b>Subscribe</b> in Model Marketplace → Model appears in Rebalancer Goals list<br/>"
        "2. <b>Configure</b> in Rebalancer → Assign the goal to client accounts<br/>"
        "3. <b>Rebalance</b> in Rebalancer → Generate buy/sell orders to match the model<br/>"
        "4. <b>Auto-Update</b> → When provider updates the model, Rebalancer goal updates automatically<br/><br/>"

        "<b>Key Point:</b> Model Marketplace is the 'shopping' experience. Rebalancer is the 'implementation' tool. "
        "You need both to use third-party models effectively.",
        body_style
    ))
    Story.append(Spacer(1, 0.2*inch))

    Story.append(Paragraph("Current Status (Q1 2026)", subheading_style))
    Story.append(Paragraph(
        "<b>Total Providers:</b> 4 (Franklin Templeton, Morningstar, Vanguard, BlackRock)<br/>"
        "<b>Models Available:</b> 12+<br/>"
        "<b>Target Clients:</b> 38 existing Rebalancer firms (500+ total Apex correspondents)<br/>"
        "<b>Phase:</b> Marketing launch & press release (Q2 2026)",
        body_style
    ))
    Story.append(PageBreak())

    # PAGE 3: Success Metrics
    Story.append(Paragraph("Success Metrics & Targets (2026)", heading_style))

    Story.append(Paragraph("Adoption Funnel", subheading_style))
    adoption_data = [
        ["Metric", "Current (Q1)", "Target (2026)"],
        ["Total Rebalancer Clients", "500", "38 enabled"],
        ["MM Enabled Clients", "38", "30 (80%)"],
        ["Users with Subscribe Permission", "TBD", "100+"],
        ["Active Model Subscriptions", "Growing", "200+"]
    ]

    t = Table(adoption_data, colWidths=[2.2*inch, 1.5*inch, 1.8*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), APEX_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    Story.append(t)
    Story.append(Spacer(1, 0.2*inch))

    Story.append(Paragraph("Business Impact Targets", subheading_style))
    impact_data = [
        ["Metric", "Target"],
        ["AUM in Models", "$500M+ by EOY 2026"],
        ["Revenue per Model", "$50K average annual"],
        ["Client Retention Impact", "+15% for MM users"],
        ["New Correspondent Wins", "MM cited in 25% of pitches"]
    ]

    t = Table(impact_data, colWidths=[2.5*inch, 3*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), APEX_AMETHYST),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    Story.append(t)
    Story.append(PageBreak())

    # PAGE 4: 8-Step Process Flow
    Story.append(Paragraph("How Users Access & Use Model Marketplace", heading_style))
    Story.append(Paragraph(
        "This 8-step process shows the complete client journey from initial setup through active portfolio management.",
        body_style
    ))
    Story.append(Spacer(1, 0.2*inch))

    steps = [
        ("Step 1: Initial Access Setup",
         "WHO: Apex Onboarding Team / Client Configurator Team<br/>"
         "WHAT: Enable Model Marketplace at correspondent level<br/>"
         "WHERE: Client Configurator → Experience Settings → Enable Model Marketplace<br/>"
         "TIMELINE: Completed during client onboarding"),

        ("Step 2: User Permission Configuration",
         "WHO: Client Administrator / Apex Client Services<br/>"
         "WHAT: Grant subscribe permissions to specific users<br/>"
         "WHERE: User management interface<br/>"
         "TIMELINE: Before first use"),

        ("Step 3: Client Acceptance & Discovery",
         "WHO: End Client/Advisor<br/>"
         "WHAT: Sign in to Ascend Workstation → Trading → Model Marketplace<br/>"
         "WHERE: Accept Apex Terms & Conditions (one-time, all providers)<br/>"
         "TIMELINE: 5-10 minutes (one-time setup)"),

        ("Step 4: Model Evaluation",
         "WHO: Client/Advisor<br/>"
         "WHAT: Review model details: Holdings, Target Weights, Summary, Resources<br/>"
         "WHERE: Columns: Provider | Model | Investment Vehicle | Status<br/>"
         "TIMELINE: Variable - depends on research depth"),

        ("Step 5: Model Subscription",
         "WHO: Authorized Client User (with subscribe permission)<br/>"
         "WHAT: Click Subscribe → Accept Provider-Specific T&Cs<br/>"
         "WHERE: Status changes: AVAILABLE → SUBSCRIBED, Button: Green → Red<br/>"
         "TIMELINE: 2-3 minutes per model"),

        ("Step 6: Post-Subscription Configuration in Rebalancer",
         "WHO: Client/Advisor<br/>"
         "WHAT: CRITICAL - Verify asset class assignments for each security<br/>"
         "WHERE: Rebalancer → Settings → Models → Create Goals → Assign to Accounts<br/>"
         "TIMELINE: 15-30 minutes for first model"),

        ("Step 7: Portfolio Rebalancing",
         "WHO: Client/Advisor<br/>"
         "WHAT: Initiate rebalance → Review generated buy/sell orders → Submit trades<br/>"
         "WHERE: Review compliance disclosures before submission<br/>"
         "TIMELINE: Variable based on portfolio size"),

        ("Step 8: Unsubscribe (Optional)",
         "WHO: Client/Advisor<br/>"
         "WHAT: Stops automatic updates but retains last subscribed weights<br/>"
         "WHERE: To fully discontinue: Delete model from Rebalancer<br/>"
         "TIMELINE: Immediate")
    ]

    for i, (title, desc) in enumerate(steps, 1):
        Story.append(Paragraph(f"<b>{title}</b>", subheading_style))
        Story.append(Paragraph(desc, body_style))
        if i == 4:
            Story.append(PageBreak())
            Story.append(Paragraph("8-Step Implementation Process (continued)", heading_style))

    Story.append(Spacer(1, 0.1*inch))
    Story.append(Paragraph("<b>KEY LIMITATION:</b> Apex does NOT automatically execute trades. Automatic scheduled rebalancing planned for Q3 2026. Clients must currently review and submit all trade orders manually.",
                          ParagraphStyle('Warning', parent=body_style, textColor=colors.red, fontName='Helvetica-Bold')))
    Story.append(PageBreak())

    # PAGE 5: Client Communication Strategy
    Story.append(Paragraph("Client Communication & Marketing Strategy", heading_style))

    Story.append(Paragraph("Target Audiences", subheading_style))
    audiences = [
        ["Audience", "Count", "Approach"],
        ["Existing Rebalancer Clients", "38 firms", "Direct outreach, already using platform"],
        ["Ascend Classic Clients Post-Migration", "TBD", "Will have Rebalancer access after conversion"],
        ["New Rebalancer Prospects", "Market", "Model Marketplace as differentiator"]
    ]

    t = Table(audiences, colWidths=[2*inch, 1.3*inch, 2.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), APEX_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    Story.append(t)
    Story.append(Spacer(1, 0.2*inch))

    Story.append(Paragraph("Communication Channels", subheading_style))
    Story.append(Paragraph(
        "<b>1. Direct Outreach:</b> Personalized emails to 38 existing Rebalancer clients highlighting immediate value<br/>"
        "<b>2. Documentation & Resources:</b> Service Center articles, video tutorials, quick-start guides<br/>"
        "<b>3. Press Release:</b> Q2 2026 announcement targeting industry publications and fintech media<br/>"
        "<b>4. Internal Enablement:</b> Sales team training, demo environment, objection handling scripts",
        body_style
    ))
    Story.append(PageBreak())

    # PAGE 6: Provider Integration
    Story.append(Paragraph("Provider Integration & Management", heading_style))

    Story.append(Paragraph("Current Providers", subheading_style))
    providers = [
        ["Provider", "Models", "Integration Method"],
        ["Franklin Templeton", "Multiple ETF models", "SFTP (daily updates)"],
        ["Morningstar", "Asset allocation models", "API integration"],
        ["Vanguard", "Target-date & balanced", "API integration"],
        ["BlackRock", "iShares-based models", "API integration"]
    ]

    t = Table(providers, colWidths=[1.8*inch, 1.8*inch, 1.9*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), APEX_AMETHYST),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    Story.append(t)
    Story.append(Spacer(1, 0.2*inch))

    Story.append(Paragraph("Provider Acquisition Strategy", subheading_style))
    Story.append(Paragraph(
        "Q3 2026 roadmap includes dedicated Business Development resource for provider acquisition. "
        "Target: 10+ providers by EOY 2026. Focus on asset managers with established ETF/mutual fund models "
        "and strong brand recognition among RIAs.",
        body_style
    ))
    Story.append(Spacer(1, 0.2*inch))

    Story.append(Paragraph("Technical Requirements for New Providers", subheading_style))
    Story.append(Paragraph(
        "- API or SFTP integration capability for model updates<br/>"
        "- Legal agreement for terms & conditions display<br/>"
        "- Model metadata: holdings, target weights, rebalancing frequency<br/>"
        "- Compliance documentation and disclosures<br/>"
        "- Dedicated support contact for client inquiries",
        body_style
    ))
    Story.append(PageBreak())

    # PAGE 7: Rebalancer Integration
    Story.append(Paragraph("Rebalancer Capabilities & Integration", heading_style))

    Story.append(Paragraph("What is Rebalancer?", subheading_style))
    Story.append(Paragraph(
        "Rebalancer is Apex's portfolio management tool that enables advisors to create target asset allocations "
        "(goals), assign them to accounts, and generate buy/sell orders to align portfolios with those targets. "
        "Model Marketplace subscriptions automatically populate as available goals within Rebalancer.",
        body_style
    ))
    Story.append(Spacer(1, 0.2*inch))

    Story.append(Paragraph("Core Rebalancer Features", subheading_style))
    features = [
        ["Feature", "Description"],
        ["Goals Management", "Create custom asset allocation targets or use subscribed models"],
        ["Account Assignment", "Link goals to individual or household accounts"],
        ["Drift Monitoring", "Track portfolio deviation from target allocation"],
        ["Order Generation", "Automated buy/sell recommendations to rebalance"],
        ["Tax Optimization", "Tax-loss harvesting and gain/loss awareness"],
        ["Compliance Checks", "Pre-trade compliance rules and disclosures"]
    ]

    t = Table(features, colWidths=[1.8*inch, 3.7*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), APEX_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    Story.append(t)
    Story.append(Spacer(1, 0.2*inch))

    Story.append(Paragraph("Critical Post-Subscription Step", subheading_style))
    Story.append(Paragraph(
        "<b>Asset Class Verification:</b> After subscribing to a model, clients MUST verify that each security "
        "in the model has the correct asset class assignment in Rebalancer. Incorrect assignments will cause "
        "rebalancing errors. This is a one-time setup per model but is frequently missed by new users.",
        ParagraphStyle('Critical', parent=body_style, textColor=colors.red, fontName='Helvetica-Bold')
    ))
    Story.append(PageBreak())

    # PAGE 8: Roadmap
    Story.append(Paragraph("Roadmap & Future Enhancements", heading_style))

    Story.append(Paragraph("2026 Roadmap", subheading_style))
    roadmap = [
        ["Quarter", "Initiative", "Status"],
        ["Q2 2026", "Marketing Launch & Press Release", "IN PROGRESS"],
        ["Q2 2026", "Enhanced Provider Onboarding Process", "IN PROGRESS"],
        ["Q3 2026", "Automatic Scheduled Rebalancing", "PLANNED"],
        ["Q3 2026", "Dedicated BD Resource for Provider Acquisition", "PLANNED"],
        ["Q4 2026", "Advanced Filtering & Search (ESG, risk level)", "PLANNED"],
        ["Q4 2026", "Model Performance Analytics Dashboard", "PLANNED"]
    ]

    t = Table(roadmap, colWidths=[1*inch, 3.3*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), APEX_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    Story.append(t)
    Story.append(Spacer(1, 0.2*inch))

    Story.append(Paragraph("Top Priority: Automatic Scheduled Rebalancing", subheading_style))
    Story.append(Paragraph(
        "Currently, clients must manually initiate rebalancing and submit trades. Q3 2026 will introduce "
        "automatic scheduled rebalancing where clients can set recurring rebalance schedules (weekly, monthly, quarterly). "
        "This removes manual overhead and ensures portfolios stay aligned with model updates.",
        body_style
    ))
    Story.append(Spacer(1, 0.2*inch))

    Story.append(Paragraph("Long-Term Vision (2027+)", subheading_style))
    Story.append(Paragraph(
        "- Direct indexing integration for tax-optimized model implementation<br/>"
        "- AI-powered model recommendations based on client risk profiles<br/>"
        "- White-label option for correspondents to feature their own models<br/>"
        "- Integration with proposal generation tools for new business pitches",
        body_style
    ))
    Story.append(PageBreak())

    # PAGE 9: Common Questions
    Story.append(Paragraph("Common Questions & Objections", heading_style))

    qna = [
        ("What if a client unsubscribes from a model?",
         "The model remains in Rebalancer with the last subscribed weights. The client stops receiving automatic updates. To fully remove, they must delete the goal in Rebalancer."),

        ("Can clients customize subscribed models?",
         "No. Models are delivered as-is from providers. Clients can create custom goals separately in Rebalancer if they need customization."),

        ("What happens if a provider discontinues a model?",
         "Clients retain access to the last published weights. Apex notifies affected subscribers and recommends alternative models."),

        ("Is there a cost to clients for Model Marketplace?",
         "No platform fee from Apex. Some providers may charge advisory fees directly - this is disclosed in provider T&Cs before subscription."),

        ("How often do models update?",
         "Varies by provider. Franklin Templeton updates daily via SFTP. Most others update monthly or quarterly. Update frequency is shown in model details."),

        ("What if a client doesn't have Rebalancer enabled?",
         "Model Marketplace requires Rebalancer access. This is a bundled feature discussion for Sales team during correspondent onboarding.")
    ]

    for i, (question, answer) in enumerate(qna, 1):
        Story.append(Paragraph(f"<b>Q{i}: {question}</b>", subheading_style))
        Story.append(Paragraph(answer, body_style))
        Story.append(Spacer(1, 0.1*inch))

    Story.append(PageBreak())

    # PAGE 10: Contact & Resources
    Story.append(Paragraph("Contact Directory & Resources", heading_style))

    Story.append(Paragraph("Key Contacts", subheading_style))
    contacts = [
        ["Role", "Contact"],
        ["Product Owner", "Neema Raphael - neema.raphael@apexclearing.com"],
        ["Technical Support", "Ascend Support - support@apexclearing.com"],
        ["Sales Inquiries", "Business Development - bd@apexclearing.com"],
        ["Provider Partnerships", "BD Team - partnerships@apexclearing.com"]
    ]

    t = Table(contacts, colWidths=[1.8*inch, 3.7*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), APEX_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    Story.append(t)
    Story.append(Spacer(1, 0.3*inch))

    Story.append(Paragraph("Documentation Resources", subheading_style))
    Story.append(Paragraph(
        "<b>Apex Service Center:</b> Knowledge base articles and video tutorials<br/>"
        "<b>Quick Start Guide:</b> Step-by-step PDF for first-time users<br/>"
        "<b>API Documentation:</b> For correspondents building custom integrations<br/>"
        "<b>Provider Showcase:</b> Detailed profiles of available model providers",
        body_style
    ))
    Story.append(Spacer(1, 0.3*inch))

    Story.append(Paragraph("Training & Enablement", subheading_style))
    Story.append(Paragraph(
        "Monthly webinars for correspondent staff covering Model Marketplace features, best practices, "
        "and new provider announcements. Demo environment available for sandbox testing before going live with clients.",
        body_style
    ))
    Story.append(Spacer(1, 1*inch))

    Story.append(Paragraph("---", ParagraphStyle('Line', parent=body_style, alignment=TA_CENTER)))
    Story.append(Spacer(1, 0.2*inch))
    Story.append(Paragraph(
        "<b>Document Version:</b> 1.1 | <b>Last Updated:</b> March 2026<br/>"
        "<b>Confidential:</b> For internal Apex use and authorized correspondents only",
        ParagraphStyle('Footer', parent=body_style, fontSize=8, textColor=colors.grey, alignment=TA_CENTER)
    ))

    # Build PDF
    doc.build(Story)
    print("PDF created successfully: Model_Marketplace_Framework.pdf")

if __name__ == "__main__":
    create_pdf()

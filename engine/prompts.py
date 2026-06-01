SPECIALTY_TEMPLATES = {
    "Thoracic Oncology": """
Key talking points:
- Actionable biomarkers: EGFR, ALK, ROS1, MET, RET, KRAS G12C
- Tissue limitations → value of high‑success‑rate NGS
- Rapid TAT for first‑line therapy decisions
- ctDNA utility for progression monitoring
""",
    "GI Oncology": """
Key talking points:
- MSI‑H, KRAS, NRAS, BRAF, HER2, NTRK
- Importance of broad profiling in CRC and pancreatic cancer
- ctDNA for MRD and recurrence monitoring
""",
    "Breast Oncology": """
Key talking points:
- ESR1, PIK3CA, HER2‑low, BRCA1/2
- Utility of RNA + DNA for complex endocrine resistance
- ctDNA for metastatic disease monitoring
""",
    "Hematology": """
Key talking points:
- Myeloid vs lymphoid panels
- Fusion detection and RNA importance
- Rapid TAT for AML/ALL decision‑making
"""
}

def get_specialty_context(specialty):
    return SPECIALTY_TEMPLATES.get(specialty, "No specialty‑specific context available.")


def meeting_script_prompt(physician, specialty, intel, crm, knowledge):
    specialty_context = get_specialty_context(specialty)

    return f"""
You are a Tempus Sales Copilot generating a 30‑second meeting script.

Physician: {physician}
Specialty: {specialty}

Specialty‑Specific Clinical Context:
{specialty_context}

Market Intelligence:
{intel}

CRM Notes:
{crm}

Product Knowledge:
{knowledge}

Generate a concise, confident, specialty‑aware script that:
- Uses the physician’s specialty to anchor value props
- Highlights relevant biomarkers and clinical decisions
- Connects Tempus testing to their patient population
- Ends with a forward‑moving suggestion

Output Format:
Meeting Script (30 seconds):
"""


def objection_handler_prompt(physician, specialty, objection, intel, crm, knowledge):
    specialty_context = get_specialty_context(specialty)

    return f"""
You are a Tempus Sales Copilot generating a specialty‑aware objection response.

Physician: {physician}
Specialty: {specialty}
Objection: "{objection}"

Specialty‑Specific Clinical Context:
{specialty_context}

Market Intelligence:
{intel}

CRM Notes:
{crm}

Product Knowledge:
{knowledge}

Generate a concise, confident objection response that:
- Acknowledges the concern
- Uses specialty‑specific biomarkers or clinical value
- Connects to the physician’s patient population
- Ends with a forward‑moving suggestion

Output Format:
Objection Response:
"""

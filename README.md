# TEMPUS GenAI Product Builder Case Study
### Deployment link: https://tempus-sales-copilot.streamlit.app/
### Github link: https://github.com/Alex-Thomas0828/Tempus-Case-Study

A Streamlit‑based GenAI application that simulates a Tempus Sales Copilot.
The tool ingests physician‑level data, CRM notes, and product knowledge to generate:

- Ranked physician insights

- 30‑second meeting scripts

- Specialty‑aware objection handling

- Specialty‑aware prompt routing

Powered by Groq Llama‑3.3‑70B‑Versatile

## Features
- Physician Ranking Engine: Uses volume, specialty, and market intel to prioritize outreach
- Meeting Script Generator: Creates concise, specialty‑aware 30‑second scripts tailored to each physician
- Objection Handling Engine: Generates confident, specialty‑specific responses to common objections
- Specialty‑Aware Prompt Routing: Automatically adjusts messaging for Thoracic, GI, Breast, and Heme oncology

## File Architecture
Case Study #1/

│

├── app.py                 # Streamlit UI

├── requirements.txt       # Dependencies

├── engine/

│   ├── llm.py             # Groq LLM wrapper

│   ├── prompts.py         # Prompt templates + specialty routing


│   └── __init__.py

└── data/                  # (Optional) Sample CSVs

## Installation
1. Clone the repo
2. Install dependencies: pip install -r requirements.txt
3. Add your .env file: GROQ_API_KEY="your_key_here"
4. Run the app: streamlit run app.py

## Example Workflow  
1. Upload your Market Intelligence CSV, CRM Notes JSON, and Product Knowledge Base Markdown
2. Select a physician from the dropdown  
3. View ranked insights  
4. Click **Generate Meeting Script**  
5. Enter an objection (e.g., “Turnaround time is too slow”)  
6. Click **Generate Objection Response**  



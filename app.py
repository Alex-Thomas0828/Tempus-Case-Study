import streamlit as st
import pandas as pd
import json

from engine.ranking import compute_ranking
from engine.llm import generate_llm_response
from engine.prompts import meeting_script_prompt
from engine.prompts import objection_handler_prompt


st.sidebar.header("Upload Data")

market_file = st.sidebar.file_uploader("Market Intelligence CSV", type=["csv"])
crm_file = st.sidebar.file_uploader("CRM Notes JSON", type=["json"])
product_file = st.sidebar.file_uploader("Product Knowledge Base", type=["md"])

if market_file and crm_file and product_file:

    df = pd.read_csv(market_file, encoding="cp1252")
    crm_notes = json.load(crm_file)
    product_knowledge = product_file.read().decode("utf-8")

    df_ranked = compute_ranking(df)

    physician = st.sidebar.selectbox("Select Physician", df_ranked["Physician"])

    st.subheader("Ranked Provider List")
    st.dataframe(df_ranked)

    if st.button("Generate Meeting Script"):
        row = df_ranked[df_ranked["Physician"] == physician].iloc[0]
        crm_entry = next((x for x in crm_notes if x["physician"] == physician), None)

        prompt = meeting_script_prompt(
            physician,
            row["Specialty"],
            row.to_dict(),
            crm_entry["notes"] if crm_entry else None,
            product_knowledge
        )

        script = generate_llm_response(prompt)
        st.success(script)
    
    st.subheader("Objection Handling")

    objection_text = st.text_input("Enter the physician's objection")

    if st.button("Generate Objection Response"):
        if not objection_text.strip():
            st.warning("Please enter an objection first.")
        else:
            row = df_ranked[df_ranked["Physician"] == physician].iloc[0]
            crm_entry = next((x for x in crm_notes if x["physician"] == physician), None)

            prompt = objection_handler_prompt(
                physician,
                row["Specialty"],
                objection_text,
                row.to_dict(),
                crm_entry["notes"] if crm_entry else None,
                product_knowledge
            )

            response = generate_llm_response(prompt)
            st.success(response)
            

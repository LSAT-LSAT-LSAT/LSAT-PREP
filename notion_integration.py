import os
from notion_client import Client

notion = Client(auth=st.secrets["NOTION_TOKEN"])
DB_ID = st.secrets["NOTION_DB_ID"]

def log_score_to_notion(score_entry):
    notion.pages.create(parent={"database_id": DB_ID},
        properties={
            "Date": {"date": {"start": score_entry["date"]}},
            "PrepTest": {"title": [{"text": {"content": score_entry["pt"]}}]},
            "Raw Score": {"number": score_entry["raw"]},
            "Scaled Score": {"number": score_entry["scaled"]},
            "Notes": {"rich_text": [{"text": {"content": score_entry["notes"]}}]}
        }
    )



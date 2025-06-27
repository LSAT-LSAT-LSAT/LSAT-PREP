
# 📎 Notion Integration Stub (To be customized by user)

from notion_client import Client
import os

# Load secrets from environment or Streamlit secrets
notion = Client(auth=os.environ.get("NOTION_TOKEN"))

# Replace with your Notion database ID
DATABASE_ID = os.environ.get("NOTION_DB_ID")

def log_score_to_notion(score_entry):
    notion.pages.create(parent={"database_id": DATABASE_ID},
                        properties={
                            "Date": {"date": {"start": score_entry["date"]}},
                            "PrepTest": {"title": [{"text": {"content": score_entry["pt"]}}]},
                            "Raw Score": {"number": score_entry["raw"]},
                            "Scaled Score": {"number": score_entry["scaled"]},
                            "Notes": {"rich_text": [{"text": {"content": score_entry["notes"]}}]},
                        })

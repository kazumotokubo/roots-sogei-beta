import streamlit as st
import json

st.title("放課後等デイ送迎最適化システム β版")

# JSONファイル読み込み
with open("children_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

st.subheader("児童データ（仮）一覧")

for child in data.get("児童一覧", []):
    st.markdown(f"- {child}")

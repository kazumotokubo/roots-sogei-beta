import streamlit as st
import json
import pandas as pd

st.title("放課後等デイ送迎最適化システム β版")

# 児童データ一覧（以前のコード）を省略して、配車表示に切り替えます

# 配車結果JSONを読み込み
with open("children_dispatch_result.json", "r", encoding="utf-8") as f:
    配車データ = json.load(f)

# 表示：迎え配車表
st.subheader("🚐 迎え配車表")
迎えdf = pd.DataFrame(配車データ["迎え配車表"])
st.dataframe(迎えdf)

# 表示：送り配車表
st.subheader("🏠 送り配車表")
送りdf = pd.DataFrame(配車データ["送り配車表"])
st.dataframe(送りdf)

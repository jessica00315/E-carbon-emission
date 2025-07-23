# E-carbon-emission.py

import streamlit as st

st.set_page_config(page_title="E-CarbonEmission", layout="wide")

st.title("♻️ 金元福碳排放儀表板")
st.markdown("這是一個展示真空成型塑膠包材碳排資訊化的範例系統。")

# 範例圖表（以靜態資料展示）
import pandas as pd
import plotly.express as px

data = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月"],
    "碳排放量（tCO₂e）": [120, 132, 128, 142, 139]
})
fig = px.line(data, x="月份", y="碳排放量（tCO₂e）", title="每月碳排放趨勢")
st.plotly_chart(fig, use_container_width=True)



st.subheader("📈 每月碳排放趨勢")
st.plotly_chart(fig1)

col1, col2 = st.columns(2)
with col1:
    st.subheader("🏭 廠區碳排佔比")
    st.plotly_chart(fig2)

with col2:
    st.subheader("⚙️ 製程碳排佔比")
    st.plotly_chart(fig3)

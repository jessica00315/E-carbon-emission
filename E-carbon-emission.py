# E_carbon_emission.py

import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

st.set_page_config(page_title="E-CarbonEmission", layout="wide")

# 頁面標題
st.title("♻️ 金元福碳排放儀表板")
st.markdown("這是一個展示真空成型塑膠包材碳排資訊化的範例系統。")

# 📈 每月碳排放趨勢圖（Plotly）
data = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月"],
    "碳排放量（tCO₂e）": [120, 132, 128, 142, 139]
})
fig1 = px.line(data, x="月份", y="碳排放量（tCO₂e）", title="每月碳排放趨勢", markers=True)
st.subheader("📈 每月碳排放趨勢")
st.plotly_chart(fig1, use_container_width=True)

# 🏭 廠區碳排圓餅圖
plant_data = pd.DataFrame({
    "廠區": ["冬山廠", "羅東廠", "宜蘭廠"],
    "碳排放量": [40, 35, 25]
})
fig2 = px.pie(plant_data, names="廠區", values="碳排放量", title="廠區碳排佔比")

# ⚙️ 製程碳排圓餅圖
process_data = pd.DataFrame({
    "製程": ["熔融", "成型", "包裝", "物流"],
    "碳排放量": [50, 30, 15, 5]
})
fig3 = px.pie(process_data, names="製程", values="碳排放量", title="製程碳排佔比")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🏭 廠區碳排佔比")
    st.plotly_chart(fig2, use_container_width=True)
with col2:
    st.subheader("⚙️ 製程碳排佔比")
    st.plotly_chart(fig3, use_container_width=True)

# 📦 單位產品碳排強度（折線圖）
intensity_data = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月"],
    "碳排強度（kgCO₂e/kg）": [2.4, 2.3, 2.1, 2.2, 2.0]
})
fig4 = px.line(intensity_data, x="月份", y="碳排強度（kgCO₂e/kg）", title="單位產品碳排強度", markers=True)
st.subheader("📦 單位產品碳排強度")
st.plotly_chart(fig4, use_container_width=True)

# 🔋 再生能源使用占比
renewable_data = pd.DataFrame({
    "來源": ["綠電", "灰電"],
    "占比": [35, 65]
})
fig5 = px.pie(renewable_data, names="來源", values="占比", title="再生能源使用比例")
st.subheader("🔋 再生能源使用占比")
st.plotly_chart(fig5, use_container_width=True)

# 📄 預覽原始 HTML 結構（從內嵌HTML）
st.subheader("🌐 HTML 範例頁預覽（靜態展示）")
html_code = """
<main class="container mt-4">
  <section class="mb-4">
    <h2>📈 每月碳排放趨勢</h2>
    <p>（此區為 HTML 原稿示意，非即時圖表）</p>
  </section>
  <section class="row mb-4">
    <div class="col-md-6">
      <h2>🏭 廠區別碳排佔比</h2>
    </div>
    <div class="col-md-6">
      <h2>⚙️ 製程別碳排佔比</h2>
    </div>
  </section>
</main>
"""
components.html(html_code, height=250)

# 📤 匯出按鈕（僅示意）
st.markdown("#### ⬇️ 資料匯出")
col_export1, col_export2 = st.columns(2)
with col_export1:
    st.button("📄 下載報告（PDF）")
with col_export2:
    st.button("📊 匯出 Excel")

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="E-CarbonEmission", layout="wide")

# 頁面標題
st.title("♻️ 金元福碳排放儀表板")
st.markdown("這是一個展示真空成型塑膠包材碳排資訊化的範例系統。")

# ✅ 每月碳排放堆疊長條圖（依ISO 14064-1 類別模擬）
st.subheader("📊 每月碳排放趨勢 ")
stacked_data = pd.DataFrame({
    "月份": ["1月", "1月", "1月", "2月", "2月", "2月", "3月", "3月", "3月"],
    "部門": ["原料", "電力", "上游運輸"] * 3,
    "碳排放量": [15474.602, 3515.320, 142, 12568.338, 2895.11, 113, 14585.895, 3105.22, 152]
})
fig1 = px.bar(stacked_data, x="月份", y="碳排放量(T)", color="類別", title="各類別碳排放堆疊圖", text_auto=True)
st.plotly_chart(fig1, use_container_width=True)

# ✅ 廠區碳排圓餅圖
plant_data = pd.DataFrame({
    "廠區": ["冬山廠", "鶯歌廠", "樹林廠"],
    "碳排放量": [40, 35, 25]
})
fig2 = px.pie(plant_data, names="廠區", values="碳排放量", title="廠區碳排佔比")

# ✅ 製程碳排圓餅圖
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

# ✅ 單位產品碳排強度（三年份對比）
st.subheader("📈 單位產品碳排強度（2023–2025 年比較）")
intensity_data = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月"] * 3,
    "年份": ["2023"] * 5 + ["2024"] * 5 + ["2025"] * 5,
    "碳排強度": [2.6, 2.5, 2.3, 2.4, 2.2, 2.5, 2.3, 2.1, 2.2, 2.0, 2.4, 2.3, 2.1, 2.2, 2.0]
})
fig4 = px.line(intensity_data, x="月份", y="碳排強度", color="年份", markers=True,
               title="單位產品碳排強度比較（kgCO₂e/kg）")
st.plotly_chart(fig4, use_container_width=True)

# ✅ 再生能源使用占比
renewable_data = pd.DataFrame({
    "來源": ["綠電", "灰電"],
    "占比": [35, 65]
})
fig5 = px.pie(renewable_data, names="來源", values="占比", title="再生能源使用比例")
st.subheader("🔋 再生能源使用占比")
st.plotly_chart(fig5, use_container_width=True)

# ✅ 匯出按鈕（示意）
st.markdown("#### ⬇️ 資料匯出")
col_export1, col_export2 = st.columns(2)
with col_export1:
    st.button("📄 下載報告（PDF）")
with col_export2:
    st.button("📊 匯出 Excel")

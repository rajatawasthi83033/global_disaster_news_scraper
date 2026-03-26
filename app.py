import streamlit as st
from scraper import fetch_disaster_news

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Global Disaster News",
    page_icon="🌍",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: bold;
    color: #f97316;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #12E049;
    margin-bottom: 30px;
}
.news-card {
    background: #020617;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 0px 15px rgba(249, 115, 22, 0.25);
}
.source-title {
    font-size: 26px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 15px;
}
.headline {
    color: #008080;
    font-size: 16px;
    margin-bottom: 8px;
}
.footer {
    text-align: center;
    color: #8A2C37;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="main-title">🌍 Global Disaster News Monitor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Press the button below to fetch the latest worldwide disaster and humanitarian crisis news</div>',
    unsafe_allow_html=True
)

# ------------------ BUTTON ------------------
center_col = st.columns(3)[1]
with center_col:
    fetch_btn = st.button("🚨 Get Latest Disaster News", use_container_width=True)

# ------------------ DATA DISPLAY ------------------
if fetch_btn:
    with st.spinner("Collecting live disaster news from trusted sources..."):
        news_data = fetch_disaster_news()

    for source, headlines in news_data.items():
        if headlines:
            st.markdown(f'<div class="source-title">📰 {source}</div>', unsafe_allow_html=True)

            for h in headlines:
                st.markdown(f'<div class="headline">• {h}</div>', unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info(f"No major disaster news found from {source}.")

# ------------------ FOOTER ------------------
st.markdown(
    '<div class="footer">📡 Real-time Disaster News Aggregator </div>',
    
    unsafe_allow_html=True
)

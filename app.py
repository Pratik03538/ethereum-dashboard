# Ethereum Transaction Viewer using Streamlit - Pratik's Advanced Dashboard
# This version includes a personalized intro, more visuals, animations, and a better UI/UX.

import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import time
import plotly.graph_objects as go

# --- Page Configuration ---
st.set_page_config(
    layout="wide",
    page_title="Pratik's Crypto Dashboard",
    initial_sidebar_state="expanded"
)

# --- Language and Text Configuration ---
LANGUAGES = {
    "English": {
        "page_title": "Pratik's Crypto Dashboard",
        "intro_header": "Welcome, Pratik",
        "intro_subheader": "Unlock deep insights into any Ethereum address. Analyze transaction history, track gas fees, and monitor live on-chain activity with this powerful, all-in-one dashboard.",
        "how_to_use_header": "ℹ️ How to Use This App",
        "how_to_use_body": "You need to enter your **Etherscan API Key** and an **Ethereum Wallet Address** in the sidebar, then click 'Fetch Initial Transactions'.",
        "api_steps_button": "How to get an Etherscan API Key?",
        "api_steps_title": "Steps to get an Etherscan API Key:",
        "api_step_1": "**Register on Etherscan:** Go to [https://etherscan.io/register](https://etherscan.io/register) to create a free account.",
        "api_step_2": "**Verify Email:** Verify your email address.",
        "api_step_3": "**Go to API Keys Page:** After logging in, click on 'API Keys' in the menu or go directly to [https://etherscan.io/myapikey](https://etherscan.io/myapikey).",
        "api_step_4": "**Create New Key:** Click the `+ Add` button, give your key a name (e.g., 'MyDashboard'), and click 'Create New API Key'.",
        "api_step_5": "**Copy Key:** Your new API Key is ready. Copy it and paste it into this app.",
        "sidebar_header": "⚙️ Settings",
        "api_key_label": "Etherscan API Key",
        "wallet_address_label": "Wallet Address",
        "fetch_button": "Fetch Initial Transactions",
        "live_feed_label": "Enable Live Feed (refresh every 15s)",
        "dashboard_ready_info": "Dashboard is ready! You can close this sidebar now for a better view.",
        "summary_header": "📈 Account Summary",
        "total_tx": "Total Transactions",
        "eth_received": "Total ETH Received",
        "eth_sent": "Total ETH Sent",
        "analysis_header": "📊 Deeper Analysis",
        "gas_chart_title": "Average Gas Price (Gwei) Over Time",
        "top_senders_title": "Top Senders (to this address)",
        "top_receivers_title": "Top Receivers (from this address)",
        "volume_header": "🗓️ Transaction Volume Over Time",
        "recent_tx_header": "📋 Recent Transactions",
        "fetching_spinner": "Fetching initial transactions for",
        "live_mode_on": "🟢 Live mode is ON.",
        "new_tx_toast": "🔥 New transaction(s) found!",
        "initial_info": "Enter your details in the sidebar and click 'Fetch Initial Transactions' to begin.",
        "warning_inputs": "Please provide both an API Key and a Wallet Address."
    },
    "Hindi": {
        "page_title": "प्रतीक भाई का क्रिप्टो अड्डा",
        "intro_header": "क्या बोलते, प्रतीक भाई",
        "intro_subheader": "कोई भी Ethereum address का पूरा कच्चा-चिट्ठा खोल। देख कितना माल आया, कितना गया, और पूरा ऑन-चेन टंटा इस खतरनाक डैशबोर्ड पे।",
        "how_to_use_header": "ℹ️ ऐप कैसे चलाने का",
        "how_to_use_body": "साइडबार में अपना **Etherscan API Key** और **Wallet का Address** डाल, और 'चल हिसाब निकाल!' पे क्लिक मार।",
        "api_steps_button": "Etherscan API Key किधर मिलेगा?",
        "api_steps_title": "Etherscan API Key बनाने का जुगाड़:",
        "api_step_1": "**Etherscan पे आईडी बना:** [https://etherscan.io/register](https://etherscan.io/register) पे जाके फोकट में आईडी बना।",
        "api_step_2": "**ईमेल चेक कर:** अपना ईमेल कन्फर्म कर।",
        "api_step_3": "**API Keys पेज पे जा:** लॉग इन के बाद, 'API Keys' पे क्लिक मार या सीधा [https://etherscan.io/myapikey](https://etherscan.io/myapikey) पे जा।",
        "api_step_4": "**नया Key बना:** `+ Add` बटन दबा, Key को कुछ नाम दे (जैसे 'MyDashboard'), और 'Create New API Key' पे क्लिक कर।",
        "api_step_5": "**Key कॉपी कर:** तेरा नया API Key रेडी है। कॉपी करके इधर ऐप में चिपका दे।",
        "sidebar_header": "⚙️ सेटिंग",
        "api_key_label": "Etherscan API Key (चाबी)",
        "wallet_address_label": "Wallet का पता",
        "fetch_button": "चल हिसाब निकाल!",
        "live_feed_label": "लाइव फीड चालू कर (हर 15 सेकंड में)",
        "dashboard_ready_info": "डैशबोर्ड रेडी है! अब साइडबार बंद कर सकता है।",
        "summary_header": "📈 खाते का हाल",
        "total_tx": "टोटल लफड़े (लेन-देन)",
        "eth_received": "कितना माल आया (ETH)",
        "eth_sent": "कितना माल गया (ETH)",
        "analysis_header": "📊 गहराई से जाँच पड़ताल",
        "gas_chart_title": "टाइम के साथ गैस का भाव (Gwei)",
        "top_senders_title": "टॉप भेजने वाले (इस पते पर)",
        "top_receivers_title": "टॉप पाने वाले (इस पते से)",
        "volume_header": "🗓️ टाइम के साथ लेन-देन का वॉल्यूम",
        "recent_tx_header": "📋 ताज़ा हिसाब-किताब",
        "fetching_spinner": "का कच्चा-चिट्ठा निकाल रहे हैं...",
        "live_mode_on": "🟢 लाइव मोड चालू है बे!",
        "new_tx_toast": "🔥 नया लफड़ा हुआ!",
        "initial_info": "शुरू करने के लिए साइडबार में डिटेल डाल और 'चल हिसाब निकाल!' पे क्लिक मार।",
        "warning_inputs": "ए भाई, चाबी और पता दोनों डालना पड़ेगा!"
    }
}


# --- Functions ---

@st.cache_data(ttl=30)
def fetch_transactions(api_key, address):
    """Fetches transactions from the Etherscan API."""
    url = (
        f"https://api.etherscan.io/api?module=account&action=txlist&address={address}"
        f"&startblock=0&endblock=99999999&sort=desc&apikey={api_key}"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["status"] == "1":
            return data["result"]
        else:
            st.session_state[
                'api_error_message'] = f"API Error: {data.get('message', 'Unknown error')} - {data.get('result', '')}"
            return None
    except requests.exceptions.RequestException as e:
        st.session_state['api_error_message'] = f"Network Error: Could not connect to Etherscan API. {e}"
        return None


def process_data(transactions, wallet_address):
    """Processes raw transaction data into a clean pandas DataFrame."""
    if not transactions or not isinstance(transactions, list):
        return pd.DataFrame()

    df = pd.DataFrame(transactions)
    required_cols = ['timeStamp', 'hash', 'from', 'to', 'value', 'gasPrice', 'gasUsed']
    for col in required_cols:
        if col not in df.columns:
            return pd.DataFrame()

    for col in ['value', 'gasPrice', 'gasUsed']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    df['value_eth'] = df['value'] / 1e18
    df['gas_price_gwei'] = df['gasPrice'] / 1e9
    df['gas_fee_eth'] = (df['gasPrice'] * df['gasUsed']) / 1e18

    df['date'] = pd.to_datetime(df['timeStamp'], unit='s')
    df['type'] = df.apply(
        lambda row: 'INCOMING' if str(row['to']).lower() == str(wallet_address).lower() else 'OUTGOING', axis=1)
    df['original_hash'] = df['hash']
    return df


def create_gas_chart(df, TEXT):
    """Creates a line chart for average gas price over time."""
    gas_df = df.set_index('date').resample('D')['gas_price_gwei'].mean().reset_index()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=gas_df['date'], y=gas_df['gas_price_gwei'],
        mode='lines+markers',
        name='Avg Gas Price',
        line=dict(color='#D4AF37', width=2)
    ))
    fig.update_layout(
        title_text=TEXT['gas_chart_title'],
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E0E0E0'),
        xaxis=dict(gridcolor='#3A3A3A'),
        yaxis=dict(gridcolor='#3A3A3A')
    )
    return fig


def style_transactions(df):
    """Applies luxury styling to the DataFrame using Pandas Styler."""

    def style_type(val):
        color = '#2E8B57' if val == 'INCOMING' else '#B22222'
        return f'background-color: {color}; color: white; font-weight: bold; border-radius: 5px;'

    def style_value(val):
        return 'font-weight: bold; color: #D4AF37;'

    display_df = df[['date', 'type', 'value_eth', 'from', 'to', 'hash']].copy()
    display_df.rename(columns={'date': 'Date', 'type': 'Type', 'value_eth': 'Value (ETH)', 'from': 'From', 'to': 'To',
                               'hash': 'Hash'}, inplace=True)

    styled_df = display_df.style.applymap(style_type, subset=['Type']) \
        .applymap(style_value, subset=['Value (ETH)']) \
        .format({'Date': '{:%d %b %Y, %H:%M}', 'Value (ETH)': '{:,.6f}'}) \
        .set_properties(**{'text-align': 'left', 'border': '1px solid #3A3A3A'}) \
        .set_table_styles([
        {'selector': 'th',
         'props': [('background-color', '#242424'), ('color', '#D4AF37'), ('text-transform', 'uppercase')]},
        {'selector': 'td', 'props': [('padding', '10px 12px')]},
        {'selector': 'tr:hover td', 'props': [('background-color', '#2C2C2C')]}
    ])
    return styled_df


def load_css():
    """Injects custom CSS for animations and styling."""
    st.markdown("""
        <style>
            @keyframes slideIn {
                0% { transform: translateY(30px); opacity: 0; }
                100% { transform: translateY(0); opacity: 1; }
            }
            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }
            .main .block-container {
                animation: slideIn 0.8s ease-out forwards;
            }
            [data-testid="stSidebar"] {
                animation: slideIn 0.8s ease-out forwards;
            }
            .intro-container {
                text-align: center;
                padding: 1rem 0;
                animation: fadeIn 1.5s ease-out;
            }
        </style>
    """, unsafe_allow_html=True)


# --- Streamlit UI ---

load_css()

# --- Language Selection ---
if 'lang' not in st.session_state:
    st.session_state.lang = 'English'

selected_lang = st.selectbox(
    'Language / भाषा',
    options=['English', 'Hindi'],
    index=0 if st.session_state.lang == 'English' else 1,
    key='lang_selector'
)
st.session_state.lang = selected_lang
TEXT = LANGUAGES[st.session_state.lang]

# --- Animated Bilingual Intro ---
st.markdown(f"<div class='intro-container'><h1>💰 {TEXT['page_title']} 💰</h1></div>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>{TEXT['intro_header']}</h3>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>{TEXT['intro_subheader']}</p>", unsafe_allow_html=True)

st.markdown("---")

with st.expander(TEXT['how_to_use_header'], expanded=False):
    st.markdown(TEXT['how_to_use_body'])
    if 'show_api_steps' not in st.session_state:
        st.session_state.show_api_steps = False
    if st.button(TEXT['api_steps_button']):
        st.session_state.show_api_steps = not st.session_state.show_api_steps
    if st.session_state.show_api_steps:
        st.markdown(f"""
        #### {TEXT['api_steps_title']}
        1.  {TEXT['api_step_1']}
        2.  {TEXT['api_step_2']}
        3.  {TEXT['api_step_3']}
        4.  {TEXT['api_step_4']}
        5.  {TEXT['api_step_5']}
        """)

# --- Sidebar ---
st.sidebar.header(TEXT['sidebar_header'])
api_key = st.sidebar.text_input(TEXT['api_key_label'], type="password", help="Enter your free Etherscan API key.")
wallet_address = st.sidebar.text_input(TEXT['wallet_address_label'], "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")

if st.sidebar.button(TEXT['fetch_button']):
    if not api_key or not wallet_address:
        st.warning(TEXT['warning_inputs'])
    else:
        st.session_state.clear()
        st.session_state.lang = selected_lang  # Preserve language choice
        with st.spinner(f"{TEXT['fetching_spinner']} '{wallet_address[:10]}...'"):
            raw_transactions = fetch_transactions(api_key, wallet_address)
            if raw_transactions:
                st.session_state['df'] = process_data(raw_transactions, wallet_address)
                st.session_state['wallet_address'] = wallet_address
                st.session_state['api_key'] = api_key
                st.session_state['fetch_done'] = True

live_toggle = st.sidebar.toggle(TEXT['live_feed_label'], key="live_mode")

if st.session_state.get('fetch_done'):
    st.sidebar.info(TEXT['dashboard_ready_info'])

# --- Main Page Display ---
if 'df' in st.session_state and not st.session_state.df.empty:
    df = st.session_state.df

    st.header(TEXT['summary_header'])
    incoming_tx = df[df['type'] == 'INCOMING']
    outgoing_tx = df[df['type'] == 'OUTGOING']
    sub_col1, sub_col2, sub_col3 = st.columns(3)
    sub_col1.metric(TEXT['total_tx'], f"{len(df)}")
    sub_col2.metric(TEXT['eth_received'], f"{incoming_tx['value_eth'].sum():,.4f} ETH")
    sub_col3.metric(TEXT['eth_sent'], f"{outgoing_tx['value_eth'].sum():,.4f} ETH")

    st.header(TEXT['analysis_header'])
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_gas_chart(df, TEXT), use_container_width=True)
    with col2:
        st.subheader(TEXT['top_senders_title'])
        top_senders = df[df['type'] == 'INCOMING'].groupby('from')['value_eth'].sum().nlargest(5)
        st.dataframe(top_senders, use_container_width=True)
        st.subheader(TEXT['top_receivers_title'])
        top_receivers = df[df['type'] == 'OUTGOING'].groupby('to')['value_eth'].sum().nlargest(5)
        st.dataframe(top_receivers, use_container_width=True)

    st.header(TEXT['volume_header'])
    chart_data = df.set_index('date').resample('D')['value_eth'].sum().reset_index()
    st.bar_chart(chart_data, x='date', y='value_eth')

    st.header(TEXT['recent_tx_header'])
    table_placeholder = st.empty()
    with table_placeholder.container():
        styled_table = style_transactions(df.head(100))
        st.dataframe(styled_table, use_container_width=True)

elif 'api_error_message' in st.session_state:
    st.error(st.session_state.api_error_message)
elif not st.session_state.get('fetch_done'):
    st.info(TEXT['initial_info'])

# --- Live Refresh Logic ---
if st.session_state.get('live_mode') and 'df' in st.session_state:
    st.sidebar.success(TEXT['live_mode_on'])

    latest_raw_tx = fetch_transactions(st.session_state.api_key, st.session_state.wallet_address)

    if latest_raw_tx:
        latest_df = process_data(latest_raw_tx, st.session_state.wallet_address)

        if not latest_df.empty:
            old_hashes = set(st.session_state.df['original_hash'])
            new_hashes = set(latest_df['original_hash'])

            if not new_hashes.issubset(old_hashes):
                st.toast(TEXT['new_tx_toast'])
                st.session_state.df = latest_df
                time.sleep(2)
                st.rerun()

    time.sleep(15)
    st.rerun()

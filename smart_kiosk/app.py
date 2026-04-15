import streamlit as st
from data import data_manager
from pathlib import Path

st.set_page_config("Smart Kiosk")

st.header("Smark Kiosk")

if "inventory" not in st.session_state:
    st.session_state["inventory"] = data_manager.load_data(Path('smart_kiosk/inventory.json'))

if "orders" not in st.session_state:
    st.session_state["orders"] = data_manager.load_data(Path("smart_kiosk/orders.json"))

with st.sidebar:
    st.markdown("## Smart Kiosk")

tab1, tab2 = st.tabs(['Dashboard', "Add New Order"])

with tab1:
    pass

with tab2: 
    from ui import orders_ui
    orders_ui.add_new_order_render()
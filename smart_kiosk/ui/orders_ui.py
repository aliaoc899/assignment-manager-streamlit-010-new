import streamlit as st
from services import kiosk_services
from data import data_manager
import time
from pathlib import Path

def add_new_order_render():
    inventory = st.session_state["inventory"]
    orders = st.session_state['orders']

    item_names = kiosk_services.find_item_names(inventory)

    item_name = st.selectbox("Item", item_names, key= "select_item")
    quantity = st.text_input("Quantity", key = "quanity_new_order")

    if st.button("Save Order", key= "new_order", use_container_width= True):
        with st.spinner("saving..."):

            item_id = None
            for item in inventory:
                if item["name"] == item_name:
                    item_id = item["item_id"]
                    break

            new_order = kiosk_services.place_order(inventory,str(item_id),int(quantity),orders)
            if new_order:
                data_manager.save_data(Path("smart_kiosk/inventory.json"), inventory)
                data_manager.save_data(Path("smart_kiosk/orders.json"), orders)

                st.success(f"new order with order id: {new_order['order_id']} is recorded.")
                    
                time.sleep(3)
                st.rerun()
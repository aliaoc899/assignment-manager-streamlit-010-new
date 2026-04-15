import uuid
from typing import List, Dict, Optional

def place_order(inventory_items : list, item_id : str, quantity: int, orders: list) -> Optional[Dict]:
    item = find_inventory_item_by_item_id(inventory_items, item_id)
    if item:
        if item['stock'] >= quantity:
            item['stock'] = item["stock"] - quantity #reduce the stock

            total = quantity * item['unit_price']

            # create the new order dict
            new_order = {
                "order_id": str(uuid.uuid4()),
                "item_id": item_id,
                "quantity": quantity,
                "status": "placed",
                "total": total
            }
            #add the new order to the orders
            orders.append(new_order)
            return new_order


def find_item_names(inventory: List) -> List:
    item_names = []
    for item in inventory:
        item_names.append(item['name'])
    return item_names

def find_orders_by_item_id():
    pass

def count_orders_by_item_id():
    pass

def find_inventory_item_by_item_id(invetory_list: list, item_id : str) -> Optional[Dict]:
    for item in invetory_list:
        if item['item_id'] == item_id:
            return item
    
    return None

def update_invetory_item():
    pass

def add_new_item_to_inventory():
    pass

def update_inventory_item():
    pass

def cancel_order():
    pass
import uuid
from typing import List, Dict, Optional

class OrderManagement:
    def __init__(self, inventory_items : List[Dict],orders: List[Dict]) -> None:
        self.invetory_items = inventory_items
        self.orders = orders

    def place_order(self, item_id : str, quantity: int) -> Optional[Dict]:
        item = self.find_inventory_item_by_item_id(item_id)
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
                self.orders.append(new_order)
                return new_order


    def find_item_names(self) -> List:
        item_names = []
        for item in self.invetory_items:
            item_names.append(item['name'])
        return item_names

    def find_orders_by_item_id(self):
        pass

    def count_orders_by_item_id(self):
        pass

    def find_inventory_item_by_item_id(self, item_id : str) -> Optional[Dict]:
        for item in self.invetory_items:
            if item['item_id'] == item_id:
                return item
        
        return None

    def update_invetory_item(self):
        pass

    def add_new_item_to_inventory(self):
        pass

    def update_inventory_item(self):
        pass

    def cancel_order(self):
        pass
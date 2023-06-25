from typing import Dict, List
import threading
import random
from tegro_money import TegroMoneyParser
from tegro_money.tegro_money.tegro_config import TegroConfig


class Tegro(TegroMoneyParser):
    def __init__(self, config: TegroConfig):
        super().__init__(config)
        self.config = config
        self.currencies = ["RUB", "EUR", "USD"]
        self.orders = []

    def get_orders(self):
        self.orders = []
        # TODO: get list of order ids
        return self.orders 
    
    def add_balance(self, email: str, currency: str, sum: float):
        # TODO: get user balance from DB
        balance = 0
        new_balance = balance + sum
        # TODO: here you can save new user balance to DB
        
    def generate_order_id(self):
        order_id = random.randint(1, 999)
        return order_id
    
    def create_order(self, currency: str, payment_system: str, fields: Dict, items: List[Dict]):
        self.get_orders()
        order_id = self.generate_order_id()
        while order_id in self.orders:
            order_id = self.generate_order_id()
        url = super().create_order(currency, order_id, payment_system, fields, items)
        # TODO: here you can add order id to DB
        self.orders.append(order_id)
        return url
    
    def _check_payments(self):
        while True:
            self.get_orders() 
            # TODO: here you can get list of order ids from DB
            orders = self.orders
            data = [self.order_info_by_order_id(order_id) for order_id in orders]
            success_orders = [order for order in data if order["status"] == 1]
            emails = [order["email"] for order in success_orders]
            amounts = [order["amount"] for order in success_orders]
            currencies = [self.currencies[order["currency_id"]] for order in success_orders]
            for email, currency, amount in zip(emails, amounts, currencies):
                self.add_balance(email, currency, amount)

    def check_payments(self):
        threading.Thread(target=self._check_payments).start()

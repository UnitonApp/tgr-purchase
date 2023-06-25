"""
Format:
python ./../../python/integration.py . $currency . $payment_system . $fields . $items
"""

import sys
import json
from .tegro import Tegro
from tegro_money.tegro_money.tegro_config import TegroConfig

with open("../settings.json", encoding = "utf-8") as f:
    data = json.load(f)

config = TegroConfig(**data)
tegro = Tegro(config)

tegro.check_payments()

url = tegro.create_order(
    str(sys.argv[1]),
    str(sys.argv[2]),
    json.loads(sys.argv[3]),
    json.loads(sys.argv[4]),
    )

print(url)
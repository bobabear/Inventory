# Inventory Management & Utilities

A collection of Python functions for:

1. **Inventory management**  
   - `update_inventory` – merge restock items into an existing inventory  
   - `merge_inventory` – convert list‐format inventory to dict and apply updates  
   - `products_info` – build and optionally update an inventory from parallel product lists  
2. **Miscellaneous utilities**  
   - `digits_summation` – recursively sum the digits of an integer  
   - `vowel_counts` – recursively count vowels in a string  

All functions are defined in `achu4_211_PA5.py`. A unittest harness (`tester5.py`) verifies their behavior.

---

## ⚙️ Prerequisites

- Python 3.6+

---

## 📥 Installation

```bash
git clone https://github.com/your-username/Inventory-main.git
cd Inventory-main
```

## How to Use

from achu4_211_PA5 import (<br>
    update_inventory,<br>
    merge_inventory,<br>
    products_info,<br>
    digits_summation,<br>
    vowel_counts<br>
)

## — Inventory functions —

### 1. update_inventory
inv = {<br>
    'Widget': [['red', 'small', 1.5], [10, 'A1']],<br>
}<br>
restock = [<br>
    ['Widget', ['blue'],    [5, 'B2']],       **existing product → tags, quantity & aisle appended**<br>
    ['Gadget', ['green', 2.0], [20, 'C3']],   **new product → added to inventory**<br>
]
updated_inv = update_inventory(inv.copy(), restock)<br>
print(updated_inv)<br>
→ {<br>
    'Widget': [['red', 'small', 'blue', 1.5], [15, 'A1 B2']],<br>
    'Gadget': [['green', 2.0], [20, 'C3']]<br>
}

### 2. merge_inventory
**start from list‐format inventory and a dict of new items**
inv_list = [<br>
    ['Widget', ['yellow'], [3, 'D4']]<br>
]<br>
new_items = {<br>
    'Widget': [['yellow'], [3, 'D4']]<br>
}<br>
merged = merge_inventory(inv_list, new_items)<br>
print(merged)
→ same as update_inventory on dict form

### 3. products_info
products            = ('Apple', 'Banana')<br>
details             = [ [['red'],       [50, 'A2']],<br>
                        [['yellow'],    [75, 'B1']] ]<br>
new_details         = [ [],              [['ripe'], [10, 'B3']] ]<br>
inventory_dict = products_info(products, details, new_products_detail=new_details)<br>
print(inventory_dict)<br>
→ {<br>
    'Apple':  [['red'],       [50, 'A2']],<br>
    'Banana': [['yellow','ripe'], [85, 'B1 B3']]<br>
}

### — Utility functions —

**digits_summation**<br>
print(digits_summation(4729)) → 4+7+2+9 = 22

**vowel_counts**<br>
print(vowel_counts("Hello, World!"))
→ {'e': 1, 'o': 2}

## Run Test Cases
python3 tester5.py achu4_211_PA5.py

from settings import *

class ResourceData:
    def __init__(self) -> None:
        self.data = {}
    
    def contains(self, key):
        if key in self.data:
            return True
        else:
            return False

    def get_quantity(self, key):
        if self.contains(key):
            return self.data[key]
        else:
            return 0

    def get_supply(self, key_res, amount):
        if key_res in self.data:
            self.data[key_res] += amount
            print(f'[RES] Added: {key_res} : {amount} -> {self.data[key_res]}')

        else:
            self.data[key_res] = amount

    def supply(self, target, key_res, amount):
        print("[RES]-> Supliying.")
        target.resource_data.get_supply(key_res, amount)

    def dump_inventory_to_target(self, target):
        for item in self.data:
            target.resource_data.get_supply(item, self.data[item])
            self.data[item] = 0
            print("[RES] -> Dumped inventory.")


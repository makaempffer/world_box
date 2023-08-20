from settings import *

class ResourceData:
    def __init__(self) -> None:
        self.data = {}

    def get_supply(self, key_res, amount):
        if key_res in self.data:
            self.data[key_res] += amount
            print(f'[RES] Added: {key_res} : {amount} -> {self.data[key_res]}')

        else:
            self.data[key_res] = amount

    def supply(self, target, key_res, amount):
        print("[RES] -> Supliying.")
        target.resource_data.get_supply(key_res, amount)

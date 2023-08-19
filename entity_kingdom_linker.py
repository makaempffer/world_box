from settings import *

class EntityKingdomLinker:
    def __init__(self, entity_list, kingdom) -> None:
        self.entity_list = entity_list
        self.kingdom = kingdom
    
    def link_kingdom_to_entity(self):
        for entity in self.entity_list:
            entity.set_kingdom(self.kingdom)
            print("[LINKER] -> Entity-Kingdom group set.")
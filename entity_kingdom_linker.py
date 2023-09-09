from settings import *


class EntityKingdomLinker:
    def __init__(self, entity_list=None, kingdom=None) -> None:
        self.entity_list = entity_list
        self.kingdom = kingdom

    def link_kingdom_to_entity(self):
        for entity in self.entity_list:
            entity.set_kingdom(self.kingdom)
            print("[LINKER] -> Entity-Kingdom link set.")

    def link_kingdom_to_target(self, kingdom, target_list):
        for entity in target_list:
            entity.set_kingdom(kingdom)

    def link_all_entities(self, entities: list, kingdoms: list):
        for i, kingdom in enumerate(kingdoms):
            for entity in entities:
                if entity.batch == i:
                    print(f"[E-LINKER] -> Entity {entity} -> Kingdom {kingdom}")
                    entity.set_kingdom(kingdom)


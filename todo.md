# TODO FUNCTIONALITIES:
1. Add modifiers/"strenght" attributes to entities that change for example: LimitCarry, AttackDamage, PickUpAmount.
2. Add way to add different kingdoms and interaction between entities from other kingdoms.
3. Grant the hability to entities to create their own kingdoms.
4. Add mechanic of conquering; The kingdom will "conquer" neighboring "tiles" as certain stats/attributes are met.
5. Add different levels of relation between kingdoms: Will range from 1~100 and will determine if a kingdom is likely to start a war
6. Add mechanics to increase/decrease levels of relation, as; Materials in close territory, distance to another kingdom, random events.
7. add random events to kingdom
8. Add territory boundaries with draw methods, and detection if entity is not in own territory: do something().
9. Add interest to tiles with resources, if it has many and valuable resources, interests would go up, making the expansion of the kingdom tend to that way.
10. Add tile textures.
11. Add, if certain requirement is met, the kingdom can send it's workers to build x building like a Farm Plot.

# TODO IN PROGRESS:
1. ## Kingdom territory "conquer".
    1. ##### OBSERVATION: Tiles can become conquered?, An imaginary Line gets created.
#### Tile Solution -> Easier to implement, only add self.is_conquered and self.conqueror.


# KNOWN ISSUES: 
1. Min size of the window = 1000, 1000 due to the tile getting functions.

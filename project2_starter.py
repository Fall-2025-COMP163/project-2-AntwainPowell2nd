"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    def __init__(self, name, health, strength, magic): # adding in the atrubutes for the class Character 
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):#creating the attack method for the class Character
        damage = self.strength
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage!")  
        
    def take_damage(self, damage):#creating the take_damage method for the class Character
        self.health -= damage
        if self.health < 0:
            print(f"{self.name} has been defeated!")
            self.health = 0
        else:
            print(f"{self.name} takes {damage} damage, remaining health: {self.health}")
        
    def display_stats(self):#displaying the stats of the class Character
        print(f"Character: {self.name}\nHealth: {self.health}\nStrength: {self.strength}\nMagic: {self.magic}")

class Player(Character):
    def __init__(self, name, character_class, health, strength, magic):#initializing the player class with its attributes includign the ones from the Character class by use of the super() function
        super().__init__(name, health, strength, magic)
        self.character_class = character_class 
        self.level = 1
        self.experience = 0
        
    def display_stats(self):#displaying the stats of the class Player in addition to the ones from the Character class by use of the super() function
        super().display_stats()
        print(f"Class: {self.character_class}\nLevel: {self.level}\nExperience: {self.experience}")

class Warrior(Player):
    def __init__(self, name):#initializing the warrior class with its attributes includign the ones from the Player and Character classes by use of the super() function
        super().__init__(name, "Warrior", 120, 15, 5) 
        
    def attack(self, target):#overriding the attack method for the class Warrior
        damage = self.strength + 5
        target.take_damage(damage)
        print(f"{self.name} performs a strike on {target.name} for {damage} damage!")
        
    def power_strike(self, target):#special ability for the class Warrior
        damage = self.strength + 10
        target.take_damage(damage)
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!")

class Mage(Player):
    def __init__(self, name):#initializing the mage class with its attributes includign the ones from the Player and Character classes by use of the super() function
        super().__init__(name, "Mage", 80, 8, 20)
        
    def attack(self, target):#overriding the attack method for the class Mage
        damage = self.magic
        target.take_damage(damage)
        print(f"{self.name} casts an attack spell on {target.name} for {damage} damage!") 
        
    def fireball(self, target):#special ability for the class Mage
        damage = self.magic + 10
        target.take_damage(damage)
        print(f"{self.name} casts Fireball on {target.name} for {damage} damage!")

class Rogue(Player):
    def __init__(self, name):#initializing the rogue class with its attributes includign the ones from the Player and Character classes by use of the super() function
        super().__init__(name, "Rogue", 90, 12, 10) 
        
    def attack(self, target):#overriding the attack method for the class Rogue
        import random
        is_critical = random.randint(1, 10) <= 3
        if is_critical:
            damage = self.strength * 2  
        else: 
            damage = self.strength 
        target.take_damage(damage)
        if is_critical:
            print(f"{self.name} lands a CRITICAL HIT on {target.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks {target.name} for {damage} damage!")

        
    def sneak_attack(self, target):#special ability for the class Rogue
        damage = self.strength * 2
        target.take_damage(damage)
        print(f"{self.name} performs a Sneak Attack on {target.name} for {damage} damage!")

class Weapon:
    def __init__(self, name, damage_bonus):#initializing the weapon class with its attributes
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):#displaying the info of the class Weapon
        print(f"Weapon: {self.name}, Damage Bonus: {self.damage_bonus}") 

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    for character in [warrior, mage, rogue]:
         print(f"\n{character.name} attacks the dummy:")
         character.attack(dummy_target)
         dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    # 
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    # 
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # TODO: Test the battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")

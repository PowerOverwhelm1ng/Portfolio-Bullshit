import random
import tkinter as tk
from tkinter import messagebox

def roll_ad100():
    return random.randint(1, 100)



def select_item_from_table(table):
    roll = roll_ad100()
    for key in table:
        if "-" in key:
            range_start, range_end = key.split("-")
            if roll >= int(range_start) and roll <= int(range_end):
                return table[key]
        elif roll == int(key):
            return table[key]
    return None

magic_items_table_a = {
    "01-50": "Potion of healing",
    "51-60": "Spell scroll (cantrip)",
    "61-70": "Potion of climbing",
    "71-90": "Spell scroll (1st level)",
    "91-94": "Spell scroll (2nd level)",
    "95-98": "Potion of greater healing",
    "99": "Bag of holding",
    "00": "Driftglobe"
}

magic_items_table_b = {
    "01-15": "Potion of greater healing",
    "16-22": "Potion of fire breath",
    "23-29": "Potion of resistance",
    "30-34": "Ammunition, +1",
    "35-39": "Potion of animal friendship",
    "40-44": "Potion of hill giant strength",
    "45-49": "Potion of growth",
    "50-54": "Potion of water breathing",
    "55-59": "Spell scroll (2nd level)",
    "60-64": "Spell scroll (3rd level)",
    "65-67": "Bag of holding",
    "68-70": "Keoghtom's ointment",
    "71-73": "Oil of slipperiness",
    "74-75": "Dust of disappearance",
    "76-77": "Dust of dryness",
    "78-79": "Dust of sneezing and choking",
    "80-81": "Elemental gem",
    "82-83": "Philter of love",
    "84": "Alchemy jug",
    "85": "Cap of water breathing",
    "86": "Cloak of the manta ray",
    "87": "Driftglobe",
    "88": "Goggles of night",
    "89": "Helm of comprehending languages",
    "90": "Immovable rod",
    "91": "Lantern of revealing",
    "92": "Mariner's armor",
    "93": "Mithral armor",
    "94": "Potion of poison",
    "95": "Ring of swimming",
    "96": "Robe of useful items",
    "97": "Rope of climbing",
    "98": "Saddle of the cavalier",
    "99": "Wand of magic detection",
    "100": "Wand of secrets"
}

magic_items_table_c = {
    "01-15": "Potion of superior healing",
    "16-22": "Spell scroll (4th level)",
    "23-27": "Ammunition, +2",
    "28-32": "Potion of clairvoyance",
    "33-37": "Potion of diminution",
    "38-42": "Potion of gaseous form",
    "43-47": "Potion of frost giant strength",
    "48-52": "Potion of stone giant strength",
    "53-57": "Potion of heroism",
    "58-62": "Potion of invulnerability",
    "63-67": "Potion of mind reading",
    "68-72": "Spell scroll (5th level)",
    "73-75": "Elixir of health",
    "76-78": "Oil of etherealness",
    "79-81": "Potion of fire giant strength",
    "82-84": "Quaal's feather token",
    "85-87": "Scroll of protection",
    "88-89": "Bag of beans",
    "90-91": "Bead of force",
    "92": "Chime of opening",
    "93": "Decanter of endless water",
    "94": "Eyes of minute seeing",
    "95": "Folding boat",
    "96": "Heward's handy haversack",
    "97": "Horseshoes of speed",
    "98": "Necklace of fireballs",
    "99": "Periapt of health",
    "100": "Sending Stones"
}

magic_items_table_d = {
    "01-20": "Potion of supreme healing",
    "21-30": "Potion of invisibility",
    "31-40": "Potion of speed",
    "41-50": "Spell scroll (6th level)",
    "51-57": "Spell scroll (7th level)",
    "58-62": "Ammunition, +3",
    "63-67": "Oil of sharpness",
    "68-72": "Potion of flying",
    "73-77": "Potion of cloud giant strength",
    "78-82": "Potion of longevity",
    "83-87": "Potion of vitality",
    "88-92": "Spell scroll (8th level)",
    "93-95": "Horseshoes of a zephyr",
    "96-98": "Nolzur's marvelous pigments",
    "99": "Bag of devouring",
    "100": "Portable hole"
}

magic_items_table_e = {
    "01-30": "Spell scroll (8th level)",
    "31-55": "Potion of storm giant strength",
    "56-70": "Potion of supreme healing",
    "71-85": "Spell scroll (9th level)",
    "86-93": "Universal solvent",
    "94-98": "Arrow of slaying",
    "99-100": "Sovereign glue"
}

magic_items_table_f = {
    "01-15": "Weapon, +1",
    "16-18": "Shield, +1",
    "19-21": "Sentinel shield",
    "22-23": "Amulet of proof against detection and location",
    "24-25": "Boots of elvenkind",
    "26-27": "Boots of striding and springing",
    "28-29": "Bracers of archery",
    "30-31": "Brooch of shielding",
    "32-33": "Broom of flying",
    "34-35": "Cloak of elvenkind",
    "36-37": "Cloak of protection",
    "38-39": "Gauntlets of ogre power",
    "40-41": "Hat of disguise",
    "42-43": "Javelin of lightning",
    "44-45": "Pearl of power",
    "46-47": "Rod of the pact keeper, +1",
    "48-49": "Slippers of spider climbing",
    "50-51": "Staff of the adder",
    "52-53": "Staff of the python",
    "54-55": "Sword of vengeance",
    "56-57": "Trident of fish command",
    "58-59": "Wand of magic missiles",
    "60-61": "Wand of the war mage, +1",
    "62-63": "Wand of web",
    "64-65": "Weapon of warning",
    "66": "Adamantine armor (chain mail)",
    "67": "Adamantine armor (chain shirt)",
    "68": "Adamantine armor (scale mail)",
    "69": "Bag of tricks (gray)",
    "70": "Bag of tricks (rust)",
    "71": "Bag of tricks (tan)",
    "72": "Boots of the winterlands",
    "73": "Circlet of blasting",
    "74": "Deck of illusions",
    "75": "Eversmoking bottle",
    "76": "Eyes of charming",
    "77": "Eyes of the eagle",
    "78": "Figurine of wondrous power (silver raven)",
    "79": "Gem of brightness",
    "80": "Gloves of missile snaring",
    "81": "Gloves of swimming and climbing",
    "82": "Gloves of thievery",
    "83": "Headband of intellect",
    "84": "Helm of telepathy",
    "85": "Instrument of the bards (Doss lute)",
    "86": "Instrument of the bards (Fochlucan bandore)",
    "87": "Instrument of the bards (Mac-Fuimidh cittern)",
    "88": "Medallion of thoughts",
    "89": "Necklace of adaptation",
    "90": "Periapt of wound closure",
    "91": "Pipes of haunting",
    "92": "Pipes of the sewers",
    "93": "Ring of jumping",
    "94": "Ring of mind shielding",
    "95": "Ring of warmth",
    "96": "Ring of water walking",
    "97": "Quiver of Ehlonna",
    "98": "Stone of good luck",
    "99": "Wind fan",
    "100": "Winged boots"
}

magic_items_table_g = {
    "01-11": "Weapon, +2",
    "12-14": "Figurine of wondrous power (Bronze griffon, Ebony fly, Golden lions, Ivory goats, Marble elephant, Onyx dog, Serpentine owl)",
    "15": "Adamantine armor (breastplate)",
    "16": "Adamantine armor (splint)",
    "17": "Amulet of health",
    "18": "Armor of vulnerability",
    "19": "Arrow-catching shield",
    "20": "Belt of dwarvenkind",
    "21": "Belt of hill giant strength",
    "22": "Berserker axe",
    "23": "Boots of levitation",
    "24": "Boots of speed",
    "25": "Bowl of commanding water elementals",
    "26": "Bracers of defense",
    "27": "Brazier of commanding fire elementals",
    "28": "Cape of the mountebank",
    "29": "Censer of controlling air elementals",
    "30": "Armor, +1 chain mail",
    "31": "Armor of resistance (chain mail)",
    "32": "Armor of resistance (chain shirt)",
    "33": "Armor, +1 chain shirt",
    "34": "Cloak of displacement",
    "35": "Cloak of the bat",
    "36": "Cube of force",
    "37": "Daern's instant fortress",
    "38": "Dagger of venom",
    "39": "Dimensional shackles",
    "40": "Dragon slayer",
    "41": "Elven chain",
    "42": "Flame tongue",
    "43": "Gem of seeing",
    "44": "Giant slayer",
    "45": "Clamoured studded leather",
    "46": "Helm of teleportation",
    "47": "Horn of blasting",
    "48": "Horn of Valhalla (silver or brass)",
    "49": "Instrument of the bards (Canaithmandolin)",
    "50": "Instrument of the bards (Cii lyre)",
    "51": "loun stone (awareness)",
    "52": "loun stone (protection)",
    "53": "loun stone (reserve)",
    "54": "loun stone (sustenance)",
    "55": "Iron bands of Bilarro",
    "56": "Armor, +1 leather",
    "57": "Armor of resistance (leather)",
    "58": "Mace of disruption",
    "59": "Mace of smiting",
    "60": "Mace of terror",
    "61": "Mantle of spell resistance",
    "62": "Necklace of prayer beads",
    "63": "Periapt of proof against poison",
    "64": "Ring of animal influence",
    "65": "Ring of evasion",
    "66": "Ring of feather falling",
    "67": "Ring of free action",
    "68": "Ring of protection",
    "69": "Ring of resistance",
    "70": "Ring of spell storing",
    "71": "Ring of the ram",
    "72": "Ring of X-ray vision",
    "73": "Robe of eyes",
    "74": "Rod of rulership",
    "75": "Rod of the pact keeper, +2",
    "76": "Rope of entanglement",
    "77": "Armor, +1 scale mail",
    "78": "Armor of resistance (scale mail)",
    "79": "Shield, +2",
    "80": "Shield of missile attraction",
    "81": "Staff of charming",
    "82": "Staff of healing",
    "83": "Staff of swarming insects",
    "84": "Staff of the woodlands",
    "85": "Staff of withering",
    "86": "Stone of controlling earth elementals",
    "87": "Sun blade",
    "88": "Sword of life stealing",
    "89": "Sword of wounding",
    "90": "Tentacle rod",
    "91": "Vicious weapon",
    "92": "Wand of binding",
    "93": "Wand of enemy detection",
    "94": "Wand of fear",
    "95": "Wand of fireballs",
    "96": "Wand of lightning bolts",
    "97": "Wand of paralysis",
    "98": "Wand of the war mage, +2",
    "99": "Wand of wonder",
    "100": "Wings of flying"
}

magic_items_table_h = {
    "01-10": "Weapon, +3",
    "11-12": "Amulet of the planes",
    "13-14": "Carpet of flying",
    "15-16": "Crystal ball (very rare version)",
    "17-18": "Ring of regeneration",
    "19-20": "Ring of shooting stars",
    "21-22": "Ring of telekinesis",
    "23-24": "Robe of scintillating colors",
    "25-26": "Robe of stars",
    "27-28": "Rod of absorption",
    "29-30": "Rod of alertness",
    "31-32": "Rod of security",
    "33-34": "Rod of the pact keeper, +3",
    "35-36": "Scimitar of speed",
    "37-38": "Shield, +3",
    "39-40": "Staff of fire",
    "41-42": "Staff of frost",
    "43-44": "Staff of power",
    "45-46": "Staff of striking",
    "47-48": "Staff of thunder and lightning",
    "49-50": "Sword of sharpness",
    "51-52": "Wand of polymorph",
    "53-54": "Wand of the war mage, +3",
    "55": "Adamantine armor (half plate)",
    "56": "Adamantine armor (plate)",
    "57": "Animated shield",
    "58": "Belt of fire giant strength",
    "59": "Belt of frost (or stone) giant strength",
    "60": "Armor, +1 breastplate",
    "61": "Armor of resistance (breastplate)",
    "62": "Candle of invocation",
    "63": "Armor, +2 chain mail",
    "64": "Armor, +2 chain shirt",
    "65": "Cloak of arachnida",
    "66": "Dancing sword",
    "67": "Demon armor",
    "68": "Dragon scale mail",
    "69": "Dwarven plate",
    "70": "Dwarven thrower",
    "71": "Efreeti bottle",
    "72": "Figurine of wondrous power (obsidian steed)",
    "73": "Frost brand",
    "74": "Helm of brilliance",
    "75": "Horn of Valhalla (bronze)",
    "76": "Instrument of the bards (Anstruthharp)",
    "77": "Ioun stone (absorption)",
    "78": "Ioun stone (agility)",
    "79": "Ioun stone (fortitude)",
    "80": "Ioun stone (insight)",
    "81": "Ioun stone (intellect)",
    "82": "Ioun stone (leadership)",
    "83": "Ioun stone (strength)",
    "84": "Armor, +2 leather",
    "85": "Manual of bodily health",
    "86": "Manual of gainful exercise",
    "87": "Manual of golems",
    "88": "Manual of quickness of action",
    "89": "Mirror of life trapping",
    "90": "Nine lives stealer",
    "91": "Oathbow",
    "92": "Armor, +2 scale mail",
    "93": "Spellguard shield",
    "94": "Armor, +1 splint",
    "95": "Armor of resistance (splint)",
    "96": "Armor, +1 studded leather",
    "97": "Armor of resistance (studded leather)",
    "98": "Tome of clear thought",
    "99": "Tome of leadership and influence",
    "100": "Tome of understanding"
}

magic_items_table_i = {
    "01-05": "Defender",
    "06-10": "Hammer of thunderbolts",
    "11-15": "Luck Blade",
    "16-20": "Sword of answering",
    "21-23": "Holy avenger",
    "24-26": "Ring of djinni summoning",
    "27-29": "Ring of invisibility",
    "30-32": "Ring of spell turning",
    "36-38": "Rod of lordly might",
    "39-41": "Vorpal sword",
    "42-43": "Belt of cloud giant strength",
    "44-45": "Armor, +2 breastplate",
    "46-47": "Armor, +3 chain mail",
    "48-49": "Armor, +3 chain shirt",
    "50-51": "Cloak of invisibility",
    "52-53": "Crystal ball (legendary version)",
    "54-55": "Armor, +1 half plate",
    "56-57": "Iron flask",
    "58-59": "Armor, +3 leather",
    "60-61": "Armor, +1 plate",
    "62-63": "Robe of the archmagi",
    "64-65": "Rod of resurrection",
    "66-67": "Armor, +1 scale mail",
    "68-69": "Scarab of protection",
    "70-71": "Armor, +2 splint",
    "72-73": "Armor, +2 studded leather",
    "74-75": "Well of many worlds",
    "76": "Magic armor (roll d12)",
    "77": "Apparatus of Kwalish",
    "78": "Armor of invulnerability",
    "79": "Belt of storm giant strength",
    "80": "Cubic gate",
    "81": "Deck of many things",
    "82": "Efreeti chain",
    "83": "Armor of resistance (half plate)",
    "84": "Horn of Valhalla (iron)",
    "85": "Instrument of the bards (OIIamh harp)",
    "86": "Ioun stone (greater absorption)",
    "87": "Ioun stone (mastery)",
    "88": "Ioun stone (regeneration)",
    "89": "Plate armor of etherealness",
    "90": "Plate armor of resistance",
    "91": "Ring of air elemental command",
    "92": "Ring of earth elemental command",
    "93": "Ring of fire elemental command",
    "94": "Ring of three wishes",
    "95": "Ring of water elemental command",
    "96": "Sphere of annihilation",
    "97": "Talisman of pure good",
    "98": "Talisman of the sphere",
    "99": "Talisman of ultimate evil",
    "100": "Tome of the stilled tongue"
}

item_a = select_item_from_table(magic_items_table_a)
item_b = select_item_from_table(magic_items_table_b)
item_c = select_item_from_table(magic_items_table_c)
item_d = select_item_from_table(magic_items_table_d)
item_e = select_item_from_table(magic_items_table_e)
item_f = select_item_from_table(magic_items_table_f)
item_g = select_item_from_table(magic_items_table_g)
item_h = select_item_from_table(magic_items_table_h)
item_i = select_item_from_table(magic_items_table_i)

def generate_magic_item():
    item_a = select_item_from_table(magic_items_table_a)
    item_b = select_item_from_table(magic_items_table_b)
    # Generate items from other tables as needed
    messagebox.showinfo("Generated Magic Items", 
                        f"Table A: {item_a}\n"
                        f"Table B: {item_b}\n"
                        f"Table C: {item_c}\n"
                        f"Table D: {item_d}\n"
                        f"Table E: {item_e}\n"
                        f"Table F: {item_f}\n"
                        f"Table G: {item_g}\n"
                        f"Table H: {item_h}\n"
                        f"Table I: {item_i}")

    # Create the GUI window

window = tk.Tk()
window.title("Magic Item Generator")
window.geometry("300x200")

# Create the UI components

label = tk.Label(window, text="Click the button to generate magic items:")
label.pack(pady=20)

generate_button = tk.Button(window, text="Generate", command=generate_magic_item)
generate_button.pack()

# Start the GUI event loop

window.mainloop()
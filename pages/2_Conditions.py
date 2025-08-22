import streamlit as st

class Toc:

    def __init__(self):
        self._items = []
        self._placeholder = None
    
    def title(self, text):
        self._markdown(text, "h1")

    def header(self, text):
        self._markdown(text, "h2", " " * 2)

    def subheader(self, text):
        self._markdown(text, "h3", " " * 4)

    def placeholder(self, sidebar=False):
        self._placeholder = st.sidebar.empty() if sidebar else st.empty()

    def generate(self):
        if self._placeholder:
            self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)
    
    def _markdown(self, text, level, space=""):
        key = "".join(filter(str.isalnum, text)).lower()

        st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
        self._items.append(f"{space}* <a href='#{key}'>{text}</a>")


toc = Toc()

st.title("Conditions")
toc.placeholder(sidebar=True)

toc.title("Conditions")

st.markdown('''Conditions are effects that can be applied to creatures through a variety of means and typically negatively affect the target creature.

## Condition Immunity
When you have Immunity to a condition, you completely ignore its effects.

## Conditions List''')

toc.header("Bleeding")
st.markdown('''
### Bleeding
- You take 1 True Damage at the start of each of your turns.
- Ending Bleeding:
	- Healed: If you heal damage from an effect such as a spell or potion, the Bleeding condition ends.
	- Medicine Check: A creature can spend 2 AP to make a DC 10 Medicine Check on itself or another creature within 1 space. On a success, the Bleeding condition ends on the target creature.
''')

toc.header("Blinded")
st.markdown('''
### Blinded
- You automatically fail Checks that require Sight.
- All other creatures are considered Unseen to you.
- You are Exposed (Attacks against you have ADV).
- You are Hindered (You have DIS on Attacks).
- If you are not guided by another creature, all terrain is considered Difficult Terrain (moving 1 Space costs 2 Spaces).
''')

toc.header("Burning")
st.markdown('''
### Burning
- You take 1 Fire Damage at the start of each of your turns.
- You or another creature within 1 Space can spend 2 AP to put out the flames. To put out the flames on yourself, you must go Prone.
''')

toc.header("Charmed")
st.markdown('''
### Charmed
- Your Charmer has ADV on Charisma Checks made against you.
- You cannot target your Charmer with harmful Attacks, Abilities, or Magic Effects.
''')

toc.header("Dazed")
st.markdown('''
### Dazed
- You have DIS on Mental Checks.
#### Heavily Dazed
- In addition to the effects of Dazed, you also have DIS on Mental Saves.
''')

toc.header("Deafened")
st.markdown('''
### Deafened
- You automatically fail Checks that require Hearing.
- All creatures are considered Unheard by you.
- You have Resistance against Sonic damage (You take half damage from Sonic damage)
''')

toc.header("Exhaustion X")
st.markdown('''
### Exhaustion X
- You gain a penalty equal to X on all Checks and Saves you make. 
- Your Speed and Save DC is reduced by X.
- If a creature ever reaches Exhaustion 6, they immediately die.
''')

toc.header("Exposed")
st.markdown('''
### Exposed
- Attacks against you have ADV.
''')

toc.header("Frightened")
st.markdown('''
### Frightened
- You must spend your turns attempting to move as far away as possible from the source of the effect.
- The only Actions you can take are:
	- Move Action, but you cannot willingly move closer to the source of the effect. 
	- Dodge Action, if you are unable to move or have nowhere farther to go
- You are Intimidated (You have DIS on all Checks while the source is within your line of sight).
''')

toc.header("Grappled")
st.markdown('''
### Grappled
- Your Speed becomes 0.
- You have DIS on Agility Saves.

#### Ending a Grapple
- Escape Grapple: You can spend 1 AP to attempt to break free. Make a Martial Check contested by the Grappler's Athletics Check.
	- Success: The Grapple immediately ends.
- Incapacitated Grappler: If the Grappler becomes Incapacitated, the Grapple immediately ends.
- Forced Movement:
	- If an effect attempts to forcibly move you beyond the Grappler's reach, the Grappler makes the Check or Save instead of you.
	- If the effect targets both you and the Grappler, the Grappler makes 1 Check or Save for both of you.
	- Success: Neither of you are moved.
	- Failure: The Grapple ends, and the effect moves both of you as intended.
- Falling:
	- If you begin Falling while Grappled, and the Grappler is not falling with you, they hold you in place if they can carry your weight.
''')

toc.header("Hindered")
st.markdown('''
### Hindered
- You have DIS on Attacks.
''')

toc.header("Impaired")
st.markdown('''
### Impaired
- You have DIS on Physical Checks.

#### Heavily Impaired
- In addition to the effects of Impaired, you also have DIS on Physical Saves.
''')

toc.header("Incapacitated")
st.markdown('''
### Incapacitated
- You cannot Speak, Concentrate, or spend Action Points.
''')

toc.header("Intimidated")
st.markdown('''
### Intimidated
- You have DIS on all Checks while the source of your intimidation is within your line of sight.
''')

toc.header("Invisible")
st.markdown('''
### Invisible
- You are Unseen.
- Creatures that cannot see you are Exposed (your Attacks against them have ADV).
- Creatures that cannot see you are Hindered (they have DIS on Attacks against you).
''')

toc.header("Paralyzed")
st.markdown('''
### Paralyzed
- Attacks made from within 1 Space that hit you are Critical Hits.
- You are Stunned 4 (automatically fail Agility, Might, and Physical Saves)
- You are Exposed
- You are Incapacitated (you can't Speak, Concentrate, or spend Action Points).
''')

toc.header("Petrified")
st.markdown('''
### Petrified
- You and your mundane belongings turn to stone, and you are no longer aware of your surroundings.
- Your weight increases 10 times.
- You have Resistance to all damage.
- Any Poisons or Diseases affecting you are suspended, and you are immune to additional Poison or Disease while Petrified.
- You are also:
	- Paralyzed 
	- Stunned
	- Exposed
	- Incapacitated
''')

toc.header("Poisoned")
st.markdown('''
### Poisoned
- You are Impaired
- You take 1 Poison Damage at the start of each of your turns.
''')

toc.header("Prone")
st.markdown('''
### Prone
While Prone, you are subjected to the following effects:
- You are Hindered.
- Ranged Attacks against you are Hindered.
- You are Exposed
#### Crawling
- Your only movement option is to Crawl, which counts as Slowed.
#### Standing Up
- You can spend 2 Spaces of movement to stand up, ending the Prone condition.
- Standing up from Prone provokes Opportunity Attacks.
''')

toc.header("Restrained")
st.markdown('''
### Restrained
- You are Hindered.
- You are Exposed.
- You are Grappled.
''')

toc.header("Slowed X")
st.markdown('''
### Slowed X
- Every 1 Space you move costs an extra 1 Space of movement for every X of Slowed
	- Ex. Slowed 2: If your move is 30, you could move 7 spaces
''')

toc.header("Stunned X")
st.markdown('''
### Stunned X
- Your current and maximum AP is reduced by X.
- If you become Stunned 4, you're also Exposed, Incapacitated, and automatically fail Physical Saves.
''')

toc.header("Surprised")
st.markdown('''
### Surprised
- You cannot spend Action Points.
- You are Exposed.
''')

toc.header("Taunted")
st.markdown('''
### Taunted
- You have DIS on Attacks against creatures other than the one that Taunted you.
''')

toc.header("Unconscious")
st.markdown('''
### Unconscious
- You are no longer aware of your surroundings.
- You drop whatever you are holding.
- You fall Prone.
- You are also:
	- Paralyzed.
	- Stunned.
	- Exposed.
	- Incapacitated.
''')

toc.header("Condition Stacking")
st.markdown('''
## Condition Stacking
Certain Conditions can stack multiple times, increasing their effects on the target.
### Condition X Values
Some Conditions have an X value, applying a bonus or penalty equal to the X value. If multiple unique effects impose the same Condition X, their values are added together.

### Stacking Conditions
Some Conditions can be applied multiple times, with their effects stacking.

#### Exposed
- Each instance increases the ADV on Attacks against the target.

#### Hindered, Impaired, & Dazed
- Each instance increases the DIS on relevant rolls.

#### Slowed
- Each instance of Slowed effectively halves your current Movement.

### Overlapping Conditions
Some Conditions do not stack, but multiple sources can still impose their effects.

#### Charmed
- A creature can be Charmed by multiple creatures, granting each one ADV on Charisma Checks against the target.
- The effect does not stack from the same source.

#### Frightened
- A creature can be Frightened by multiple sources.
- If surrounded by multiple sources of fear, they cannot move and may only take the Dodge Action.

#### Grappled
- A creature can be Grappled by multiple creatures.
- The target remains Grappled until freed from all sources.

#### Moving a Grappled Target
- If multiple creatures are Grappling the same target, one attempting to move the target must succeed on a Contested Athletics Check against all other Grapplers.
	- Success: The Grapple ends for all except the moving creature.
	- Failure: The target remains Grappled.

#### Intimidated
- A creature can be Intimidated by multiple creatures.
- The effect does not stack, and the target suffers only DIS 1 on Checks.

#### Restrained
- A creature can be Restrained by multiple sources.
- The target remains Restrained until freed from all sources.

### Exclusive Conditions

#### Taunted
- A creature can only be Taunted by one creature at a time.
- If another creature Taunts the target, the previous Taunt ends.

### Non-Stacking Conditions
The following Conditions do not stack.
- Burning
- Bleeding
- Poisoned
- Deafened
- Blinded
- Invisible
- Prone
- Incapacitated
- Stunned
- Paralyzed
- Unconscious
- Petrified
- Surprised

If a creature is already affected by one of these Conditions and is subjected to it again, the new effect replaces the old one if its duration is longer.
''')

toc.generate()
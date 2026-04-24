import sys, json, re, os

print("Starting generation of 5 completely new unique quizzes (6 to 10)...")

# Base template from question.html
with open(r'f:\Python Project\kids questions\question.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Part 1 Subjects/Verbs
p1_subjs_pl = ["The lions", "The teachers", "The computers", "The airplanes", "The fast trains", "The little mice", "The purple butterflies", "The loud drums", "The bright lights", "The running horses", "The jumping frogs", "The yellow cars", "The fluffy clouds", "The tall trees", "The silly monkeys"]
p1_verbs_pl = ["roar", "teach", "beep", "fly", "speed", "squeak", "flutter", "bang", "glow", "gallop", "leap", "honk", "float", "sway", "swing"]
p1_subjs_sg = ["The lion", "The teacher", "The computer", "The airplane", "The fast train", "The little mouse", "The purple butterfly", "The loud drum", "The bright light", "The running horse", "The jumping frog", "The yellow car", "The fluffy cloud", "The tall tree", "The silly monkey"]
p1_verbs_sg = ["roars", "teaches", "beeps", "flies", "speeds", "squeaks", "flutters", "bangs", "glows", "gallops", "leaps", "honks", "floats", "sways", "swings"]

def gen_p1(i):
    base_idx = i * 3
    q = []
    q.append({"q": f"{p1_subjs_pl[base_idx]} {p1_verbs_pl[base_idx]} loudly.", "correct": "Correct"})
    q.append({"q": f"{p1_subjs_sg[base_idx+1]} {p1_verbs_sg[base_idx+1]} today.", "correct": "Correct"})
    q.append({"q": f"{p1_subjs_pl[base_idx+2]} {p1_verbs_pl[base_idx+2]} nicely.", "correct": "Correct"})
    q.append({"q": f"{p1_subjs_pl[base_idx]} {p1_verbs_sg[base_idx]} loudly.", "correct": "Not Correct"})
    q.append({"q": f"{p1_subjs_sg[base_idx+1]} {p1_verbs_pl[base_idx+1]} today.", "correct": "Not Correct"})
    q.append({"q": f"{p1_subjs_pl[base_idx+2]} {p1_verbs_sg[base_idx+2]} nicely.", "correct": "Not Correct"})
    import random
    random.seed(i)
    random.shuffle(q)
    return q

# Part 2 Formal/Informal 
formals = [
    "I would appreciate your guidance.", "Please contact me later.", "I am writing to inform you.", 
    "It is a pleasure to meet you.", "We apologize for the delay.", "I am delighted to accept.", 
    "Please keep off the grass.", "Kindly return the document.", "I have no inclination to do that.", 
    "That is highly satisfactory.", "I eagerly await your reply.", "You are cordially invited.", 
    "It is of utmost importance.", "I require some assistance.", "We must depart immediately."
]
informals = [
    "Help me out.", "Hit me up later.", "Just letting you know.", 
    "Nice to meet ya.", "Sorry we're late.", "I'd love to go.", 
    "Don't walk on the grass.", "Give it back.", "I don't wanna do that.", 
    "That's super cool.", "Can't wait to hear back.", "Come to my party.", 
    "It's a big deal.", "Need a hand here.", "We gotta go right now."
]
def gen_p2(i):
    base_idx = i * 3
    q = []
    for j in range(3):
        q.append({"q": formals[base_idx+j], "type": "Formal"})
        q.append({"q": informals[base_idx+j], "type": "Informal"})
    import random
    random.shuffle(q)
    return q

# Part 3 Prefix/Suffix 
p3_data = [
    {"q": "What does non- mean in nonfiction?", "opts": ["not", "again", "before"], "ans": "not"},
    {"q": "A powerful person is:", "opts": ["full of power", "without power", "before power"], "ans": "full of power"},
    {"q": "What is the root in 'restart'?", "opts": ["start", "rest", "art"], "ans": "start"}, 
    {"q": "What does anti- mean in antifreeze?", "opts": ["against", "before", "again"], "ans": "against"},
    {"q": "What prefix do you add to 'cover' to mean 'find'?", "opts": ["un-", "re-", "mis-"], "ans": "un-"},
    {"q": "An 'endless' road: ", "opts": ["has no end", "has many ends", "ends again"], "ans": "has no end"},
    {"q": "What does mis- mean in mistake?", "opts": ["wrong", "again", "before"], "ans": "wrong"},
    {"q": "A harmless spider is:", "opts": ["without harm", "full of harm", "harmful again"], "ans": "without harm"},
    {"q": "What is the root in 'disappear'?", "opts": ["appear", "dis", "pear"], "ans": "appear"},
    {"q": "What does pre- mean in preheat?", "opts": ["before", "after", "again"], "ans": "before"},
    {"q": "What prefix do you add to 'turn' to mean 'bring back'?", "opts": ["re-", "un-", "pre-"], "ans": "re-"},
    {"q": "A 'joyful' child is:", "opts": ["full of joy", "without joy", "joyful again"], "ans": "full of joy"},
    {"q": "What does re- mean in revisit?", "opts": ["visit again", "visit before", "not visit"], "ans": "visit again"},
    {"q": "A fearless hero is:", "opts": ["without fear", "full of fear", "fearing again"], "ans": "without fear"},
    {"q": "What is the root in 'unlucky'?", "opts": ["lucky", "un", "uck"], "ans": "lucky"},
    {"q": "What does sub- mean in submarine?", "opts": ["under", "over", "again"], "ans": "under"},
    {"q": "What prefix makes 'kind' mean 'not kind'?", "opts": ["un-", "re-", "pre-"], "ans": "un-"},
    {"q": "A 'colorful' bird is:", "opts": ["full of color", "without color", "coloring again"], "ans": "full of color"},
    {"q": "What does over- mean in oversleep?", "opts": ["too much", "not enough", "again"], "ans": "too much"},
    {"q": "A speechless person is:", "opts": ["unable to speak", "speaking a lot", "speaking again"], "ans": "unable to speak"},
    {"q": "What is the root in 'misplace'?", "opts": ["place", "mis", "lace"], "ans": "place"},
    {"q": "What does mid- mean in midnight?", "opts": ["middle", "end", "beginning"], "ans": "middle"},
    {"q": "What suffix makes 'hope' mean 'full of hope'?", "opts": ["-ful", "-less", "-ed"], "ans": "-ful"},
    {"q": "An 'unfriendly' dog is:", "opts": ["not friendly", "very friendly", "friendly again"], "ans": "not friendly"},
    {"q": "What does under- mean in underwater?", "opts": ["below", "above", "again"], "ans": "below"},
    {"q": "A thankful person is:", "opts": ["full of thanks", "without thanks", "thanking again"], "ans": "full of thanks"},
    {"q": "What is the root in 'dislike'?", "opts": ["like", "dis", "ik"], "ans": "like"},
    {"q": "What does trans- mean in transport?", "opts": ["across", "under", "before"], "ans": "across"},
    {"q": "What suffix makes 'home' mean 'without a home'?", "opts": ["-less", "-ful", "-ed"], "ans": "-less"},
    {"q": "A 'recycle' bin is for:", "opts": ["cycling again", "never cycling", "cycling before"], "ans": "cycling again"}
]
def gen_p3(i):
    return p3_data[i*6:(i+1)*6]

# Part 4 Story Sequencing
p4_stories = [
    [
        "____, we packed our tent for camping.",
        "____, we hiked up the steep mountain track.",
        "____, we found a flat spot for our camp.",
        "____, we pitched the tent together.",
        "____, we roasted marshmallows on the fire.",
        "____, we slept under the brilliant stars."
    ],
    [
        "____, I picked up a blank piece of paper.",
        "____, I grabbed my favorite pencil.",
        "____, I drew the outline of a big house.",
        "____, I colored the roof bright red.",
        "____, I added some green grass and trees.",
        "____, I hung the drawing on the fridge."
    ],
    [
        "____, we got the soap and a sponge.",
        "____, we sprayed the car with the hose.",
        "____, we scrubbed the dirt off the doors.",
        "____, we rinsed the soap away with water.",
        "____, we dried the car with a soft towel.",
        "____, the car looked shiny and brand new!"
    ],
    [
        "____, I walked into the big library.",
        "____, I looked through the adventure section.",
        "____, I found a book about space explorers.",
        "____, I took it to the front desk.",
        "____, the librarian scanned my library card.",
        "____, I took the book home to read."
    ],
    [
        "____, we bought seeds from the local store.",
        "____, we dug small holes in the garden dirt.",
        "____, we dropped a seed into each hole.",
        "____, we covered them up with soil.",
        "____, we watered the garden using a watering can.",
        "____, we waited for the little green sprouts."
    ]
]
def gen_p4(i):
    s = p4_stories[i]
    q = []
    q.append({"q": s[0], "opts": ["First", "Last", "Next"], "ans": "First"})
    q.append({"q": s[1], "opts": ["Second", "First", "Last"], "ans": "Second"})
    q.append({"q": s[2], "opts": ["Next", "Finally", "First"], "ans": "Next"})
    q.append({"q": s[3], "opts": ["Then", "First", "Last"], "ans": "Then"})
    q.append({"q": s[4], "opts": ["Last", "First", "Second"], "ans": "Last"})
    q.append({"q": s[5], "opts": ["Finally", "Then", "First"], "ans": "Finally"})
    return q

# Part 5 Possessive ("s", "se", "es", "ss")
p5_words = [
    ("cactus", "s", "The <div class='drop-blank p5-blank' id='p5b0'></div> spikes are sharp.", "cactus's", "cactuses"),
    ("nose", "se", "The dog's <div class='drop-blank p5-blank' id='p5b1'></div> is very wet.", "nose's", "noses"),
    ("beaches", "es", "The two <div class='drop-blank p5-blank' id='p5b2'></div> sand was very white.", "beaches'", "beach's"),
    ("kiss", "ss", "The sweet <div class='drop-blank p5-blank' id='p5b3'></div> sound was loud.", "kiss's", "kisses"),
    ("suitcase", "se", "My heavy <div class='drop-blank p5-blank' id='p5b4'></div> handle broke.", "suitcase's", "suitcases"),
    ("dishes", "es", "All the <div class='drop-blank p5-blank' id='p5b5'></div> spots were clean.", "dishes'", "dish's"),
    
    ("octopus", "s", "The <div class='drop-blank p5-blank' id='p5b0'></div> arms have suckers.", "octopus's", "octopuses"),
    ("rose", "se", "The red <div class='drop-blank p5-blank' id='p5b1'></div> petals are soft.", "rose's", "roses"),
    ("foxes", "es", "The three <div class='drop-blank p5-blank' id='p5b2'></div> dens are deep.", "foxes'", "fox's"),
    ("boss", "ss", "My <div class='drop-blank p5-blank' id='p5b3'></div> meeting is at noon.", "boss's", "bosses"),
    ("house", "se", "Our <div class='drop-blank p5-blank' id='p5b4'></div> front door is blue.", "house's", "houses"),
    ("branches", "es", "The broken <div class='drop-blank p5-blank' id='p5b5'></div> leaves fell down.", "branches'", "branch's"),
    
    ("bus", "s", "The yellow <div class='drop-blank p5-blank' id='p5b0'></div> tires are big.", "bus's", "buses"),
    ("cheese", "se", "The Swiss <div class='drop-blank p5-blank' id='p5b1'></div> smell is strong.", "cheese's", "cheeses"),
    ("glasses", "es", "Sarah's <div class='drop-blank p5-blank' id='p5b2'></div> frames are pink.", "glasses'", "glass's"),
    ("class", "ss", "The entire <div class='drop-blank p5-blank' id='p5b3'></div> project was great.", "class's", "classes"),
    ("mouse", "se", "The little <div class='drop-blank p5-blank' id='p5b4'></div> squeak was quiet.", "mouse's", "mouses"),
    ("matches", "es", "The two <div class='drop-blank p5-blank' id='p5b5'></div> tips were red.", "matches'", "match's"),
    
    ("walrus", "s", "The sleepy <div class='drop-blank p5-blank' id='p5b0'></div> whiskers twitched.", "walrus's", "walruses"),
    ("nurse", "se", "The kind <div class='drop-blank p5-blank' id='p5b1'></div> stethoscope is cold.", "nurse's", "nurses"),
    ("buses", "es", "The city <div class='drop-blank p5-blank' id='p5b2'></div> routes are long.", "buses'", "bus's"),
    ("princess", "ss", "The royal <div class='drop-blank p5-blank' id='p5b3'></div> gown is sparkly.", "princess's", "princesses"),
    ("hose", "se", "The garden <div class='drop-blank p5-blank' id='p5b4'></div> nozzle is leaking.", "hose's", "hoses"),
    ("boxes", "es", "The moving <div class='drop-blank p5-blank' id='p5b5'></div> tape came off.", "boxes'", "box's"),

    ("virus", "s", "The computer <div class='drop-blank p5-blank' id='p5b0'></div> code was deleted.", "virus's", "viruses"),
    ("base", "se", "The lamp's <div class='drop-blank p5-blank' id='p5b1'></div> weight is heavy.", "base's", "bases"),
    ("peaches", "es", "The ripe <div class='drop-blank p5-blank' id='p5b2'></div> pits are hard.", "peaches'", "peach's"),
    ("compass", "ss", "The old <div class='drop-blank p5-blank' id='p5b3'></div> glass is cracked.", "compass's", "compasses"),
    ("horse", "se", "The wild <div class='drop-blank p5-blank' id='p5b4'></div> mane is black.", "horse's", "horses"),
    ("wishes", "es", "The three <div class='drop-blank p5-blank' id='p5b5'></div> power faded away.", "wishes'", "wish's")
]

def gen_p5(i):
    items = p5_words[i*6:(i+1)*6]
    q = []
    bank = []
    for item in items:
        q.append({"q": item[2], "ans": item[3]})
        bank.append(item[3])
        bank.append(item[4])
    import random
    random.seed(i)
    random.shuffle(bank)
    return q, bank

# Generate files 6 through 10
for num in range(6, 11):
    idx = num - 6 # 0 to 4
    p1 = gen_p1(idx)
    p2 = gen_p2(idx)
    p3 = gen_p3(idx)
    p4 = gen_p4(idx)
    p5_q, p5_bank = gen_p5(idx)
    
    out = html
    # Update titles so you know which quiz it is
    out = out.replace("<title>2nd Grade Super Quiz!</title>", f"<title>2nd Grade Super Quiz - Set {num}!</title>")
    out = out.replace("<h1>🌟 2nd Grade Super Quiz! 🌟</h1>", f"<h1>🌟 2nd Grade Super Quiz - Set {num}! 🌟</h1>")
    
    # Replace the actual data cleanly using regex
    out = re.sub(r"const part1Data = \[.*?\];", f"const part1Data = {json.dumps(p1, indent=4)};", out, flags=re.DOTALL)
    out = re.sub(r"const part2Data = \[.*?\];", f"const part2Data = {json.dumps(p2, indent=4)};", out, flags=re.DOTALL)
    out = re.sub(r"const part3Data = \[.*?\];", f"const part3Data = {json.dumps(p3, indent=4)};", out, flags=re.DOTALL)
    out = re.sub(r"const part4Data = \[.*?\];", f"const part4Data = {json.dumps(p4, indent=4)};", out, flags=re.DOTALL)
    out = re.sub(r"const part5Data = \[.*?\];", f"const part5Data = {json.dumps(p5_q, indent=4)};", out, flags=re.DOTALL)
    out = re.sub(r"const p5BankWords = \[.*?\];", f"const p5BankWords = {json.dumps(p5_bank, indent=4)};", out, flags=re.DOTALL)
    
    filename = rf'f:\Python Project\kids questions\question{num}.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f"Generated {filename}")

print("Successfully created 5 completely fresh files (6-10).")

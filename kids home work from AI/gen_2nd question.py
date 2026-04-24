import sys, json, re, os

print("Starting generation of 4 new quizzes...")

with open(r'f:\Python Project\kids questions\question.html', 'r', encoding='utf-8') as f:
    html = f.read()

quizzes = [
    { # Quiz 2
        "p1": [
            { "q": "The frogs leaps into the pond.", "correct": "Not Correct" },
            { "q": "The small rabbit hops quickly.", "correct": "Correct" },
            { "q": "The cars speeds down the road.", "correct": "Not Correct" },
            { "q": "The children runs outside to play.", "correct": "Not Correct" },
            { "q": "The bright stars shine at night.", "correct": "Correct" },
            { "q": "The boat sink in the water.", "correct": "Not Correct" }
        ],
        "p2": [
            { "q": "Please accept my apologies.", "type": "Formal" },
            { "q": "My bad!", "type": "Informal" },
            { "q": "I would like to request some water.", "type": "Formal" },
            { "q": "Give me a drink.", "type": "Informal" },
            { "q": "We are delighted to see you.", "type": "Formal" },
            { "q": "Nice to see ya!", "type": "Informal" }
        ],
        "p3": [
            { "q": "What does 'pre-' mean in 'preview'?", "opts": ["Watch before", "Watch again", "Do not watch"], "ans": "Watch before" },
            { "q": "What does 'un-' mean in 'unhappy'?", "opts": ["Very happy", "Not happy", "Happy again"], "ans": "Not happy" },
            { "q": "Which suffix turns 'help' into 'without help'?", "opts": ["-ful", "-less", "-ed"], "ans": "-less" },
            { "q": "What is the root word of 'careless'?", "opts": ["Care", "Less", "Car"], "ans": "Care" },
            { "q": "What does 're-' mean in 'rebuild'?", "opts": ["Build again", "Do not build", "Build before"], "ans": "Build again" },
            { "q": "Which suffix means 'full of'?", "opts": ["-ed", "-less", "-ful"], "ans": "-ful" }
        ],
        "p4": [
            { "q": "____, we opened the board game box.", "opts": ["First", "Last", "Finally"], "ans": "First" },
            { "q": "____, we read the instructions together.", "opts": ["Second", "Next", "Last"], "ans": "Second" },
            { "q": "____, we chose our playing pieces.", "opts": ["Then", "First", "Finally"], "ans": "Then" },
            { "q": "____, we took turns rolling the dice.", "opts": ["Next", "Second", "First"], "ans": "Next" },
            { "q": "____, someone won the game!", "opts": ["Last", "First", "Next"], "ans": "Last" },
            { "q": "____, we put all the pieces back in the box.", "opts": ["Finally", "First", "Then"], "ans": "Finally" }
        ],
        "p5": [
            { "q": "The <div class='drop-blank p5-blank' id='p5b0'></div> legs are very long.", "ans": "octopus's" },
            { "q": "The <div class='drop-blank p5-blank' id='p5b1'></div> tail is gray and thin.", "ans": "mouse's" },
            { "q": "The two <div class='drop-blank p5-blank' id='p5b2'></div> leaves fell off.", "ans": "branches'" },
            { "q": "Usually the <div class='drop-blank p5-blank' id='p5b3'></div> rules are strict.", "ans": "boss's" },
            { "q": "The <div class='drop-blank p5-blank' id='p5b4'></div> computer is broken.", "ans": "class's" },
            { "q": "The two <div class='drop-blank p5-blank' id='p5b5'></div> skin is fuzzy.", "ans": "peaches'" }
        ],
        "p5_bank": ["octopus's", "octopuses", "mouse's", "mouses", "branches'", "branch's", "boss's", "bosses'", "class's", "classes", "peaches'", "peach's"]
    },
    { # Quiz 3
        "p1": [
            { "q": "The cats meow loudly for food.", "correct": "Correct" },
            { "q": "The tree branch break in the wind.", "correct": "Not Correct" },
            { "q": "The dog jump over the tall fence.", "correct": "Not Correct" },
            { "q": "The boys plays soccer after school.", "correct": "Not Correct" },
            { "q": "The red apple falls from the tree.", "correct": "Correct" },
            { "q": "The teacher write on the board.", "correct": "Not Correct" }
        ],
        "p2": [
            { "q": "I'm gonna be late.", "type": "Informal" },
            { "q": "I will be arriving shortly.", "type": "Formal" },
            { "q": "What are you doing today?", "type": "Formal" },
            { "q": "Whatcha doin?", "type": "Informal" },
            { "q": "Could you assist me, please?", "type": "Formal" },
            { "q": "Help me out here.", "type": "Informal" }
        ],
        "p3": [
            { "q": "What prefix makes 'cover' mean to find something hidden?", "opts": ["un-", "re-", "dis-"], "ans": "un-" },
            { "q": "What does 'colorLESS' mean?", "opts": ["Full of color", "Without color", "Bright color"], "ans": "Without color" },
            { "q": "What does the prefix 'dis-' mean in 'disagree'?", "opts": ["agree again", "completely agree", "do not agree"], "ans": "do not agree" },
            { "q": "Joyful means:", "opts": ["without joy", "full of joy", "to joy again"], "ans": "full of joy" },
            { "q": "What is the root word of 'reopen'?", "opts": ["re", "open", "pen"], "ans": "open" },
            { "q": "'Pretest' is a test taken:", "opts": ["after", "before", "instead of"], "ans": "before" }
        ],
        "p4": [
            { "q": "____, we found a good spot to build a sandcastle.", "opts": ["First", "Last", "Next"], "ans": "First" },
            { "q": "____, we filled our buckets with wet sand.", "opts": ["Second", "Last", "Finally"], "ans": "Second" },
            { "q": "____, we flipped the buckets upside down.", "opts": ["Then", "First", "Second"], "ans": "Then" },
            { "q": "____, we added some seashells for decoration.", "opts": ["Next", "Finally", "First"], "ans": "Next" },
            { "q": "____, we dug a moat around it.", "opts": ["Last", "First", "Second"], "ans": "Last" },
            { "q": "____, the waves washed our castle away!", "opts": ["Finally", "First", "Then"], "ans": "Finally" }
        ],
        "p5": [
            { "q": "The <div class='drop-blank p5-blank' id='p5b0'></div> tent is huge!", "ans": "circus's" },
            { "q": "The <div class='drop-blank p5-blank' id='p5b1'></div> feathers are white.", "ans": "goose's" },
            { "q": "All three <div class='drop-blank p5-blank' id='p5b2'></div> engines are loud.", "ans": "buses'" },
            { "q": "The empty <div class='drop-blank p5-blank' id='p5b3'></div> rim is cracked.", "ans": "glass's" },
            { "q": "The beautiful <div class='drop-blank p5-blank' id='p5b4'></div> color is blue.", "ans": "dress's" },
            { "q": "The two <div class='drop-blank p5-blank' id='p5b5'></div> lids are open.", "ans": "boxes'" }
        ],
        "p5_bank": ["circus's", "circuses", "goose's", "gooses", "buses'", "bus's", "glass's", "glasses", "dress's", "dresses", "boxes'", "box's"]
    },
    { # Quiz 4
        "p1": [
            { "q": "The bee fly to the flower.", "correct": "Not Correct" },
            { "q": "The monkeys swing on the vines.", "correct": "Correct" },
            { "q": "The little baby cry.", "correct": "Not Correct" },
            { "q": "The bears sleep all winter.", "correct": "Correct" },
            { "q": "The sun shine very bright today.", "correct": "Not Correct" },
            { "q": "The ducks swims in the cold water.", "correct": "Not Correct" }
        ],
        "p2": [
            { "q": "That is awesome!", "type": "Informal" },
            { "q": "That is highly impressive.", "type": "Formal" },
            { "q": "I regret to inform you.", "type": "Formal" },
            { "q": "Sorry to tell you this.", "type": "Informal" },
            { "q": "See you later!", "type": "Informal" },
            { "q": "I look forward to our next meeting.", "type": "Formal" }
        ],
        "p3": [
            { "q": "If you misspell a word, you spelled it:", "opts": ["correctly", "again", "wrong"], "ans": "wrong" },
            { "q": "What does 'fearful' mean?", "opts": ["without fear", "full of fear", "to fear before"], "ans": "full of fear" },
            { "q": "What suffix makes 'pain' mean 'having no pain'?", "opts": ["-ful", "-less", "-ed"], "ans": "-less" },
            { "q": "What does 'prepay' mean?", "opts": ["pay later", "pay before", "never pay"], "ans": "pay before" },
            { "q": "What is the root word of 'unfriendly'?", "opts": ["un", "friend", "ly"], "ans": "friend" },
            { "q": "Which word has a prefix?", "opts": ["return", "helpful", "jumping"], "ans": "return" }
        ],
        "p4": [
            { "q": "____, we got out the coloring book.", "opts": ["First", "Finally", "Next"], "ans": "First" },
            { "q": "____, we opened the box of fresh crayons.", "opts": ["Second", "First", "Last"], "ans": "Second" },
            { "q": "____, we chose a page to color.", "opts": ["Then", "Finally", "First"], "ans": "Then" },
            { "q": "____, we colored inside the lines.", "opts": ["Next", "First", "Last"], "ans": "Next" },
            { "q": "____, we signed our names at the bottom.", "opts": ["Last", "First", "Second"], "ans": "Last" },
            { "q": "____, we showed the artwork to our parents.", "opts": ["Finally", "Then", "First"], "ans": "Finally" }
        ],
        "p5": [
            { "q": "The <div class='drop-blank p5-blank' id='p5b0'></div> spread is very fast.", "ans": "virus's" },
            { "q": "The <div class='drop-blank p5-blank' id='p5b1'></div> uniform is white.", "ans": "nurse's" },
            { "q": "The three <div class='drop-blank p5-blank' id='p5b2'></div> fur coats are red.", "ans": "foxes'" },
            { "q": "The <div class='drop-blank p5-blank' id='p5b3'></div> needle points north.", "ans": "compass's" },
            { "q": "The wooden <div class='drop-blank p5-blank' id='p5b4'></div> shape is tall.", "ans": "cross's" },
            { "q": "Both <div class='drop-blank p5-blank' id='p5b5'></div> flames are hot.", "ans": "matches'" }
        ],
        "p5_bank": ["virus's", "viruses", "nurse's", "nurses", "foxes'", "fox's", "compass's", "compasses", "cross's", "crosses", "matches'", "match's"]
    },
    { # Quiz 5
        "p1": [
            { "q": "The wind blows hard during the storm.", "correct": "Correct" },
            { "q": "The big elephant drink lots of water.", "correct": "Not Correct" },
            { "q": "The snake slither through the grass.", "correct": "Not Correct" },
            { "q": "The lions roar at the zoo.", "correct": "Correct" },
            { "q": "The green frog capture a fly.", "correct": "Not Correct" },
            { "q": "The children sing loudly.", "correct": "Correct" }
        ],
        "p2": [
            { "q": "Please respond as soon as you can.", "type": "Formal" },
            { "q": "Reply ASAP.", "type": "Informal" },
            { "q": "Thank you for the gift.", "type": "Formal" },
            { "q": "Thanks for the present!", "type": "Informal" },
            { "q": "You gotta be kidding me.", "type": "Informal" },
            { "q": "I find that hard to believe.", "type": "Formal" }
        ],
        "p3": [
            { "q": "Someone who is 'thankless' has:", "opts": ["lots of thanks", "no thanks", "thanks again"], "ans": "no thanks" },
            { "q": "What does 'reappear' mean?", "opts": ["appear before", "appear again", "never appear"], "ans": "appear again" },
            { "q": "What prefix changes 'fair' to its opposite?", "opts": ["un-", "pre-", "-ful"], "ans": "un-" },
            { "q": "'Playful' means:", "opts": ["without play", "full of play", "played again"], "ans": "full of play" },
            { "q": "What is the root word of 'preheat'?", "opts": ["heat", "pre", "ate"], "ans": "heat" },
            { "q": "Which word has a suffix?", "opts": ["unzip", "rebuild", "harmless"], "ans": "harmless" }
        ],
        "p4": [
            { "q": "____, we packed our swimsuits and towels.", "opts": ["First", "Last", "Then"], "ans": "First" },
            { "q": "____, we drove perfectly down to the beach.", "opts": ["Second", "Finally", "First"], "ans": "Second" },
            { "q": "____, we set up our big umbrella on the sand.", "opts": ["Next", "Second", "First"], "ans": "Next" },
            { "q": "____, we put on our sunscreen.", "opts": ["Then", "Finally", "First"], "ans": "Then" },
            { "q": "____, we splashed in the cool ocean waves!", "opts": ["Last", "First", "Second"], "ans": "Last" },
            { "q": "____, we drove home exhausted and happy.", "opts": ["Finally", "First", "Next"], "ans": "Finally" }
        ],
        "p5": [
            { "q": "The <div class='drop-blank p5-blank' id='p5b0'></div> tusks are very sharp.", "ans": "walrus's" },
            { "q": "The yellow <div class='drop-blank p5-blank' id='p5b1'></div> holes are tiny.", "ans": "cheese's" },
            { "q": "Our two <div class='drop-blank p5-blank' id='p5b2'></div> magic came true.", "ans": "wishes'" },
            { "q": "The soft <div class='drop-blank p5-blank' id='p5b3'></div> springs are bouncy.", "ans": "mattress's" },
            { "q": "The green <div class='drop-blank p5-blank' id='p5b4'></div> blades are very tall.", "ans": "grass's" },
            { "q": "The three paint <div class='drop-blank p5-blank' id='p5b5'></div> bristles are wet.", "ans": "brushes'" }
        ],
        "p5_bank": ["walrus's", "walruses", "cheese's", "cheeses", "wishes'", "wish's", "mattress's", "mattresses", "grass's", "grasses", "brushes'", "brush's"]
    }
]

for idx, qz in enumerate(quizzes):
    num = idx + 2
    out = html
    # Update titles so you know which quiz it is
    out = out.replace("<title>2nd Grade Super Quiz!</title>", f"<title>2nd Grade Super Quiz - Set {num}!</title>")
    out = out.replace("<h1>🌟 2nd Grade Super Quiz! 🌟</h1>", f"<h1>🌟 2nd Grade Super Quiz - Set {num}! 🌟</h1>")
    
    # Replace the actual data cleanly using regex
    out = re.sub(r"const part1Data = \[.*?\];", f"const part1Data = {json.dumps(qz['p1'], indent=4)};", out, flags=re.DOTALL)
    out = re.sub(r"const part2Data = \[.*?\];", f"const part2Data = {json.dumps(qz['p2'], indent=4)};", out, flags=re.DOTALL)
    out = re.sub(r"const part3Data = \[.*?\];", f"const part3Data = {json.dumps(qz['p3'], indent=4)};", out, flags=re.DOTALL)
    out = re.sub(r"const part4Data = \[.*?\];", f"const part4Data = {json.dumps(qz['p4'], indent=4)};", out, flags=re.DOTALL)
    out = re.sub(r"const part5Data = \[.*?\];", f"const part5Data = {json.dumps(qz['p5'], indent=4)};", out, flags=re.DOTALL)
    out = re.sub(r"const p5BankWords = \[.*?\];", f"const p5BankWords = {json.dumps(qz['p5_bank'], indent=4)};", out, flags=re.DOTALL)
    
    filename = rf'f:\Python Project\kids questions\question{num}.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f"Generated {filename}")

print("Successfully created all 4 extra files.")

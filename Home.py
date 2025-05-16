
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap');         /* Times New Roman alternative */
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');             /* Helvetica Neue alternative */
@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap');      /* Courier New alternative */
@import url('https://fonts.googleapis.com/css2?family=Playwrite+US+Trad&display=swap');    /* Playwrite US Trad */
@import url('https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap');         /* Indie Flower */

.font-noto {
    font-family: 'Noto Serif', serif;
}

.font-roboto {
    font-family: 'Roboto', sans-serif;
}

.font-sourcecode {
    font-family: 'Source Code Pro', monospace;
}

.font-playwrite {
    font-family: 'Playwrite US Trad', cursive;
}

.font-indie {
    font-family: 'Indie Flower', cursive;
}
</style>
""", unsafe_allow_html=True)


if 'current_screen' not in st.session_state:
    st.session_state['current_screen'] = 0
    st.session_state['break_yet'] = False

if 'break_timer' not in st.session_state:
    st.session_state['timer'] = 15

if 'passage_key' not in st.session_state:
    st.session_state['passage_key'] = -1

if 'log' not in st.session_state:
    st.session_state['log'] = {'email': "", 'first_passage': -1, 'font_for_passage_2': -1, 'passage_1_version': -1, 'passage_1_score': -1, 'passage_2_score': -1}

if 'titles' not in st.session_state:
    # Updated passage titles
    st.session_state['titles'] = ["The Transport Cavern", "The Whispering Grove"]
    # Updated passages
    st.session_state['passages'] = [
        "In a land unlike any other, deep beneath the Crystalline Expanse, lies the Transport Cavern—a place where energy currents spiral through the air and stone seems to breathe. Within this vast, glittering chamber, a complex system of moving platforms, each glowing a soft amber, allows inhabitants to journey from one quadrant to another.\n\n"
        "The system is powered by fluxstones, which pulse with a rhythm that seems almost alive. These stones, embedded into the walls, emit waves of kinetic charge that propel the platforms without any need for visible machinery. As the charge builds, platforms glide smoothly along translucent rails, changing direction only when signaled by a flicker of blue light from the stones.\n\n"
        "Each platform can hold up to four passengers, but only when their combined weight aligns with the harmonics of the current. If the balance is off, the platform hums a warning tone and remains still until the correct distribution is restored. Despite the potential for confusion, the system is rarely delayed.\n\n"
        "Navigation is guided by driftsigns—floating panels that pulse in rhythm with the passenger’s destination thoughts. While the precise mechanism of this interaction remains unknown, the system has proven uncannily accurate, transporting travelers to even the most remote chambers.\n\n"
        "Residents have used the cavern system for centuries, adapting their daily routines to its quirks. While first-time travelers often report disorientation due to the ever-shifting patterns of the rails, most quickly become attuned to the fluid logic of the cavern. Even so, Transport Guardians remain on standby at major nodes, ready to assist if a platform misroutes or a fluxstone flickers out.",
        "At the center of the floating isle of Tura lies the Whispering Grove, a dense forest of featherleaf trees that communicate not with sound, but through patterns of light. Each tree possesses a crown of translucent leaves that shimmer in subtle hues—blues, greens, and violets—depending on stimuli sensed in the air.\n\n"
        "Observers note that when a creature walks through the grove, the trees closest to it will glow briefly in a ripple, signaling its movement to the others. Over time, researchers mapped these reactions and discovered distinct patterns associated with different kinds of movement, atmospheric pressure shifts, and even emotional states.\n\n"
        "Communication among the trees appears to be decentralized, with no single tree acting as a hub. Instead, the grove functions as a responsive network where input in one area can trigger visual echoes miles away. The color responses, while beautiful, are not random. A sudden gust of wind causes a pale green cascade, while a sharp cry elicits spirals of violet and blue.\n\n"
        "Locals living near the grove use its reactions as a form of forecasting. If the trees shimmer red-orange before dawn, it is often taken as a sign of coming storms. While scientific consensus is still forming, the correlation between tree behavior and environmental changes is strong enough to influence daily decisions.\n\n"
        "Despite its sensitivity, the grove is resilient. When a large stone fell into the western edge last season, the trees dimmed for only a moment before resuming their typical patterns. Restoration did not come from external help but from the surrounding trees recalibrating their glow, effectively “healing” the light network from within.\n\n"
        "The Whispering Grove remains an enigma. It is neither fully understood nor easily explained, but those who spend time within it often leave with a sense of being gently observed by the forest itself."
    ]
    # Updated MCQs
    st.session_state['mcqs'] = [
        [  # The Transport Cavern questions
            ["What powers the movement of the platforms in the Transport Cavern?",
                {1: "Steam engines", 2: "Magnetic rails", 3: "Driftsigns", 4: "Fluxstones", "A": 4}
            ],
            ["How is direction determined for each platform?",
                {1: "A lever attached to the rails", 2: "The thoughts of the passenger", 3: "Voice commands", 4: "Fixed route schedules", "A": 2}
            ],
            ["What happens if the passengers’ weight does not match the harmonic threshold?",
                {1: "A warning tone sounds and the platform does not move", 2: "The platform ejects passengers", 3: "The platform begins to shake violently", 4: "The platform moves slowly", "A": 1}
            ],
            ["Why are Transport Guardians stationed at major nodes?",
                {1: "To repair broken platforms", 2: "To direct traffic and stop theft", 3: "To assist travelers and fix misroutes", 4: "To collect passage fees", "A": 3}
            ],
            ["What challenge do new users of the Transport Cavern typically experience?",
                {1: "Overcrowding", 2: "Language barriers", 3: "Lack of signage", 4: "Disorientation from shifting rails", "A": 4}
            ]
        ],
        [  # The Whispering Grove questions
            ["How do the featherleaf trees communicate?",
                {1: "Through musical notes", 2: "Through colored light patterns", 3: "By releasing spores", 4: "Using underground roots", "A": 2}
            ],
            ["What happens when a creature walks through the Whispering Grove?",
                {1: "The trees grow taller", 2: "The trees emit a humming sound", 3: "Nearby trees shimmer to signal its presence", 4: "The ground pulses with energy", "A": 3}
            ],
            ["What was concluded from mapping tree reactions?",
                {1: "Different stimuli trigger specific light patterns", 2: "Only one tree controls the whole grove", 3: "Trees react randomly to light", 4: "Trees only react to human presence", "A": 1}
            ],
            ["What do locals believe a red-orange glow before dawn means?",
                {1: "The trees are angry", 2: "A traveler is near", 3: "Nightfall will be delayed", 4: "A storm is coming", "A": 4}
            ],
            ["How did the grove respond after a stone damaged its western edge?",
                {1: "The grove restored itself through recalibration", 2: "The affected trees died", 3: "The trees went dark for weeks", 4: "People had to replant the trees", "A": 1}
            ]
        ]
    ]

def enter_screen():
    st.title("Reading Comprehension Test | AP Statistics Project")
    st.write("Welcome to our AP Stats project and thanks for doing this! You'll read two different passages, with 1 minute to read each, and then you'll answer 5 multiple-choice questions about each passage. Between the passages, you'll have a 15-second break, which you can skip if you choose. You'll be able to see your scores at the end! To get started, please fill in your email in the form below and hit the start button.")
    
    with st.form("Email"):
        email = st.text_input("Please enter your school email: ")
        submitted = st.form_submit_button("Start")
        if submitted: #decide the font and the passage that the user sees first!
            if email == "open sesame!":
                st.session_state["current_screen"] = 7
                st.rerun()
            else:
                st.session_state['log']['email']
                rand_int = random.randint(1, 4)
                if rand_int == 1:
                    st.session_state["current_screen"] = 1
                    st.session_state['log']['first_passage'] = 1
                    st.session_state["passage_key"] = 0
                    st.session_state['log']['passage_1_version'] = 0
                    st.rerun()
                elif rand_int == 2:
                    st.session_state["current_screen"] = 1
                    st.session_state['log']['first_passage'] = 1
                    st.session_state["passage_key"] = 1
                    st.session_state['log']['passage_1_version'] = 1
                    st.rerun()
                elif rand_int == 3:
                    st.session_state["current_screen"] = 4
                    st.session_state['log']['first_passage'] = 2
                    st.session_state["passage_key"] = 0   
                    st.session_state['log']['passage_1_version'] = 1  
                    st.rerun()
                elif rand_int == 4:
                    st.session_state["current_screen"] = 4
                    st.session_state['log']['first_passage'] = 2
                    st.session_state["passage_key"] = 1
                    st.session_state['log']['passage_1_version'] = 0
                    st.rerun()
                else:
                    raise ValueError("Random integer out of range!")
                return

def passage_one(passage_key): #the times new roman passage
    st.empty()
    st.title(f"Passage 1: {st.session_state['titles'][st.session_state["passage_key"]]}")

    timer_placeholder = st.empty()

    st.markdown(f'<div class="font-noto">{st.session_state['passages'][st.session_state["passage_key"]]}</div>', unsafe_allow_html=True)

    for remaining in range(60, -1, -1):
        timer_placeholder.markdown(f"**Time remaining:** {remaining} seconds")
        time.sleep(1)

    st.session_state["current_screen"] = 2
    st.rerun()


def mcq_one(passage_key): #mcq associated with times new roman passage
    st.title(f"Multiple Choice 1: {st.session_state['titles'][st.session_state["passage_key"]]}")

    with st.form(f"MCQ for Passage 1: {st.session_state["passage_key"]}"):

        q_0 = st.radio(st.session_state['mcqs'][st.session_state['passage_key']][0][0], list(st.session_state['mcqs'][st.session_state['passage_key']][0][1].values())[:4])
        q_1 = st.radio(st.session_state['mcqs'][st.session_state['passage_key']][1][0], list(st.session_state['mcqs'][st.session_state['passage_key']][1][1].values())[:4])
        q_2 = st.radio(st.session_state['mcqs'][st.session_state['passage_key']][2][0], list(st.session_state['mcqs'][st.session_state['passage_key']][2][1].values())[:4])
        q_3 = st.radio(st.session_state['mcqs'][st.session_state['passage_key']][3][0], list(st.session_state['mcqs'][st.session_state['passage_key']][3][1].values())[:4])
        q_4 = st.radio(st.session_state['mcqs'][st.session_state['passage_key']][4][0], list(st.session_state['mcqs'][st.session_state['passage_key']][4][1].values())[:4])

        submitted = st.form_submit_button("Submit")

        if submitted:
            score = 0
            if q_0 == st.session_state['mcqs'][st.session_state['passage_key']][0][1][st.session_state['mcqs'][st.session_state['passage_key']][0][1]['A']]:
                score+=1
            if q_1 == st.session_state['mcqs'][st.session_state['passage_key']][1][1][st.session_state['mcqs'][st.session_state['passage_key']][1][1]['A']]:
                score+=1
            if q_2 == st.session_state['mcqs'][st.session_state['passage_key']][2][1][st.session_state['mcqs'][st.session_state['passage_key']][2][1]['A']]:
                score+=1
            if q_3 == st.session_state['mcqs'][st.session_state['passage_key']][3][1][st.session_state['mcqs'][st.session_state['passage_key']][3][1]['A']]:
                score+=1
            if q_4 == st.session_state['mcqs'][st.session_state['passage_key']][4][1][st.session_state['mcqs'][st.session_state['passage_key']][4][1]['A']]:
                score+=1
            st.session_state['log']['passage_1_score'] = score
            if not(st.session_state['break_yet']):
                st.session_state['current_screen'] = 3
                if st.session_state['passage_key'] == 0:
                    st.session_state['passage_key'] = 1
                else:
                    st.session_state['passage_key'] = 0
                st.rerun()
            else:
                st.session_state['current_screen'] = 6
                st.rerun()

def passage_two(passage_key): #random choice font
    st.empty()
    st.title(f"Passage 2: {st.session_state['titles'][st.session_state["passage_key"]]}")
    font_of_choice = random.choice(["font-roboto", "font-sourcecode", "font-playwrite", "font-indie"])
    st.session_state['log']['font_for_passage_2'] = font_of_choice

    timer_placeholder = st.empty()

    st.markdown(f'<div class={font_of_choice}>{st.session_state['passages'][st.session_state["passage_key"]]}</div>', unsafe_allow_html=True)

    for remaining in range(60, -1, -1):
        timer_placeholder.markdown(f"**Time remaining:** {remaining} seconds")
        time.sleep(1)

    st.session_state["current_screen"] = 5
    st.rerun()

def mcq_two(passage_key): #mcq associated with random font passage
    st.title(f"Multiple Choice 2: {st.session_state['titles'][st.session_state["passage_key"]]}") 

    with st.form(f"MCQ for Passage 2: {st.session_state["passage_key"]}"):

        q_0 = st.radio(st.session_state['mcqs'][st.session_state['passage_key']][0][0], list(st.session_state['mcqs'][st.session_state['passage_key']][0][1].values())[:4])
        q_1 = st.radio(st.session_state['mcqs'][st.session_state['passage_key']][1][0], list(st.session_state['mcqs'][st.session_state['passage_key']][1][1].values())[:4])
        q_2 = st.radio(st.session_state['mcqs'][st.session_state['passage_key']][2][0], list(st.session_state['mcqs'][st.session_state['passage_key']][2][1].values())[:4])
        q_3 = st.radio(st.session_state['mcqs'][st.session_state['passage_key']][3][0], list(st.session_state['mcqs'][st.session_state['passage_key']][3][1].values())[:4])
        q_4 = st.radio(st.session_state['mcqs'][st.session_state['passage_key']][4][0], list(st.session_state['mcqs'][st.session_state['passage_key']][4][1].values())[:4])

        submitted = st.form_submit_button("Submit")

        if submitted:
            score = 0
            if q_0 == st.session_state['mcqs'][st.session_state['passage_key']][0][1][st.session_state['mcqs'][st.session_state['passage_key']][0][1]['A']]:
                score+=1
            if q_1 == st.session_state['mcqs'][st.session_state['passage_key']][1][1][st.session_state['mcqs'][st.session_state['passage_key']][1][1]['A']]:
                score+=1
            if q_2 == st.session_state['mcqs'][st.session_state['passage_key']][2][1][st.session_state['mcqs'][st.session_state['passage_key']][2][1]['A']]:
                score+=1
            if q_3 == st.session_state['mcqs'][st.session_state['passage_key']][3][1][st.session_state['mcqs'][st.session_state['passage_key']][3][1]['A']]:
                score+=1
            if q_4 == st.session_state['mcqs'][st.session_state['passage_key']][4][1][st.session_state['mcqs'][st.session_state['passage_key']][4][1]['A']]:
                score+=1
            st.session_state['log']['passage_2_score'] = score

            if not(st.session_state['break_yet']):
                st.session_state['current_screen'] = 3
                if st.session_state['passage_key'] == 0:
                    st.session_state['passage_key'] = 1
                else:
                    st.session_state['passage_key'] = 0
                st.rerun()
            else:
                st.session_state['current_screen'] = 6
                st.rerun()

def break_15_sec(): 
    st.session_state['break_yet'] = True
    st.title("Break!")
    
    timer_placeholder = st.empty()
    skip = st.button("Skip")

    for remaining in range(st.session_state['timer'], -1, -1):
        timer_placeholder.markdown(f"**Time remaining:** {remaining} seconds")
        st.session_state['timer']+=(-1)
        if skip:
            break
        time.sleep(1)

    if st.session_state['log']['passage_1_score'] == -1:
        st.session_state["current_screen"] = 1
    else: 
        st.session_state["current_screen"] = 4
    
    st.rerun()

def is_empty_csv(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for i, _ in enumerate(reader):
            if i: 
                return False
    return True

@st.cache_resource
def get_csv_path():
    return os.path.join(os.getcwd(), "stored_data.csv")

def is_empty_csv(path):
    if not os.path.exists(path):
        return True
    with open(path, newline="") as f:
        return sum(1 for _ in f) <= 1

def initialize_csv():
    path = get_csv_path()
    if is_empty_csv(path):
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(list(st.session_state['log'].keys()))

def end_page_and_upload():
    st.balloons()
    st.title("Thank you!")

    initialize_csv()

    path = get_csv_path()
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(list(st.session_state['log'].values()))

def dataviewer():
    st.title("Data Viewer")
    path = get_csv_path()
    initialize_csv()  

    df = pd.read_csv(path)
    _ = st.data_editor(df, num_rows="dynamic")

if st.session_state["current_screen"] == 0:
    enter_screen()
if st.session_state["current_screen"] == 1:
    passage_one(st.session_state["passage_key"])
if st.session_state["current_screen"] == 2:
    mcq_one(st.session_state["passage_key"])
if st.session_state["current_screen"] == 3:
    break_15_sec()
if st.session_state["current_screen"] == 4:
    passage_two(st.session_state["passage_key"])
if st.session_state["current_screen"] == 5:
    mcq_two(st.session_state["passage_key"])
if st.session_state["current_screen"] == 6:
    end_page_and_upload()
if st.session_state["current_screen"] == 7:
    dataviewer()

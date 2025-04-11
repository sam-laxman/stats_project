import streamlit as st
import os
import random
import time
import pandas as pd
import csv

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
    st.session_state['titles'] = ["Polar Bears", "Volcanoes"]
    st.session_state['passages'] = ["Polar bears are uniquely adapted to survive in the harsh Arctic environment. Their thick fur provides insulation against extreme cold, while their black skin absorbs heat from the sun. Beneath their fur, a layer of fat helps retain body warmth. Their large, powerful paws allow them to swim long distances and walk on ice without slipping. Despite these adaptations, climate change has significantly affected their habitat. Melting sea ice reduces their ability to hunt seals, their primary food source, leading to declining populations in some regions.", "Volcanoes are powerful geological formations that release molten rock, ash, and gases from beneath the Earth’s surface. They form when pressure builds up in the mantle, forcing magma upward through cracks in the crust. Some volcanoes erupt explosively, sending ash high into the atmosphere, while others release slow-moving lava flows. Volcanic eruptions can cause significant environmental changes, including air pollution, climate shifts, and land formation. While dangerous, volcanoes also create fertile soil that supports agriculture in many regions around the world."]
    st.session_state['mcqs'] = [[["What is the primary function of a polar bear’s thick fur?",{1: "To help them swim faster", 2: "To insulate them from the cold", 3: "To make them appear larger to predators", 4: "To keep their skin dry", "A": 2}], ["Why do polar bears have black skin?", {1: "It helps them stay camouflaged", 2: "It absorbs heat from the sun", 3: "It protects them from predators", 4: "It helps them swim better", "A": 2}], ["How has climate change impacted polar bears?", {1: "It has helped them find more food", 2: "It has made them migrate to warmer areas", 3: "It has reduced their ability to hunt", 4: "It has increased their population", "A": 3}], ["What do polar bears primarily eat?", {1: "Fish", 2: "Penguins", 3: "Whales", 4: "Seals", "A": 4}], ["What is one advantage of polar bears’ large paws?", {1: "They allow them to move quickly on ice", 2: "They help them climb trees", 3: "They keep their fur dry", 4: "They store extra fat", "A": 1}]], [["What is one cause of a volcanic eruption?", {1: "Magma rising due to pressure", 2: "Ocean currents shifting", 3: "Lightning strikes in the atmosphere", 4: "Sudden changes in temperature", "A": 1}], ["How do explosive eruptions differ from slow-moving lava flows?", {1: "They release less ash", 2: "They send ash high into the atmosphere", 3: "They do not affect the environment", 4: "They happen only in the ocean", "A": 2}], ["What is a positive effect of volcanic activity?", {1: "It creates fertile soil", 2: "It removes toxic gases from the air", 3: "It prevents earthquakes", 4: "It stops forest fires", "A": 1}], ["What is magma?", {1: "Hardened lava on the surface", 2: "A type of volcanic gas", 3: "Molten rock beneath the Earth’s surface", 4: "The outer layer of a volcano", "A": 3}], ["What is one environmental impact of volcanic eruptions?", {1: "They lower sea levels", 2: "They create strong hurricanes", 3: "They can cause climate shifts", 4: "They increase oxygen levels in the air", "A": 3}]]]

def enter_screen():
    st.title("Reading Comprehension Test | AP Statistics Project")
    st.write("Welcome to our AP Stats project and thanks for doing this! You'll read two different passages, with 1 minute to read each, and then you'll answer 5 multiple-choice questions about each passage. Between the passages, you'll have a 15-second break, which you can skip if you choose. You'll be able to see your scores at the end! To get started, please fill in your email in the form below and hit the start button.")
    
    with st.form("Email"):
        email = st.text_input("Please enter your school email: ")
        submitted = st.form_submit_button("Start")
        if submitted: #decide the font and the passage that the user sees first!
            if email == password:
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
            
    if st.session_state["current_screen"] == 0 and not(submitted):
        with st.form("Authentication"):
            st.write("Please DO NOT enter a password unless you're part of the group running this experiment. The password lets you view the collected data.")
            password = st.text_input("Enter the password: ")
            data_view = st.form_submit_button("See Data")  
            if data_view:
                if password == "open sesame!":
                    st.session_state['current_screen'] = 7 
                    st.rerun()
                else:
                    st.error("Please enter the correct password.")
                    data_view = False
                    st.rerun()
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

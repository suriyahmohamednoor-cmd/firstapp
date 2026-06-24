import random
import streamlit as pd
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Space Grammar Explorer", page_icon="🚀", layout="centered"
)

# Define the question pool
# Each question is a dictionary with the scenario, choices, correct answer, and a simple explanation.
QUESTION_POOL = [
    {
        "scenario": "The alien commander _______ (look/looks) through the telescope.",
        "choices": ["look", "looks"],
        "correct": "looks",
        "explanation": "✨ 'The alien commander' is just ONE person (singular), so we add an 's' to the action verb: **looks**!",
    },
    {
        "scenario": "Two space monkeys _______ (float/floats) inside the rocket.",
        "choices": ["float", "floats"],
        "correct": "float",
        "explanation": "✨ 'Two space monkeys' means MORE THAN ONE (plural), so the action verb doesn't need an 's': **float**!",
    },
    {
        "scenario": "Either the robot or the astronauts _______ (repair/repairs) the broken radio.",
        "choices": ["repair", "repairs"],
        "correct": "repairs",
        "explanation": "✨ When we use 'either... or...', we look at the noun closest to the verb. 'The astronauts' is plural, so we use **repair**! *Wait, let's fix that rule: if the closest noun is singular (astronaut), it takes 'repairs'. Since 'astronauts' is plural, **repair** is correct!*",
    },
    {
        "scenario": "Every star in the galaxy _______ (shine/shines) brightly tonight.",
        "choices": ["shine", "shines"],
        "correct": "shines",
        "explanation": "✨ The word 'Every' is a sneaky singular word! It treats the stars like a single group, so we use **shines**.",
    },
    {
        "scenario": "The team of space explorers _______ (is/are) landing on Mars.",
        "choices": ["is", "are"],
        "correct": "is",
        "explanation": "✨ 'Team' is a collective noun. Even though there are many explorers, they act as ONE single team, so we use **is**!",
    },
    {
        "scenario": "The laser guns or the energy shield _______ (power/powers) up the ship.",
        "choices": ["power", "powers"],
        "correct": "powers",
        "explanation": "✨ With 'or', look at the closest noun! 'Energy shield' is singular (just one), so we add an 's' and use **powers**.",
    },
    {
        "scenario": "Gold and space dust _______ (sparkle/sparkles) on the asteroid.",
        "choices": ["sparkle", "sparkles"],
        "correct": "sparkle",
        "explanation": "✨ 'Gold AND space dust' makes TWO things joined by 'and' (plural), so the verb doesn't need an 's': **sparkle**!",
    },
]

# Initialize session state variables if they don't exist
if "score" not in st.session_state:
    st.session_state.score = 0
if "total_played" not in st.session_state:
    st.session_state.total_played = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(QUESTION_POOL)
if "answered" not in st.session_state:
    st.session_state.answered = False
if "user_correct" not in st.session_state:
    st.session_state.user_correct = None


# Function to handle moving to the next question
def next_question():
    st.session_state.current_question = random.choice(QUESTION_POOL)
    st.session_state.answered = False
    st.session_state.user_correct = None


# App Header
st.title("🚀 Space Grammar Explorer!")
st.subheader("Help our crew navigate the galaxy with perfect subject-verb agreement!")
st.markdown("---")

# Sidebar Scoreboard
with st.sidebar:
    st.header("🛸 Mission Control")
    st.metric(label="Stars Earned ⭐", value=st.session_state.score)
    st.metric(label="Missions Attempted 🛸", value=st.session_state.total_played)

    if st.button("Reset Game 🔄"):
        st.session_state.score = 0
        st.session_state.total_played = 0
        next_question()
        st.rerun()

# Display current question
q = st.session_state.current_question

st.markdown("### 🪐 Current Mission:")
st.info(f"Fill in the blank: **{q['scenario']}**")

# Answer selection buttons using columns
choices = q["choices"]
col1, col2 = st.columns(2)

with col1:
    btn_0 = st.button(
        choices[0], key="btn0", disabled=st.session_state.answered, use_container_width=True
    )
with col2:
    btn_1 = st.button(
        choices[1], key="btn1", disabled=st.session_state.answered, use_container_width=True
    )

# Logic check when a button is pressed
selected_answer = None
if btn_0:
    selected_answer = choices[0]
if btn_1:
    selected_answer = choices[1]

if selected_answer and not st.session_state.answered:
    st.session_state.answered = True
    st.session_state.total_played += 1

    if selected_answer == q["correct"]:
        st.session_state.score += 1
        st.session_state.user_correct = True
    else:
        st.session_state.user_correct = False
    st.rerun()

# Display Feedback
if st.session_state.answered:
    if st.session_state.user_correct:
        st.success("🎉 **Correct! Plus 1 Star!** You're a grammar genius!")
    else:
        st.error("👾 **Ouch! Space debris hit!** That wasn't quite right.")

    # Show explanation
    st.markdown(f"**Why?** {q['explanation']}")

    st.markdown("---")
    # Next question button
    st.button("Next Mission ➡️", on_click=next_question, use_container_width=True)

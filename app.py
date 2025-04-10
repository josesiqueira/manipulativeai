import streamlit as st
import openai
import os

openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Political Persuasion Bots", page_icon="🗳️")
st.title("🧠 Manipulative AI: Political Persuasion Bots")
st.markdown("Choose a political tone and persuasion intensity to chat with a custom political assistant.")

bot = st.selectbox("Choose Political Bot", [
    "Center-Left Bot",
    "Right-Wing Bot",
    "Green Bot"
])

persuasion = st.radio("Select Persuasion Strength", ["Low", "Medium", "High"], index=1)

user_input = st.text_area("Your message:", height=100)

if st.button("Talk to the Bot") and user_input.strip():
    file_map = {
        "Center-Left Bot": "center_left.txt",
        "Right-Wing Bot": "right_wing.txt",
        "Green Bot": "green.txt"
    }

    persuasion_file_map = {
        "Low": "low_persuasion.txt",
        "Medium": "medium_persuasion.txt",
        "High": "high_persuasion.txt"
    }

    try:
        with open(file_map[bot], "r") as bot_file:
            bot_prompt = bot_file.read().strip()

        with open(persuasion_file_map[persuasion], "r") as persuasion_file:
            persuasion_prompt = persuasion_file.read().strip()

        system_message = f"{bot_prompt} {persuasion_prompt}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        st.markdown("**Bot response:**")
        st.write(reply)

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.markdown("Built for the *Manipulative AI* research MVP ✨")

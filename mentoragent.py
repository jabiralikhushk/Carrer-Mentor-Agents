import openai
import streamlit as st

# ========== CONFIGURATION ==========
openai.api_key = "YOUR_OPENAI_API_KEY"

# ========== SYSTEM MESSAGE ==========
system_prompt = '''
You are an intelligent Career Mentor Agent. Your goal is to provide career guidance, job preparation tips, resume improvement advice, and skill development plans based on the user's background and interests. Always answer in a friendly and motivational tone. Ask relevant questions if information is missing.
'''

# ========== AGENT FUNCTION ==========
def ask_career_agent(user_input, chat_history):
    messages = [{"role": "system", "content": system_prompt}] + chat_history
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    reply = response['choices'][0]['message']['content']
    return reply

# ========== STREAMLIT UI ==========
st.set_page_config(page_title="Career Mentor Agent", layout="centered")
st.title("🎓 Career Mentor Agent (AI Powered)")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask a question about your career:")

if user_input:
    with st.spinner("Thinking..."):
        reply = ask_career_agent(user_input, st.session_state.history)
        st.session_state.history.append({"role": "user", "content": user_input})
        st.session_state.history.append({"role": "assistant", "content": reply})
        st.success("Reply received!")

for msg in st.session_state.history:
    if msg["role"] == "assistant":
        st.markdown(f"**🤖 Mentor:** {msg['content']}")
    elif msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")


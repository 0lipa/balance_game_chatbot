import streamlit as st
import time
import balance_game_function as bg
import usage as us
import chat as ch


# st.navigation([
#     # st.Page('balance_game.py',title='HOME', icon='🏠'),
#     st.Page(us.usage_page, title='How to chat', icon='🤔'),
#     st.Page(ch.chat_page,title="Let's chat",icon='🤖')
# ])

def chat_page():
    st.session_state.button1 = False
    st.markdown("<h4 style='text-align: center; '>🤓밸런스 게임을 시작해봅시다🤓</h4>",unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; '>모델을 불러오는 중입니다...</h4>",unsafe_allow_html=True)
    time.sleep(3)

    st.markdown("<h6 style='text-align: left; '>🤖</h6>",unsafe_allow_html=True)
    first_input = '안녕! 오늘은 무엇에 대해 이야기해볼까?'
    with st.container(border=True):
        st.markdown(f"<h6 style='text-align: left; '>{first_input}</h6>",unsafe_allow_html=True)
        bg.read_chatbot(first_input)

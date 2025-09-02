import time
import streamlit as st
import usage as us
import chat as ch

# st.navigation([
#     st.Page('balance_game.py',title='HOME', icon='🏠'),
#     st.Page(us.usage_page, title='How to chat', icon='🤔'),
#     st.Page(ch.chat_page,title="Let's chat",icon='🤖')
# ])

def usage_page():
    st.markdown("<h4 style='text-align: center; '>이 사이트에서는 챗봇과 재미있는 밸런스 게임을 해볼 수 있습니다.</h4>",unsafe_allow_html=True)
    time.sleep(2)

    with st.container(border=True):
        st.markdown("<h5 style='text-align: center; color : brown'>🤔 자주 묻는 질문 1 🤔</h5>",unsafe_allow_html=True)
        time.sleep(2)
        st.markdown("<h6 style='text-align: center;'>밸런스 게임 주제를 미리 생각해야 하나요?</h6>",unsafe_allow_html=True)
        time.sleep(2)

        st.markdown("<h5 style='text-align: center; color : brown'> 😎 미리 생각할 필요 없습니다❗</h5>",unsafe_allow_html=True)
        time.sleep(1)
        st.markdown("<h6 style='text-align: center;'>🤖 챗봇이 주제를 얘기해주니까요! (똑똑하죠?~)</h6>",unsafe_allow_html=True)
        time.sleep(2)
    with st.container(border=True):
        st.markdown("<h5 style='text-align: center; color: brown'>🤔 자주 묻는 질문 2 🤔</h5>",unsafe_allow_html=True)
        time.sleep(2)
        st.markdown("<h6 style='text-align: center;'>어떻게 대화를 시작해야하나요?</h6>",unsafe_allow_html=True)
        time.sleep(2)

        st.markdown("<h5 style='text-align: center;color: brown'> 😎오른쪽 위 **챗봇과 대화하기** 버튼을 눌러주세요❗</h5>",unsafe_allow_html=True)
        time.sleep(1)
        st.markdown("<h6 style='text-align: center;'>🤖 챗봇에게 '밸런스 게임을 하자'라고 이야기해봅시다 ㅎㅎ</h6>",unsafe_allow_html=True)
        time.sleep(2)

    with st.container(border=True):
        st.markdown("<h5 style='text-align: center; color: brown'>🤔 자주 묻는 질문 3 🤔</h5>",unsafe_allow_html=True)
        time.sleep(2)
        st.markdown("<h6 style='text-align: center;'>그만하고 싶으면 어떻게 해야하나요?</h6>",unsafe_allow_html=True)
        time.sleep(2)

        st.markdown("<h5 style='text-align: center;color: brown'> 😎 아주 쉬워요❗</h5>",unsafe_allow_html=True)
        time.sleep(1)
        st.markdown("<h6 style='text-align: center;'>🤖 챗봇에게 그만하고 싶다고 말하면 됩니다 ㅎㅎ</h6>",unsafe_allow_html=True)
        time.sleep(2)

    st.markdown("<h4 style='text-align: center;'>자, 그럼 밸런스 게임을 하러 가볼까요?</h4>",unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>건투를 빕니다👊</h5>",unsafe_allow_html=True)
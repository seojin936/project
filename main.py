import streamlit as st

# 게임 상태를 저장하는 세션 상태 초기화
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'turn' not in st.session_state:
    st.session_state.turn = 'player1'
if 'questions' not in st.session_state:
    st.session_state.questions = []

# 게임 시작 화면
if not st.session_state.game_started:
    st.title("스무고개 게임")
    st.write("게임을 시작하려면 아래 버튼을 클릭하세요.")
    if st.button("게임 시작"):
        st.session_state.game_started = True
        st.session_state.turn = 'player1'
        st.session_state.questions = []
        st.experimental_rerun()

# 게임 진행 화면
else:
    st.title(f"스무고개 게임 - {st.session_state.turn}의 차례")

    # 질문 기록 표시
    if st.session_state.questions:
        st.write("이전에 나온 질문들:")
        for q in st.session_state.questions:
            st.write(f"- {q}")

    # 질문 입력 및 제출
    question = st.text_input("질문을 입력하세요:")
    if st.button("질문 제출"):
        if question:
            st.session_state.questions.append(question)
            st.session_state.turn = 'player2' if st.session_state.turn == 'player1' else 'player1'
            st.experimental_rerun()
        else:
            st.warning("질문을 입력해주세요.")

    # 게임 종료 버튼
    if st.button("게임 종료"):
        st.session_state.game_started = False
        st.experimental_rerun()

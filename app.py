from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

import os
import streamlit as st

load_dotenv() # .envファイルの環境変数を読み込む

# OpenAIのAPIキーを環境変数から取得
api_key = os.getenv("OPENAI_API_KEY")

st.title("サンプルアプリ: 専門家A,Bが回答するアプリ")

st.write("##### 動作モード1: 専門家A:エンジニア")
st.write("入力フォームに質問を入力し、「実行」ボタンを押すことで専門家Aからの回答が得られます。")
st.write("##### 動作モード2: 専門家B:弁護士")
st.write("入力フォームに質問を入力し、「実行」ボタンを押すことで専門家Aからの回答が得られます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["専門家A:エンジニア", "専門家B:弁護士"]
)

st.divider() # 画面に区切り線を入れる

# 入力メッセージを格納する変数を統一
input_message = ""

if selected_item == "専門家A:エンジニア":
    input_message = st.text_input(label="エンジニアに対する質問を入力してください。")
    text_count = len(input_message)

else:
    input_message = st.text_input(label="弁護士に対する質問を入力してください。")
    text_count = len(input_message)

# 入力テキストと選択ボタンを引数にしてllmを戻り値とする関数 を定義する
def get_response(input_message, selected_item):
    if input_message:
        lmm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, openai_api_key=api_key)
        messages = [
            SystemMessage(content=f"あなたは{selected_item}です。"),
            HumanMessage(content=input_message)
            ]
        result = lmm(messages)
        return result
    else:
        st.error("質問を入力してから「実行」ボタンを押してください。")

if st.button("実行"):
    st.divider()
    if input_message:
        response = get_response(input_message, selected_item)
        if response:
            st.write(f"回答: {response.content}")
    else:
        st.error("質問を入力してから「実行」ボタンを押してください。")



from dotenv import load_dotenv
import os

from openai import OpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("サンプルアプリ: 専門家A,Bが回答するアプリ")

st.write("##### 動作モード1: 専門家A:エンジニア")
st.write("入力フォームに質問を入力し、「実行」ボタンを押すことで専門家Aからの回答が得られます。")
st.write("##### 動作モード2: 専門家B:弁護士")
st.write("入力フォームに質問を入力し、「実行」ボタンを押すことで専門家Aからの回答が得られます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["専門家A:エンジニア", "専門家B:弁護士"]
)

st.divider()

if selected_item == "専門家A:エンジニア":
    input_message = st.text_input(label="エンジニアに対する質問を入力してください。")
    text_count = len(input_message)

else:
    input_message_B = st.text_input(label="弁護士に対する質問を入力してください。")
    text_count = len(input_message_B)


if st.button("実行"):
    st.divider()

    if selected_item == "専門家A:エンジニア":
        if input_message:
            response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "あなたは親切なアシスタントです。"},
                        {"role": "user", "content": input_message}
                    ]
                )
            st.write(f"回答: {response.choices[0].message.content}")

        else:
            st.error("質問を入力してから「実行」ボタンを押してください。")

    elif selected_item == "専門家B:弁護士":
        if input_message_B:
            response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "あなたは親切なアシスタントです。"},
                        {"role": "user", "content": input_message_B}
                    ]
                )
            st.write(f"回答: {response.choices[0].message.content}")

        else:
            st.error("質問を入力してから「実行」ボタンを押してください。")

    else:
        st.error("動作モードを選択してから「実行」ボタンを押してください。")
import streamlit as st
from streamlit import set_page_config

import functions

todos = functions.get_todos()

set_page_config(
    title = "Todos",
    layout = "vertical"
)
def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todoapp")
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

st.text_input(label="New todo:", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)



st.session_state
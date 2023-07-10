import streamlit as st
import functions
import os

if not os.path.exists('file.txt'):
    with open('file.txt', 'w') as file:
        pass
todos = functions.get_todos()
def todo_add():
    todo = st.session_state['new_todo']
    todos.append(todo+'\n')
    functions.write_todos(todos)

st.title('My to do tasks web app')

for index , item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label='todo to add',placeholder='Enter your todo.....',key='new_todo', on_change=todo_add)





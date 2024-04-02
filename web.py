import streamlit as st
import todosfunctions

todos = todosfunctions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"# dictionary for data entered in webapp
    todos.append(todo)
    todosfunctions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=f"checkbox_{index}")
    if checkbox:
        todos.pop(index)
        todosfunctions.write_todos(todos)
        del st.session_state[f"checkbox_{index}"]
        st.experimental_rerun()

st.text_input(label="Enter ToDo", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

#st.session_state
# prints it in webapp directly

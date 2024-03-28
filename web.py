import streamlit as slt
import functions

def addTodo():
    todo = slt.session_state["todoInputBox"]+"\n"
    todos.append(todo)
    functions.writeTodos(todos)

todos = functions.getTodos()

slt.title("My Todo App")
slt.subheader("Todos")
slt.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = slt.checkbox(todo, key=todo)
    if checkbox == True:
        todos.pop(index)
        functions.writeTodos(todos)
        del slt.session_state[todo]
        slt.rerun()

slt.text_input(label=" ", placeholder="enter todo here",
               on_change=addTodo, key="todoInputBox")

slt.session_state
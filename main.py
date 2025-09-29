# PYTHON - WORDING W/ STRINGS: MY INFO
from pyscript import when, display, document

def function1(e):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    message = f""" Student Profile:\n
    Name   : {name}
    Age    : {age}
    School : {school}

    Result:\n
    Your name is {name}, currently at {age} years old. You are currently studying at {school}.
    """

    display(message, target="output")
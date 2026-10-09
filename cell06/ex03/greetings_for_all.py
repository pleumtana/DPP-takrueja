#!/usr/bin/env python3

def greetings(name="noble stranger"):
    
    if name == "noble stranger":
        print("noble stranger")

    elif not isinstance(name, str):
        print("Error! It was not a name")

    else:
        print("Hello, " + name + "!")


greetings("Tanawat")
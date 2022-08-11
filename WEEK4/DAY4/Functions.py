def hello_world(name="world", age="unknown", language="EN"):
    if(language=="EN"):
        print(f"hello {name}. Age is {age}")
    elif(language=="FR"):
        print(f"bonjour {name}. Age est {age}")
    else:
        print("language is not not supported")

hello_world("Pragassen", 24, "FR")
hello_world(name="Yajna", language="FR")
hello_world(language="Kreole")
hello_world() #this will print hello world by default.
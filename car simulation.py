command = set()
while True:
    input_command = input("> ").lower()
    if input_command == "help":
        print('''
start - To start the car.
stop - To stop the car.
exit - To exit
            ''')
    elif input_command == "start":
        if "start" in command:
            print("Car already started.")
            if "stop" in command:
                command.remove("stop")
        else:
            print("Engine started....")
    elif input_command == "stop":
        if "stop" in command:
            print("Car already stopped.")
            if "start" in command:
                command.remove("start")
        else:
            print("Car stopped.")
    elif input_command ==  "exit":
        break
    else:
        print("I don't understand you....")
    command.add(input_command)
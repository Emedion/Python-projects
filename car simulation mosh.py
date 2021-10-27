started = False
while True:
    input_command = input("> ").lower()
    if input_command == "help":
        print('''
start - To start the car.
stop - To stop the car.
exit - To exit
            ''')
    elif input_command == "start":
        if started:
            print("Car already started!")
        else:
            print("Car started...")
            started = True
    elif input_command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            print("Car stopped")
            started = False

    elif input_command ==  "exit":
        break
    else:
        print("I don't understand you....")
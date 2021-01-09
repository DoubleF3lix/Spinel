# Spinel
A minecraft server wrapper written in python.

This program in its current state only allows you to read the chat and send commands (as the server).

## Tutorial
First, install spinel by running `pip install spinel` in the terminal.

Import Spinel by using `import spinel` at the top of your file.
You'll need a server premade (which can be done with [Pyrite](https://github.com/ProfessorFelix/Pyrite)). Rename your server `.jar` file to `spinel_server.jar`

Now, make an instance of your server with: `server = spinel.server(path)`.

Start the server with `server.start()`.

To read messages and send commands, make a while loop like so:
```
while True:
    msg = server.latest_message()
    
    if msg:
        print(msg.raw) # this prints the whole message
        print(msg.author) # this prints the name of the one who sent the message
        print(msg.content) # this prints the message content

        server.write("say Hello, World") # Writes "Hello, World" to the chat repeatedly
```

## Example
```
import spinel

server = spinel.server()
server.start()

while True:
    msg = server.latest_message()

    if msg:
        print(msg.raw)
        if msg.content.split(" ")[0] == "!math":
            result = eval(msg.content.split(" ")[1])
            output = 'tellraw @a {"text":"' + msg.content.split(" ")[1] + '=' + str(result) + '"}'
            server.write(output)
```
            
This code prints all messages to the python terminal and allows the user to perform basic math using the `!math` command.

## Note
If you print just `msg`, then it will print `msg.raw` instead. It is reccomended you use `msg.raw` anyway to be more explicit.
You'll need to manually close your server terminal before relaunching 

## Dependencies
* os
* subprocess
* sys
* threading
* queue

## Credits
* Ravbug
* Princess
* Winter_Snake
* vdvman1
* AjaxGB
* A2
* PeerHeer

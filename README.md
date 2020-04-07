# Spinel
A minecraft server wrapper written in python.

This program in its current state only allows you to read the chat and send commands (as the server).

## Tutorial
First, download the `spinel.py` file and put it in the same file as your server.
You'll also need to install any dependencies you don't have already below.

Import Spinel by using `import spinel` at the top of your file.
You'll need a server premade (which can be done with [Pyrite])(https://github.com/Xephlon/Pyrite). Rename your server `.jar` file to `spinel_server.jar`

Now, make an instance of your server with: `server = spinel.server()`. By default, this registeres the server as being in a folder named `server` which is in the same folder as `spinel.py`, but this can be changed by using `server = spinel.server(path)`.

Start the server with `server.start()`.

To read messages and send commands, make a while loop like so:
```
while True:
    msg = server.latestMessage()
    
    if msg != None:
        print(msg.raw) # this prints the whole message
        print(msg.author) # this prints the name of the one who sent the message
        print(msg.content) # this prints the message content
```

## Example
```
import spinel

server = spinel.server()
server.start()

while True:
    msg = server.latestMessage()

    if msg != None:
        print(msg.raw)
        if msg.content.split(" ")[0] == "!math":
            result = eval(msg.content.split(" ")[1])
            output = 'tellraw @a {"text":"' + msg.content.split(" ")[1] + '=' + str(result) + '"}'
            server.write(output)
```
            
This code prints all messages to the python terminal and allows the user to perform basic math using the `!math` command.

## Notes
On windows, the server will be automatically closed when the program runs. It does this by killing the `java.exe` process, so if you are a Java developer, you might want to consider disabling this feature using `server.start(killServer=False)`. For Linux and Mac users, the server must be closed manually before launching or else Spinel will return an error.

## Dependencies
* os
* subprocess
* sys
* platform 
* psutil (install with pip)
* threading
* queue

## Credits
* Ravbug
* nigel
* Winter_Snake
* vdvman1
* AjaxGB
* A2

## Planned Features
* Built in data gathering (like player.position())
* Built in commands (player.teleport(), server.say(), block.fill(), etc.)
* Automatic server closing for Mac and Linux

import os
import subprocess
import sys
from threading import Thread
from queue import Queue, Empty 

# https://stackoverflow.com/questions/375427/non-blocking-read-on-a-subprocess-pipe-in-python
class server:
    def __init__(self, server_dir=os.path.join(os.getcwd(), "server")):
        self.server_dir = server_dir
        self.queue = Queue()
        self.thread = Thread()
        self.ON_POSIX = 'posix' in sys.builtin_module_names

        self.server_output = []

    def _queue(self, stdout, queue):
        for line in iter(stdout.readline, b''):
            queue.put(line)
            self.server_output.append(line.replace("\n", ""))
        stdout.close()

    def start(self, wait_for_server=True, nogui=False):
        startup_cmd = "java -jar spinel_server.jar"
        if nogui:
            startup_cmd += " --nogui"
        self.pipe = subprocess.Popen(startup_cmd, cwd=self.server_dir, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True, text=True, bufsize=1, close_fds=self.ON_POSIX)
        self.thread = Thread(target=self._queue, args=(self.pipe.stdout, self.queue))
        self.thread.daemon = True
        self.thread.start() 

        if wait_for_server:
            server_up = False
            # Wait for the server to startup by checking for the "help" message
            while not server_up:
                for line in self.server_output:
                    if "For help, type \"help\"" in line:
                        server_up = True

    def latest_message(self):
        try: 
            return message(self.queue.get_nowait().replace("\n", ""))
        except Empty: 
            pass

    def write(self, msg):
        self.pipe.stdin.write(msg + "\n")

class message:
    def __init__(self, message):
        self.raw = message
        self.author = ""
        self.content = ""
        try: 
            # checks if the message has a valid author (prevents things like commands from registering as chat)
            if message.split(" ")[3].startswith("<") and message.split(" ")[3].endswith(">"):
                self.content = message.split(" ")[4:]
                self.content = " ".join(self.content)
                self.author = message.split(" ")[3].replace(">", "").replace("<", "")
        except IndexError:
            pass

    def __str__(self):
        return self.raw

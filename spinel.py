import os
import platform
import subprocess
import sys

from queue import Empty, Queue
from threading import Thread

import psutil

# https://stackoverflow.com/questions/375427/non-blocking-read-on-a-subprocess-pipe-in-python


class Server:
    def __init__(self, server_dir=os.path.join(os.getcwd(), "server")):
        self.server_dir = server_dir
        self.queue = Queue()
        self.thread = Thread()
        self.on_posix = 'posix' in sys.builtin_module_names

    def _queue(self, stdout, queue):
        for line in iter(stdout.readline, b''):
            queue.put(line)
        stdout.close()

    def start(self, kill_server=True):
        if kill_server:
            for process in psutil.process_iter():
                if (process.name() == "java.exe" and platform.system() == "Windows"):
                    process.kill()

        self.pipe = subprocess.Popen(f"java -jar spinel_server.jar", cwd=self.server_dir, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True, text=True, bufsize=1, close_fds=self.on_posix)
        self.thread = Thread(target=self._queue, args=(self.pipe.stdout, self.queue))
        self.thread.daemon = True
        self.thread.start()

    def latest_message(self):
        try:
            return Message(self.queue.get_nowait().replace("\n", ""))
        except Empty:
            pass

    def write(self, msg):
        self.pipe.stdin.write(msg + "\n")


class Message:
    def __init__(self, message):
        try:
            # checks if the message has a valid author (prevents things like commands from registering as chat)
            if message.split(" ")[3].startswith(">") and message.split(" ")[3].endswith("<"):
                self.raw = message
                self.content = message.split(" ")[4:]
                self.content = " ".join(self.content)
                self.author = message.split(" ")[3].replace(">", "").replace("<", "")
        except IndexError:
            pass

# a simple command for traversing between dirs :3
import os

def execute(self, directory):
    os.chdir(directory
             .replace("##HOME", str(self.homedir))
             .replace("##START", str(self.startingdir))
             .replace("'", "")
             .replace('"', "")
             )

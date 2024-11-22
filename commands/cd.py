import os


def execute(self, directory):
    if directory == "##HOME":
        os.chdir(self.homedir)
    else:
        os.chdir(directory)

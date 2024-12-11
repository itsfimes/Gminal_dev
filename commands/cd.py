import os


def execute(self, directory):
    # if directory == "##HOME":
    #     os.chdir(self.homedir)
    # elif directory == "##START":
    #     os.chdir(self.startingdir)
    # else:
    os.chdir(directory.replace("##HOME", self.homedir).replace("##START", self.startingdir))

import os


def execute(self, directory):
    # if directory == "##HOME":
    #     os.chdir(self.homedir)
    # elif directory == "##START":
    #     os.chdir(self.startingdir)
    # else:
    os.chdir(directory.replace("##HOME", str(self.homedir)).replace("##START", str(self.startingdir)))

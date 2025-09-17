# By customising this file you can make gminal look however you'd like
# Exciting right?
# Well not really, but since I chose to not make the core of Gminal open-source,
# but I still want you to have control over most things, that Gminal is doing,
# I felt like this was the best way to do it
# So enjoy, and let me know your thoughts about this feature :3
# dang the :3 emoji looks really angry with the font im using :c

id = "Default print"
version = "0.1"
is_modded = 0  # Make this number 1 if you edit this file, it doesn't have any meaning, apart from the text on startup showing, that your Gminal is modded


def gmin_print(message, internal=False, from_logger=False, *args, **kwargs):
    # The "internal" arg is used for signaling if the message is just internal -> thus doesn't need to be displayed
    # The "from_logger" arg signals if the message is from the logger, it's mostly messages, that get passed into the latest.log file
    if not internal or not from_logger:
        print(message, *args, **kwargs)
    else:
        print(message, *args, **kwargs)  # replace this pass by a print function, if you want to see this stuff
        # or alternatively if you manage to implement some textual renderer or something, have this be logged to some widget


def get_id(self):
    return id


def get_version(self):
    return version


def get_is_modded():
    return is_modded

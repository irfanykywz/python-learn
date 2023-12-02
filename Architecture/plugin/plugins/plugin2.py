import plugins


class PluginB(plugins.Base):

    def __init__(self):
        pass

    def start(self):
        print("Plugin B")
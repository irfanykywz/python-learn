import plugins


class PluginA(plugins.Base):

    def __init__(self):
        self.pluginName = 'Awwe'
        pass

    def start(self):
        print("Plugin A")
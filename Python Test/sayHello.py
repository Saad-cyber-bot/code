class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window

        return self.window

if _name_ == "__main__":
    SayHello().run()
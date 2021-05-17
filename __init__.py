from mycroft import MycroftSkill, intent_file_handler


class ArtesMarciais(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('marciais.artes.intent')
    def handle_marciais_artes(self, message):
        self.speak_dialog('marciais.artes')


def create_skill():
    return ArtesMarciais()


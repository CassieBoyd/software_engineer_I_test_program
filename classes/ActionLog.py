class ActionLog:
    def __init__(self):
        self.action_list = []

    def write_action_log_to_file(self):
        # with statement opens text file, writes action_list in file then closes file.
        with open("log.txt",'w') as log:
            log.writelines(self.action_list)

    # Appends action_list with actions
    def add_to_action_list(self, action):
        self.action_list.append(action)
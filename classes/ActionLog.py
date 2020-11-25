class ActionLog:
    def __init__(self):
        self.action_list = ["thing1", "thing2"]

    def write_action_log_to_file(self):
        # file_object = open(r"../log.txt","w")
        # file_object.writelines(self.action_list)
        # file_object.close()
        with open("log.txt",'w') as log:
            log.writelines(self.action_list)
            
    def add_to_action_list(self, action):
        self.action_list.append(action)
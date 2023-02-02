class Smartphone:
    def __init__(self, mark_smartphone, model_smartphone, user_number):
        self.mark_smartphone = mark_smartphone
        self.model_smartphone = model_smartphone
        self.user_number = user_number


    def print_list(self):
        print(self.mark_smartphone, self.model_smartphone, self.user_number)
        
import datetime
class MyCalendar:
    def convertdate(self, args):
        if type(args) == str:
            try:
                args = datetime.datetime.strptime(args, '%d/%m/%Y').date()
            except ValueError:
                args = 0
        return args
    def __init__(self, *args):
        self.datas = []
        self.temp = []
        for dt in args:
            self.temp.append(self.convertdate(dt))
        for dt in self.temp:
            if type(dt) != int and type(dt) != list and type(dt) != tuple:
                self.datas.append(self.convertdate(dt))
    def add_holiday(self, *args):
        for dt in args:
            if self.convertdate(dt) not in self.temp:
                self.temp.append(self.convertdate(dt))
        for dt in self.temp:
            if self.convertdate(dt) not in self.datas and type(dt) != int:
                self.datas.append(self.convertdate(dt))
    def check_holiday(self, args):
        if self.convertdate(args) in self.datas:
            print(args)
            isholiday = True
        else:
            isholiday = False
        return isholiday
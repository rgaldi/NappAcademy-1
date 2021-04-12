import datetime as dt


class MyCalendar:
    def __init__(self, *args):
        self.datas = []
        self.check_format(*args)

    def convert(self, dt1):
        if isinstance(dt1, dt.date):
            return dt1

        try:
            converted = dt.datetime.strptime(dt1, '%d/%m/%Y').date()
            return converted
        except (ValueError, TypeError):
            return None

    def check_format(self, *args):
        for item in args:
            item2 = self.convert(item)
            if item2 is not None:
                self.datas.append(item2)

    def add_holiday(self, *dates):
        self.check_format(*dates)
        local_datas = set(self.datas)
        self.datas = list(local_datas)

    def check_holiday(self, item):
        item2 = self.convert(item)
        if item2 is not None and item2 in self.datas:
            return True
        else:
            return False

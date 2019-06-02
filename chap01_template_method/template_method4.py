from abc import ABCMeta  # 2.6以上限定
from abc import abstractmethod


class Report(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.title = "月次報告"
        self.text = ["順調", "最高"]

    def output_report(self):
        self.output_start()
        self.output_head()
        self.output_body_start()
        self.output_body()
        self.output_body_end()
        self.output_end()

    def output_body(self):
        for line in self.text:
            self.output_line(line)

    @abstractmethod
    def output_start(self): pass

    @abstractmethod
    def output_head(self): pass

    @abstractmethod
    def output_body_start(self): pass

    @abstractmethod
    def output_line(self, line): pass

    @abstractmethod
    def output_body_end(self): pass

    @abstractmethod
    def output_end(self): pass


if __name__ == "__main__":
    report = Report()
    report.output_report()

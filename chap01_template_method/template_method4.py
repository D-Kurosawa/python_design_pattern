import abc


class Report(metaclass=abc.ABCMeta):

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

    @abc.abstractmethod
    def output_start(self): pass

    @abc.abstractmethod
    def output_head(self): pass

    @abc.abstractmethod
    def output_body_start(self): pass

    @abc.abstractmethod
    def output_line(self, line): pass

    @abc.abstractmethod
    def output_body_end(self): pass

    @abc.abstractmethod
    def output_end(self): pass


if __name__ == "__main__":
    report = Report()
    report.output_report()

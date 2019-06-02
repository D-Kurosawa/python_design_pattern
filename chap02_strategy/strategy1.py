class Report(object):
    def __init__(self, title, text, formatter):
        self.title = title
        self.text = text
        self.formatter = formatter

    def output_report(self):
        self.formatter.output_report(self.title, self.text)


class Formatter(object):
    def output_report(self, title, text):
        assert False


class HTMLFormatter(Formatter):
    def output_report(self, title, text):
        print("<html>")
        print("<head>")
        print("<title>%s</title>" % (title,))
        print("</head>")
        print("<body>")
        for line in text:
            print("<p>%s</p>" % (line,))
        print("</body>")
        print("</html>")


class PlainTextFormatter(Formatter):
    def output_report(self, title, text):
        print("***%s***" % (title,))
        for line in text:
            print(line)


if __name__ == "__main__":
    report = Report("月次報告", ["順調！", "最高です！"],
                    PlainTextFormatter())
    report.output_report()
    print("-" * 70)
    report = Report("月次報告", ["順調！", "最高です！"],
                    HTMLFormatter())
    report.output_report()
    print("-" * 70)

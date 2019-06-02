class Report(object):
    def __init__(self, title, text, formatter):
        self.title = title
        self.text = text
        self.formatter = formatter

    def output_report(self):
        # self.formatter(self.title, self.text)
        self.formatter(self)


def html_formatter(content):
    print("<html>")
    print("<head>")
    print("<title>%s</title>" % (content.title,))
    print("</head>")
    print("<body>")
    for line in content.text:
        print("<p>%s</p>" % (line,))
    print("</body>")
    print("</html>")


if __name__ == "__main__":
    report = Report(u"月次報告", [u"順調！", u"最高です！"],
                    html_formatter)
    report.output_report()

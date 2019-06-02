class Report(object):
    def __init__(self, title, text, formatter):
        self.title = title
        self.text = text
        self.formatter = formatter

    def output_report(self):
        # self.formatter.output_report(self.title, self.text)
        # formatter として、呼び出し可能型を取るように変更
        self.formatter(self.title, self.text)


# 関数版のHTMLFormatter
def html_formatter(title, text):
    print("<html>")
    print("<head>")
    print("<title>%s</title>" % (title,))
    print("</head>")
    print("<body>")
    for line in text:
        print("<p>%s</p>" % (line,))
    print("</body>")
    print("</html>")


# Callable版 PlainTextFormatter
class PlainTextFormatter(object):
    def __init__(self, decoration="***"):
        self.decoration = decoration

    def __call__(self, title, text):
        print("%s%s%s" % (self.decoration, title, self.decoration))
        for line in text:
            print(line)


if __name__ == "__main__":
    report = Report(u"月次報告", [u"順調！", u"最高です！"],
                    html_formatter)
    report.output_report()
    report = Report(u"月次報告", [u"順調！", u"最高です！"],
                    PlainTextFormatter())
    report.output_report()
    report = Report(u"月次報告", [u"順調！", u"最高です！"],
                    PlainTextFormatter("==="))
    report.output_report()

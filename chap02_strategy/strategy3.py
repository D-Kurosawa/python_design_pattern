class Report:
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
    print(f"<title>{content.title}</title>")
    print("</head>")
    print("<body>")
    for line in content.text:
        print(f"<p>{line}</p>")
    print("</body>")
    print("</html>")


if __name__ == "__main__":
    report = Report("月次報告", ["順調！", "最高です！"], html_formatter)
    report.output_report()

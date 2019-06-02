class Report:
    def __init__(self):
        self.title = "月次報告"
        self.text = ["順調", "最高"]

    def output_report(self, output_format):
        if output_format == "plain":
            print(f"*** {self.title} ***")
        elif output_format == "html":
            print("<html>")
            print("<head>")
            print(f"<title>{self.title}</title>")
            print("</head>")
            print("<body>")

        for line in self.text:
            if output_format == "plain":
                print(line)
            else:
                print(f"<p>{line}</p>")

        if output_format == "html":
            print("</body>")
            print("</html>")


if __name__ == "__main__":
    report = Report()
    report.output_report("plain")
    report.output_report("html")

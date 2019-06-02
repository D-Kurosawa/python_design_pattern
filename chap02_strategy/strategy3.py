"""
Report.output_reportでformatterに渡されているのは、titleとtext の2つだけですが、
今後渡すべき要素が増える可能性もあります。例えば日付や提出者名など。

そこで、一々要素を選んで渡すのではなく、Reportオブジェクトそのものを渡してしまう方法もあります。

しかし、こうするとformatterとReportの結合度が増してしまいます。

Strategyパターンを使う際は、ストラテジの範囲と渡すべきデータを見極める必要があり、
それを誤ると、第2第3のStrategyの適用を妨げることにもなります。
"""


class Report:
    def __init__(self, title, text, formatter):
        self.title = title
        self.text = text
        self.formatter = formatter

    def output_report(self):
        """
        self.formatter(self.title, self.text) -> self.formatter(self)
        """
        self.formatter(self)


def html_formatter(content):
    """
    :type content: Report
    """
    print("<html>")
    print("<head>")
    print(f"<title>{content.title}</title>")
    print("</head>")
    print("<body>")
    for line in content.text:
        print(f"<p>{line}</p>")
    print("</body>")
    print("</html>")


class PlainTextFormatter:
    def __init__(self, decoration="***"):
        self.decoration = decoration

    def __call__(self, content):
        """
        :type content: Report
        """
        print(f"{self.decoration}{content.title}{self.decoration}")
        for line in content.text:
            print(line)


if __name__ == "__main__":
    report = Report("月次報告", ["順調！", "最高です！"], html_formatter)
    report.output_report()

    print("-" * 70)

    report = Report("月次報告", ["順調！", "最高です！"], PlainTextFormatter())
    report.output_report()

    print("-" * 70)

    report = Report("月次報告", ["順調！", "最高です！"], PlainTextFormatter("==="))
    report.output_report()

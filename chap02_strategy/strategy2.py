"""
strategy1.pyのHTMLFormatterもPlainTextFormatterもFormatterから継承しているのは、
output_reportメソッドだけです。
特別なアルゴリズムやメンバ変数を受け継いでいるわけではありません。
すると、Formatter基底クラスなんか要らないんじゃないか、と考えるのは自然な発想です。

Pythonは『ダックタイピング』を採用しています。
オブジェクトの出自がどうであろうが、output_reportメソッドがあればそれで良いのです。
さらに言えば、HTMLFormatterも、PlainTextFormatterも、output_report以外にメソッドがありません。
メンバ変数すらないのです。これじゃあ、ただの関数と変わりません。

ならば、本当に関数にしてしまえばいいじゃありませんか！

Reportクラスにも多少の変更しました。これで関数を渡すことが出来ます。

また、PlainTextFormatterもタイトルの飾り部分を変更できるようにし、
関数のように呼び出せるようにしました。

__call__メソッドを定義すれば、インスタンスを関数のように呼び出せるようになります。
"""


class Report:
    """
    :type title: str
    :type text: list[str]
    :type formatter: any
    """

    def __init__(self, title, text, formatter):
        """
        :type title: str
        :type text: list[str]
        :type formatter: any
        """
        self.title = title
        self.text = text
        self.formatter = formatter

    def output_report(self):
        # self.formatter.output_report(self.title, self.text)
        # formatter として、呼び出し可能型を取るように変更
        self.formatter(self.title, self.text)


# 関数版のHTMLFormatter
def html_formatter(title, text):
    """
    :type title: str
    :type text: list[str]
    """
    print("<html>")
    print("<head>")
    print(f"<title>{title}</title>")
    print("</head>")
    print("<body>")
    for line in text:
        print(f"<p>{line}</p>")
    print("</body>")
    print("</html>")


# Callable版 PlainTextFormatter
class PlainTextFormatter:
    """
    :type decoration: str
    """

    def __init__(self, decoration="***"):
        """
        :type decoration: str
        """
        self.decoration = decoration

    def __call__(self, title, text):
        """
        :type title: str
        :type text: list[str]
        """
        print(f"{self.decoration}{title}{self.decoration}")
        for line in text:
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

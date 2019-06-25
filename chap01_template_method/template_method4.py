"""
Pythonはその性質上、インターフェイスとか抽象メソッドを
ズバリ定義する構文というものはありませんでした。
template_method3.pyの例では assert 文があるので、
Reportクラスをインスタンス化して呼び出すと例外が投げられますが。
たぶんあまり必要になることがなかったのでしょう。

大規模開発では必要な事もあるため、Python 2.6/3.0 からは、
abcモジュールが追加されました。ちなみにabc は Abstract Base Classes の略です。
ジョークではありません。この程度の例では必要ない（むしろ、邪魔）のですが、
一応、abcも使ってみました。

これで、Report をインスタンス化しようとすると、バッチリ怒ってくれます。
"""
import abc


class Report(metaclass=abc.ABCMeta):
    """
    :type title: str
    :type text: list[str]
    """

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
    def output_start(self):
        pass

    @abc.abstractmethod
    def output_head(self):
        pass

    @abc.abstractmethod
    def output_body_start(self):
        pass

    @abc.abstractmethod
    def output_line(self, line):
        pass

    @abc.abstractmethod
    def output_body_end(self):
        pass

    @abc.abstractmethod
    def output_end(self):
        pass


class HTMLReport(Report):
    def output_start(self):
        print("<html>")

    def output_head(self):
        print("<head>")

        print(f"<title>{self.title}</title>")

        print("</head>")

    def output_body_start(self):
        print("<body>")

    def output_line(self, line):
        """
        :type line: str
        """
        print(f"<p>{line}</p>")

    def output_body_end(self):
        print("</body>")

    def output_end(self):
        print("</html>")


class PlainTextReport(Report):
    def output_head(self):
        print(f"*** {self.title} ***")

    def output_line(self, line):
        """
        :type line: str
        """
        print(line)

    def output_start(self):
        pass

    def output_body_start(self):
        pass

    def output_body_end(self):
        pass

    def output_end(self):
        pass


if __name__ == "__main__":
    report = PlainTextReport()
    report.output_report()

    report = HTMLReport()
    report.output_report()

    report = Report()
    report.output_report()

"""
HTMLもプレーンテキストも、
    ヘッダ情報を出力
        ↓
    タイトルを出力
        ↓
    本文を出力
        ↓
    末尾の部分を出力
と言う処理は変わりません。

そこで、オブジェクト指向の基本を使います。
抽象基底クラスを定義して、不変な処理は基底クラスに
フォーマット毎に異なる処理の詳細はサブクラスに任せるのです。

これでコードがすっきりした上、新しいフォーマットへの対応も容易になったはずです。
"""


class Report(object):
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

    def output_start(self):
        assert False, "called abstruct method output_start"

    def output_head(self):
        print(self.title)

    def output_body_start(self):
        assert False, "called abstruct method output_body_start"

    def output_line(self, line):
        assert False, "called abstruct method output_body"

    def output_body_end(self):
        assert False, "called abstruct method output_body_end"

    def output_end(self):
        assert False, "called abstruct method output_end"


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
        print(f"<p>{line}</p>")

    def output_body_end(self):
        print("</body>")

    def output_end(self):
        print("</html>")


class PlainTextReport(Report):
    def output_start(self):
        pass

    def output_head(self):
        print(f"*** {self.title} ***")

    def output_body_start(self):
        pass

    def output_line(self, line):
        print(line)

    def output_body_end(self):
        pass

    def output_end(self):
        pass


if __name__ == "__main__":
    report = PlainTextReport()
    report.output_report()

    report = HTMLReport()
    report.output_report()

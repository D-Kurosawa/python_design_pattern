"""
HTMLを出力するクラスを作ったら、後からプレーンテキストでも出力してくれと言われてしまった。
とりあえず、フォーマットを引数で指定するようにしたら・・・

このプログラムの悪い点は、output_reportの中でフォーマット固有の処理が絡み合っていること。
もし、PostScript、CSV等とフォーマットが増えていったら・・・やってられません！
デザインパターンの原則「変わるものを変わらないものから分離する」に反しています。
"""


class Report:
    """
    :type title: str
    :type text: list[str]
    """

    def __init__(self):
        self.title = "月次報告"
        self.text = ["順調", "最高"]

    def output_report(self, output_format):
        """
        :type output_format: str
        """
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

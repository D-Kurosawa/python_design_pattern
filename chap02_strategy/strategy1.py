"""
Strategyパターンでは、変化するアルゴリズムを、サブクラスではなく第３者のオブジェクトに移譲します。

    前回のTemplateMethodパターンではレポートのフォーマットの切り替えに、
    抽象基底クラスを作成し、詳細な点はサブクラスに任せます。

    TemplateMethodパターンの欠点は、継承を用いていることです。
    サブクラスは基底クラスに依存してしまうのです。
    一度基底クラスがコケると全ての子孫が皆コケてしまいますし、
    互いにくっついて離すことが出来ないのです。

    また、TemplateMethodパターンは柔軟性に問題があります。

    まず、実行時のHTMLで出力するか・プレーンテキストで出力するかを切り替えづらいのです。
    そして、新しいフォーマットを作るたびに、一々サブクラスを作るのは大げさな場合があります。

そこで登場するのがStrategyパターンです。

このとき、HTMLFormatter・PlainTextFormatterはそれぞれ、
「レポートをフォーマットする」という同じ目的のストラテジ Strategyを定義しています。

ストラテジオブジェクトは、同じインターフェイスと動作を備えている必要があります。
今回の場合はtitleとtextを引数に取りレポートを出力するoutput_reportメソッドです。
同じインターフェイスを持っているので、ストラテジの利用者（コンテキスト Context）
は実行時にストラテジを切り替えることが容易になるのです。

また、「レポートをフォーマットする」という機能の実装をformatterに任せて、
Reportからその部分を取り除くことで「関心の分離」を行うことが出来ます。
"""


class Report:
    def __init__(self, title, text, formatter):
        self.title = title
        self.text = text
        self.formatter = formatter

    def output_report(self):
        self.formatter.output_report(self.title, self.text)


class Formatter:
    def output_report(self, title, text):
        assert False


class HTMLFormatter(Formatter):
    def output_report(self, title, text):
        print("<html>")
        print("<head>")
        print(f"<title>{title}</title>")
        print("</head>")
        print("<body>")
        for line in text:
            print(f"<p>{line}</p>")
        print("</body>")
        print("</html>")


class PlainTextFormatter(Formatter):
    def output_report(self, title, text):
        print(f"***{title}***")
        for line in text:
            print(line)


if __name__ == "__main__":
    report = Report("月次報告", ["順調！", "最高です！"], PlainTextFormatter())
    report.output_report()

    print("-" * 70)

    report = Report("月次報告", ["順調！", "最高です！"], HTMLFormatter())
    report.output_report()

    print("-" * 70)

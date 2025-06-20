from flask import Flask

app = Flask(__name__)

@app.route('/')
def law_of_sines_and_cosines():
    return '''
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>公民：国家と政治の解説</title>
    <style>
        /* 全体スタイル */
        body {
            font-family: "Helvetica Neue", Arial, sans-serif;
            background-color: #fdfdfd;
            color: #333;
            margin: 0;
            padding: 0;
        }

        /* ヘッダー */
        header {
            background-color: #3498db;
            color: #fff;
            padding: 20px 10%;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        header h1 {
            font-size: 2.5rem;
            margin: 0;
        }

        /* コンテンツ領域 */
        main {
            max-width: 1200px;
            margin: 20px auto;
            padding: 10px 10%;
            line-height: 1.8;
        }

        /* セクションのデザイン */
        section {
            margin-bottom: 40px;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        section h2 {
            font-size: 1.8rem;
            color: #2c3e50;
            margin-bottom: 15px;
            border-left: 5px solid #3498db;
            padding-left: 10px;
        }

        section p {
            margin-bottom: 15px;
        }

        section ul, section ol {
            margin-left: 20px;
            padding-left: 20px;
        }

        section ul li, section ol li {
            margin-bottom: 10px;
        }

        .highlight {
            color: #e74c3c;
            font-weight: bold;
        }

        /* リストスタイル */
        ul {
            list-style-type: disc;
        }

        ol {
            list-style-type: decimal;
        }

        /* リンクや強調 */
        a {
            color: #3498db;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        /* フッター */
        footer {
            text-align: center;
            color: #888;
            font-size: 0.9rem;
            padding: 10px;
            background-color: #f4f4f4;
            border-top: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <header>
        <h1>公民：国家と政治の解説</h1>
    </header>

    <main>
        <section>
            <h2>国家の役割</h2>
            <p>国家は、国民の生活を守り、社会を円滑に運営するために以下の役割を果たしています。</p>
            <ul>
                <li><span class="highlight">治安維持</span>：警察や防衛力を通じて国民の安全を確保。</li>
                <li><span class="highlight">法律の制定と執行</span>：憲法に基づき、国民の権利を守る法律を整備。</li>
                <li><span class="highlight">経済活動の調整</span>：税金や公共事業を通じて経済の安定化を図る。</li>
                <li><span class="highlight">社会保障</span>：医療、教育、年金などの制度を提供し、国民の福祉を向上。</li>
                <li><span class="highlight">外交と国際協力</span>：他国との関係を維持し、国際的な課題に取り組む。</li>
            </ul>
        </section>

        <section>
            <h2>総理大臣の選ばれ方</h2>
            <p>日本の総理大臣（内閣総理大臣）は、以下の手順で選ばれます。</p>
            <ol>
                <li>国会議員が投票する「<span class="highlight">首班指名選挙</span>」で選ばれる。</li>
                <li>衆議院と参議院で別の人が選ばれた場合、衆議院の議決が優先される。</li>
                <li>首班指名された候補者が天皇から正式に任命を受けて総理大臣に就任。</li>
            </ol>
            <p>総理大臣は内閣のトップとして、以下の役割を果たします：</p>
            <ul>
                <li>内閣の方針を決定。</li>
                <li>閣僚（大臣）を任命・罷免する権限を持つ。</li>
                <li>国会や外交の場で国家を代表する。</li>
            </ul>
        </section>

        <section>
            <h2>天皇の仕事（国事行為）</h2>
            <p>天皇は日本国憲法において「<span class="highlight">日本国および日本国民統合の象徴</span>」とされています。天皇が行う仕事（<span class="highlight">国事行為</span>）には以下があります。</p>
            <ul>
                <li>内閣総理大臣や最高裁判所長官の任命。</li>
                <li>国会の召集や衆議院の解散を宣言。</li>
                <li>憲法改正や条約の公布。</li>
                <li>外国の大使や国賓の接遇。</li>
            </ul>
            <p>天皇は政治的権限を持たず、内閣の助言と承認に基づいて国事行為を行います。</p>
        </section>

        <section>
            <h2>民営化とは</h2>
            <p><span class="highlight">民営化</span>とは、国や地方自治体が運営している事業を民間企業に移管することです。</p>
            <h3>民営化の目的</h3>
            <ul>
                <li>経営の効率化：民間企業の自由な運営によってコスト削減やサービス向上を図る。</li>
                <li>政府の負担軽減：国の財政負担を減らし、資源を他の分野に振り分ける。</li>
                <li>市場競争の促進：競争原理によって品質向上が期待される。</li>
            </ul>
            <h3>日本における主な民営化の事例</h3>
            <ul>
                <li><span class="highlight">日本郵政</span>：2007年に郵便局や貯金事業を分社化。</li>
                <li><span class="highlight">国鉄（現：JR）</span>：1987年に分割・民営化され、現在は地域ごとの鉄道会社として運営。</li>
                <li><span class="highlight">NTT</span>：1985年に民営化され、通信事業の自由化を促進。</li>
            </ul>
            <h3>民営化の課題</h3>
            <ul>
                <li>採算が合わない地域でのサービス縮小の懸念。</li>
                <li>国民全体への利益が行き渡らない可能性。</li>
                <li>市場独占のリスク（例：競争が生じない場合）。</li>
            </ul>
        </section>
    </main>

    <footer>
        © 2024 公民解説！！！
    </footer>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

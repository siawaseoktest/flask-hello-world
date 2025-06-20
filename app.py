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
    <title>二次関数の解説</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        .example {
            background-color: #f9f9f9;
            padding: 15px;
            border-left: 4px solid #007BFF;
            margin: 20px 0;
        }
        code {
            background-color: #eaeaea;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
        }
        .formula {
            background-color: #f4f4f4;
            padding: 10px;
            border: 1px solid #ccc;
            margin: 10px 0;
            font-family: monospace;
            display: inline-block;
        }
    </style>
</head>
<body>
    <h1>二次関数の解説</h1>
    <p>
        二次関数とは、次の形で表される関数です：
    </p>
    <div class="formula">
        y = ax<sup>2</sup> + bx + c &nbsp; (a ≠ 0)
    </div>
    <p>ここで、<code>a</code>, <code>b</code>, <code>c</code> は定数で、<code>a ≠ 0</code> が条件です。</p>

    <h2>二次関数の特徴</h2>
    <h3>1. グラフの形</h3>
    <ul>
        <li>二次関数のグラフは放物線になります。</li>
        <li><code>a &gt; 0</code> のとき、グラフは上に開いた形（下に凸）。</li>
        <li><code>a &lt; 0</code> のとき、グラフは下に開いた形（上に凸）。</li>
    </ul>

    <h3>2. 頂点と対称軸</h3>
    <ul>
        <li>放物線には対称性があり、対称軸は次の式で表されます：<br>
            <div class="formula">x = -b / (2a)</div>
        </li>
        <li>頂点はグラフの最も高い点または低い点で、その座標は次の通りです：<br>
            <div class="formula">頂点の座標: (-b / (2a), c - b<sup>2</sup> / (4a))</div>
        </li>
    </ul>

    <h3>3. x切片とy切片</h3>
    <ul>
        <li><strong>x切片：</strong> \(x\)-軸との交点は、方程式 <code>ax<sup>2</sup> + bx + c = 0</code> を解くことで求められます。</li>
        <li><strong>y切片：</strong> \(y\)-軸との交点は、<code>x = 0</code> を代入して求めます。その値は次の通りです：<br>
            <div class="formula">y = c</div>
        </li>
    </ul>

    <h2>例題</h2>
    <div class="example">
        <p>次の二次関数について考えます：</p>
        <div class="formula">y = x<sup>2</sup> - 4x + 3</div>
        <ol>
            <li>対称軸： <code>x = -(-4) / (2 * 1) = 2</code></li>
            <li>頂点：<br>
                <code>x = 2</code> を代入すると、<code>y = 2<sup>2</sup> - 4(2) + 3 = -1</code>。<br>
                したがって、頂点の座標は <code>(2, -1)</code>。</li>
            <li>y切片：<br>
                <code>x = 0</code> を代入すると、<code>y = 3</code>。</li>
        </ol>
        <p>このグラフは、頂点が <code>(2, -1)</code> にあり、対称軸は <code>x = 2</code> です。</p>
    </div>

    <h2>まとめ</h2>
    <p>二次関数の重要なポイント：</p>
    <ul>
        <li>放物線の形は定数 <code>a</code> の符号によって決まる。</li>
        <li>頂点と対称軸を求めることで、グラフの形状を理解しやすくなる。</li>
        <li>y切片やx切片も、グラフの特徴を把握する上で重要。</li>
    </ul>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

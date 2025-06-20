from flask import Flask

app = Flask(__name__)

@app.route('/')
def law_of_sines_and_cosines():
    return '''
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>正弦定理と余弦定理</title>
        <style>
            body { font-family: sans-serif; padding: 2rem; line-height: 1.6; }
            h1 { color: #2c3e50; }
            h2 { color: #34495e; }
            code { background: #f4f4f4; padding: 0.2em 0.4em; border-radius: 4px; }
        </style>
    </head>
    <body>
        <h1>三角形の定理：正弦定理と余弦定理</h1>
        
        <h2>🔷 正弦定理（せいげんていり）</h2>
        <p>
            任意の三角形において、角の正弦とその向かい側の辺との比はすべて等しくなります。
        </p>
        <p>
            <code>a / sin(A) = b / sin(B) = c / sin(C)</code><br>
            （ここで、a, b, c は各角 A, B, C の向かいの辺の長さ）
        </p>

        <h2>🔶 余弦定理（よげんていり）</h2>
        <p>
            三角形の一辺の長さの2乗は、他の2辺の長さの2乗の和から、それら2辺とその間の角の余弦の積の2倍を引いたものに等しくなります。
        </p>
        <p>
            <code>c² = a² + b² - 2ab × cos(C)</code><br>
            （同様に、他の辺にも適用できます）
        </p>

        <h2>📘 用途</h2>
        <ul>
            <li>正弦定理：2つの角と1つの辺がわかっているときの三角形の解法に使えます。</li>
            <li>余弦定理：3辺がわかっている場合や、2辺とその間の角がわかっている場合に有効です。</li>
        </ul>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

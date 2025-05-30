# ボードゲーム「ハッククラッド」用ツール
ゲームの詳しい内容は下記URLを参照
https://sites.google.com/view/hackclad/home

# 作成した経緯
表題のボードゲームでは、敵の行動パターンがあらかじめプレイヤーに知らされており、その情報を元にプレイヤーは意思決定を行う。しかし、盤面に実際の敵の行動が図示されているわけではないため少々わかりづらいと感じていた。また、javascriptとflaskによるアプリ開発の学習用にちょうど良いと思い作成した。

# つまづいたところ
盤面のどの位置に敵のコマがあるかなど、マス目を特定するための方法がわからなかった。最終的には、縦、横の座標を配列で表すこととした。

# 使用技術
python 3.12
flask

# テスト実行手順
リポジトリのクローン
```
git clone https://github.com/ex-test228/clad_tool.git
```

依存関係のインストール
```
pip install -r requirements.txt
```

ディレクトリの移動
```
cd clad_tool
```

実行  
macOS / Linux:
```
python3 main.py
```
Windows:
```
python main.py
```

haikus
![image](https://github.com/ituyama/haikus/assets/42466955/4d26bbf1-e548-493a-88ec-f627ff65da27)

haikusは、与えられた俳句から季語を識別し、その俳句の形式と構造を分析するPythonモジュールです。
機能

    季語の識別: 俳句に含まれる季語を識別します。
    俳句の形式分析: 与えられた俳句が伝統的な5-7-5の構造を持つかどうかを分析します。
    
使用方法

まず、モジュールをインポートします：

python

from haikus import haikus

次に、分析したい俳句をリスト形式で関数に渡します：

python

user_haiku = ["古池", "蛙飛び込む", "水の音"]
result = haikus(user_haiku)
print(result)

依存関係

    PyKakasi: 日本語テキストのカナ変換に使用されます。

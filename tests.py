import json
from pykakasi import kakasi

# JSONデータを読み込む
with open('kigo.json', 'r', encoding='utf-8') as f:
    kigo_data = json.load(f)

# Kakasiの初期化
kakasi_instance = kakasi()

# ひらがな変換を行う関数


def hiragana(text):
    kakasi_instance.setMode('J', 'H')
    conv = kakasi_instance.getConverter()
    return conv.do(text)

# 俳句か短歌を判定する関数


def determine_poem_type(haiku):
    # 俳句か短歌かの判定はひらがなの文字数で行う（俳句は17音、短歌は31音以下）
    haiku_length = len(hiragana(haiku))
    if haiku_length == 17:
        return "俳句"
    elif haiku_length <= 31:
        return "短歌"
    else:
        return "その他"

# 俳句に含まれている季語とひらがな読みを取得する関数


def find_kigo(haiku, kigo_list):
    found_kigo = []
    for kigo_entry in kigo_list:
        kigo = kigo_entry['kigo']
        readings = kigo_entry['readings']
        for reading in readings:
            if kigo in haiku or reading in haiku:
                found_kigo.append({"kigo": kigo, "reading": reading})
                break  # 一度見つかったら中止
    return found_kigo

# 俳句を5-7-5の形式または5-7-5-7-7の形式に分割し、判別結果を配列で返す関数


def process_haiku_list(haiku_list):
    results = []
    for haiku in haiku_list:
        poem_type = determine_poem_type(haiku)
        found_kigo = find_kigo(haiku, kigo_data)
        result = {
            "poem_type": poem_type,
            "kigo": found_kigo
        }
        results.append(result)
    return results

# 俳句の上の句、中の句、下の句を分割して判別結果を返す関数


def process_haiku_parts(upper, middle, lower):
    haiku_list = [upper, middle, lower]
    results = process_haiku_list(haiku_list)
    return results


results = process_haiku_parts("古池や", "蛙とびこむ", "水のおと")
print("判別結果(JSON形式):")
print(json.dumps(results, ensure_ascii=False))

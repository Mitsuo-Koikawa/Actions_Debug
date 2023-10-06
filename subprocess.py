import os, requests, subprocess

# 設定ファイルの内容
data_files = [
    {
        "name": "Tenki",
        "title": "テスト",
        "url": "https://www.data.jma.go.jp/developer/xml/feed/regular.xml",
        "format": "xml",
        "license": None
    },
    {
        "name": "TokyoOpenDataCatalog",
        "title": "東京オープンデータカタログ",
        "url": "https://catalog.data.metro.tokyo.lg.jp/api/3/action/package_search?q=*:*&rows=999999&start=0",
        "format": "csv",  # このフォーマットは仮定しています。実際のフォーマットに合わせて変更してください。
        "license": None
    },
    {
        "name": "NurserySchool",
        "title": "東京都認証保育所一覧",
        "url": "https://www.fukushi.metro.tokyo.lg.jp/kodomo/hoiku/ninsyo/ichiran.files/ninshouichiran050801.xlsx",
        "format": "xlsx",
        "license": None
    }
]

# 各フォーマットに対応するコンバータアプリの辞書
converters = {
    "csv": "CSV.exe",
    "xml": "XML.exe",
    "xlsx": "excel.exe"
}

# 外部スクリプトを生成する関数
def generate_script(data_file):
    # ダウンロードコマンド
    download_cmd = f"wget {data_file['url']} -O {data_file['name']}.{data_file['format']}\n"
    
    # コンバータアプリを実行するコマンド
    converter_cmd = f"{converters[data_file['format']]} {data_file['name']}.{data_file['format']} -o {data_file['name']}.txt\n"
    
    return download_cmd + converter_cmd

# 外部スクリプトを実行する関数
def execute_script(script_name):
    subprocess.run(["bash", script_name])

# メインの処理
if __name__ == "__main__":
    script_name = "conversion_script.sh"
    
    # スクリプトの内容を生成
    script_content = "#!/bin/bash\n\n"
    for data_file in data_files:
        script_content += generate_script(data_file)
    
    # スクリプトをファイルに書き込む
    with open(script_name, "w") as f:
        f.write(script_content)
    
    # スクリプトを実行可能にする
    os.chmod(script_name, 0o755)
    
    # スクリプトを実行
    execute_script(script_name)



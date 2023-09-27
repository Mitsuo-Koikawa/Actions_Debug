import re, os, requests, yaml
from datetime import datetime

DATA_FOLDER = "docs/data"

def fetch_data(url):  
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def main():
    with open('opendata.yml', 'r') as yml:
        config = yaml.safe_load(yml)
        od_links = config['link']

    html = "# Open Data 整形済み最新データ\n"

    # dataフォルダの中を全部消す
    for item in os.listdir(DATA_FOLDER):
        item_path = os.path.join(DATA_FOLDER, item)
        if os.path.isfile(item_path):
                os.remove(item_path)

    for od_link in od_links:
        obj_data = fetch_data(od_link['url'])
        
        # 現在の時間をもとにファイル名を作成
        now = datetime.now().strftime('%Y%m%d-%H:%M:%S')
        file_name = f"{now}-"

        # Curl形式の様々な引き数のついたURLに対応したファイル名抽出
        pattern = r'/([^/]+?\.[a-zA-Z0-9]{1,8})$'
        file_org = re.search(pattern, od_link['url'])
        file_name += od_link['name'] if file_org is None else file_org.group(1)
        
        # ファイルにDataを保存
        with open(DATA_FOLDER + "/" + file_name, 'w') as f:
            f.write(obj_data)
        
        html += '[' + od_link['name'] + '](data/' + file_name + ') \('
        html += '[source](' + od_link['url'] + ')\)\n\n'

if __name__ == '__main__':
    main()

import requests
from datetime import datetime

def fetch_xml():
    url = 'https://www.data.jma.go.jp/developer/xml/feed/regular.xml'
    
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def main():
    xml_content = fetch_xml()
    
    # 現在の時間をもとにファイル名を作成
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f"./docs/data/{now}.xml"
    
    # ファイルにXMLを保存
    with open(file_name, 'w') as f:
        f.write(xml_content)

if __name__ == '__main__':
    main()

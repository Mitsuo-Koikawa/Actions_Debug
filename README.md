# GitHub Actionsを使ったOpenDataの自動取得
GitHub Actionsで定期的にPythonを実行し公開されているOpenDataを取得し、整形し、GitHub Pagesで整形済みデータを公開する。

# 設定方法
```
README.md       : このファイル
fetch.py        : OpenDataを読み込むPython Script
.github/
  + workflows/
    - main.yml  : Actions Workflow設定ファイル
docs/           : GitHub Pages公開ページ
  - index.html  : Pythonで自動生成されるTop Page
  - xxx.xml     : 取得されたOpenData
  + images/     : 各種画像ファイル
```
[手順]
1. RepositoryのClone
1. ローカル環境でのPython動作確認
1. 自分のRepository作成
1. アクセストークンなどをRepositoryのSecretに保存
1. Actionsでスクリプトの自動実行設定
1. Pagesで取得したOpenDataの公開

## Secretの設定
adfdas

## Actionsの設定
dsdf


## Pagesの設定
だｓふぁ

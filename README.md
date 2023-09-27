# OpenDataの自動取得と整形
GitHub Actionsで定期的にPythonを実行し、公開されているOpenDataを取得、整形、GitHub Pagesで整形済みデータの公開をします。

GitHub Pagesは公開Repositoryになるため、OpenDataの取得やファイル保存に必要な各種トークンはRepositoryのSecretに保存しています。
GitHubは容量制限がありますし、Actionsの処理は遅めなので大容量のデータ処理には向きません。

# 設定方法
```
README.md       : このファイル
fetch.py        : OpenDataを読み込むPython Script
opendata.yml    : 読み込むデータのリンク集
.github/
  + workflows/
    - main.yml  : Actions Workflow設定ファイル
docs/           : GitHub Pages公開ページ
  - index.html  : Pythonで自動生成されるTop Page
  + data/       : 取得されたOpenDataの保存場所
  + images/     : 各種画像ファイル
```
[手順]
1. RepositoryのClone
1. ローカル環境でのPython動作確認
1. 新しいRepository作成
1. アクセストークンなどをRepositoryのSecretに登録
1. Actionsでスクリプトの自動実行設定
1. Pagesで取得したOpenDataの公開

## RepositoryのClone
Cloneしたいフォルダを作成し、そのフォルダの中で以下を実行します。
> git clone https://github.com/Mitsuo-Koikawa/Actions_Debug.git .

## ローカル環境でのPython動作確認
opendata.yml ファイルを編集して、アクセスをしたいOpenDataの情報を登録して、以下を実行してください。
> python3 fetch.py
docs/dataフォルダーの中に取得したデータが登録され、そのデータへのリンクを含んだindex.mdが自動作成されます。以前に取得したデータは残りません。

## 新しいRepository作成
新しいRepositoryをGitHubのWeb画面上で作成し、動作確認をしたローカルのRepositoryをPushしてください。詳細は他のサイトをご参照ください。

## Secretの設定
Actionsが作成したファイル変更を反映させるため、GitHubのアクセストークンが必要です。アカウントの管理画面から必要に応じて新規アクセストークンを作成してください。

Repositoryの管理画面の一番下の方にある [Secrets and variables] を開いて、[Actions] を選んでください。
[New repository secret] というボタンを押して、使用するアクセストークンを以下の名前で登録してください。
> ACTIONS_TOKEN

## Actionsの設定
Repositoryの[Actions]タブを選んで[New workflow]を選んでください。設定ファイルとして以下のファイルを登録してください。
> .github/workflows/main.yml

上記 YAMLファイルの中の以下の数値を変更する事で実行する周期を指定できます。
> on:
>  schedule:
>    - cron: '*/60 * * * *' # Every hour

Actionsは実行に時間がかかるので、あまり小さい数字にしないでください。
Workflowが正常に動作するとActionsタブの中に実行履歴が保存されてゆきます。

## Pagesの設定
他のサイトを参考にして、GitHub Pagesを設定してください。
> Branch: main
> Folder: docs


タグごとにsimplenoteのコンテンツを標準出力に表示するスクリプトです

メモアプリをsimplenoteからNotionに移行する時に使いました

dockerでの実行手順
```
# 最初にenvを作ってUSERNAMEとPASSWORDにsimplenoteのユーザ名(メールアドレス)とパスワードを設定します
# 出力先のファイルも作成してください
touch .env output.txt

# その後dockerをbuildしてattach
docker build ./
docker run -it --env-file .env -v $(pwd):/workdir simplenote /bin/bash

# コンソールからタグ名を指定してpythonを実行するとタグのコンテンツが標準出力に表示されます
python /workdir/src/main.py タグ名
```

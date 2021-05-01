タグごとにsimplenoteのコンテンツを標準出力に表示するスクリプトです
メモアプリをsimplenoteからNotionに移行する時に使いました

dockerでの実行手順
```
# 最初にenvを作ってUSERNAMEとPASSWORDにsimplenoteのユーザ名(メールアドレス)とパスワードを設定します
touch .env
docker run -it --name simplenote ./

# その後dockerをbuildしてattach
docker build ./
docker run -it --env-file .env simplenote /bin/bash
docker run -it --env-file .env -v $(pwd):/workdir simplenote /bin/bash

# コンソールからタグ名を指定してpythonを実行するとタグのコンテンツが標準出力に表示されます
python /workspace/src/main.py タグ名
```

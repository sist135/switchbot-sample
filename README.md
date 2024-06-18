# README

### リポジトリの取得
Git がない場合、ZIP 形式でのダウンロードも可能。
```
git clone https://github.com/sist135/switchbot-sample
```

### 環境構築
```
cd switchbot-sample

# Python 仮想環境の作成
python -m venv .venv

# Python 仮想環境の有効化
.\.venv\Scripts\activate

# Python 仮想環境の確認
gcm python | select -expand source
# -> C:/path/to/switchbot-sample/.venv/Scripts/python.exe

# パッケージのインストール
pip install -r requirements.txt
```

### API トークンの取得
1. 公式サイトの手順に従って API トークンを取得 \
https://blog.switchbot.jp/announcement/api-v1-1/ 

1. プロジェクトルート直下の `.env` ファイルに API トークン、シークレットを入力

```
echo 'SWITCHBOT_TOKEN="<your-api-token>"' >> .env
echo 'SWITCHBOT_SECRET="<your-api-secret>"' >> .env
```

### デバイス ID の登録
デバイス一覧を取得する
```
python src\list_devices
```
出力された JSON で照明のデバイス ID を確認する

デバイス ID を .env ファイルに書き込む
```
echo 'DEVICE_ID'="<your-device-id>"' >> .env
```

### 消灯の実行
```
python src\main.py
```

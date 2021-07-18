立ち上げ方

1. ビルドする(初回のみ)
```
docker-compose build
```

2. サーバーを立ち上げる
```
docker-compose up -d
```
3. サーバーにアクセス
localhost:8001/list
にアクセス 

4. サーバーを止める
```
docker-compose down
```

コマンドの実行の仕方
```
docker-compose run --rm web [コマンド]
```

dockerの動作確認
```
docker ps -a
```

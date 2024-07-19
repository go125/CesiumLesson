# React

- Cesiumをソースから動作させる
  - Cesium自体の改修は今回想定していないため、あくまでも実験として実施した。
- [参考](https://qiita.com/keijipoon/items/615ebaf7561a27d744f5#cesium%E3%81%A8%E3%81%AF)

## Execution

### コンテナ起動

```
docker-compose up -d
```

## コンテナへの接続(フロント)

```
docker compose exec front sh
```

## npm init

- 初回のみ実施する

```
mkdir cesium-project
cd cesium-project
npm init -y
npm install cesium
```

## アプリ起動

- stを用いて静的ファイルをホストする

```
cd cesium-project
npm i st -g
st -nc -i index.html -p 3000
```

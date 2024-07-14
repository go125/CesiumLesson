# React

- Cesiumとの連携方法は検討中であるが、難易度が高いと思われる

## Execution

### コンテナ起動

```
docker-compose up -d
```

## コンテナへの接続(フロント)

```
docker compose exec front sh
```

## npm install

- 初回のみ実施する

```
cd react-basic
npm install
npm install cesium@1.82
```

## アプリ起動

```
npm start
```

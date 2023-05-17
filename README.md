# CesiumLesson

- [参考Webサイト(React)](https://qiita.com/Bashi50/items/8086e27c8e356e786227)
- [参考Webサイト(Cesium)](https://qiita.com/Bashi50/items/8086e27c8e356e786227)

## Execution

### 最初に1回だけ実行

- docker-compose.yamlとDockerfileを用意する
- プロジェクトの作成

```
docker-compose run --rm front sh -c "npm install -g create-react-app && create-react-app react-test"
```

### 起動

- Docker Compose内の「command: sh -c "cd react-test && yarn start"」が自動実行される

```
docker-compose up
```

### アクセストークンの設定

- [設定方法](https://zenn.dev/lesserpanda/articles/2baa2f6eed690b)

## Google 3D Tile

- Docker起動の上、[こちら](http://localhost:3000/index2.html)からアクセス可能です。
- Google API Keyは現在手入力が必要です。
    - Google API Keyの利用はIIS VPN経由に制限しています。

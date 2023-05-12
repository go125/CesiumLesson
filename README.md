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

- 現状アクセストークンはindex.htmlに直接入力する必要があります。

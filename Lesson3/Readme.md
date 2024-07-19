# Dockerを用いた環境構築

## 起動

## コンテナへの接続

```
docker compose up -d
docker compose exec front bash
```

## アプリケーションの起動

```
cd src/front
pip install -r requirements.txt
streamlit run app.py --server.port 5000
```

- Cesiumの表示は困難。

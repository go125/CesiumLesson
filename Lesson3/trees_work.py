import pandas as pd
import folium
from folium.plugins import MarkerCluster

# CSVファイルのパス
csv_file = "/content/trees.csv"  # 適宜変更してください

# CSVファイルを読み込む
data = pd.read_csv(csv_file)

# 地図の中心を指定（緯度と経度の平均値を使用）
latitude_mean = data["緯度"].mean()
longitude_mean = data["経度"].mean()
map_center = [latitude_mean, longitude_mean]

# Foliumマップを作成
map_trees = folium.Map(location=map_center, zoom_start=12)
marker_cluster = MarkerCluster().add_to(map_trees)

# CSVのデータをマーカーとして地図に追加
for index, row in data.iterrows():
    folium.Marker(
        location=[row["緯度"], row["経度"]],
        popup=(
            f"<b>樹種:</b> {row['樹種']}<br>"
            f"<b>区分:</b> {row['区分']}<br>"
            f"<b>樹高:</b> {row['樹高(m)']}m<br>"
            f"<b>枝張:</b> {row['枝張(m)']}m<br>"
            f"<b>幹周:</b> {row['幹周(cm)']}cm<br>"
            f"<b>行政区:</b> {row['行政区']}<br>"
            f"<b>路線名:</b> {row['路線名']}<br>"
            f"<b>通称道路名:</b> {row['通称道路名']}"
        )
    ).add_to(marker_cluster)

# 地図を保存
output_file = "trees_map.html"
map_trees.save(output_file)

print(f"地図を {output_file} に保存しました。ブラウザで開いて確認してください。")

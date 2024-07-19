import streamlit as st
import streamlit.components.v1 as components

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
components.html("<h1>テスト1</h1>",height = 150)
components.html(f"""
            <h2>テスト2</h2>
            <script src="https://cesium.com/downloads/cesiumjs/releases/1.82/Build/Cesium/Cesium.js"></script>
            <link href="https://cesium.com/downloads/cesiumjs/releases/1.82/Build/Cesium/Widgets/widgets.css" rel="stylesheet">
            <div id="cesiumContainer"></div>
            <script>
                const CESIUM_API_KEY = {st.secrets["cesium_api_key"]};
                Cesium.Ion.defaultAccessToken = CESIUM_API_KEY;
                const viewer = new Cesium.Viewer('cesiumContainer');
                var your_3d_tiles =viewer.scene.primitives.add(new Cesium.Cesium3DTileset({{
                url : 'https://plateau.geospatial.jp/main/data/3d-tiles/bldg/13100_tokyo/13104_shinjuku-ku/low_resolution/tileset.json'
                }}));
                viewer.flyTo(your_3d_tiles);
            </script>"""
            ,height = 500)
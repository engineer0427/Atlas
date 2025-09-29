import os
from pyvis.network import Network

class Visualizer:
    def __init__(self):
        # 네트워크 기본 설정
        self.net = Network(
            height="750px",
            width="100%",
            bgcolor="#ffffff",
            font_color="black"
        )
        self.net.force_atlas_2based()  # 레이아웃 안정화

        # 기본 physics & layout 옵션 (겹침 방지 + 균형 배치)
        self.net.set_options("""
{
  "physics": {
    "enabled": true,
    "repulsion": {
      "nodeDistance": 250,
      "centralGravity": 0.3,
      "springLength": 150,
      "springStrength": 0.05
    }
  },
  "layout": {
    "improvedLayout": true
  }
}
""")


    def add_node(self, node_id, label, node_type):
        color_map = {
            "paper": "#1f77b4",     # 파랑
            "code": "#2ca02c",      # 초록
            "dataset": "#ff7f0e"    # 주황
        }
        shape_map = {
            "paper": "ellipse",
            "code": "box",
            "dataset": "diamond"
        }
        self.net.add_node(
            node_id,
            label=label,
            color=color_map.get(node_type, "gray"),
            shape=shape_map.get(node_type, "ellipse")
        )

    def add_edge(self, src, dst, label=None):
        self.net.add_edge(src, dst, label=label)

    def show(self, path="outputs/network.html"):
        # 출력 폴더 자동 생성
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # notebook 모드 끄고 HTML 저장
        self.net.write_html(path, notebook=False)
        print(f"Graph saved to {path}")

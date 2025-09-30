import os
from pyvis.network import Network

class Visualizer:
    def __init__(self, height="750px", width="100%", bgcolor="#ffffff", font_color="black"):
        # 네트워크 기본 설정
        self.net = Network(height=height, width=width, bgcolor=bgcolor, font_color=font_color)
        self.net.force_atlas_2based()

    def add_node(self, node_id, label, node_type):
        color_map = {"paper": "#1f77b4", "code": "#2ca02c", "dataset": "#ff7f0e"}
        shape_map = {"paper": "ellipse", "code": "box", "dataset": "diamond"}
        self.net.add_node(
            node_id,
            label=label,
            color=color_map.get(node_type, "gray"),
            shape=shape_map.get(node_type, "ellipse"),
            size=20 if node_type == "paper" else 15,
            title=f"{node_type.upper()} | {label}"  # hover 시 툴팁
        )

    def add_edge(self, src, dst, label=None):
        self.net.add_edge(src, dst, label=label)

    def show(self, path="outputs/graphs/network.html"):
        # 출력 폴더 자동 생성
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # 👇 안정된 간격 (너무 길지 않게 + 겹침 최소화)
        self.net.repulsion(
            node_distance=350,     # 적당한 노드 간 거리
            central_gravity=0.25,  # 중심으로 살짝 강하게 당김
            spring_length=200,     # 연결 길이 짧게
            spring_strength=0.03   # 당기는 힘 강화
        )

        self.net.write_html(path, notebook=False)
        print(f"Graph saved to {path}")

    def save_json(self, path="outputs/graphs/network.json"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.net.save_graph(path)
        print(f"Graph JSON saved to {path}")
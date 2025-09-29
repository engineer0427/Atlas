from atlas.viz.visualizer import Visualizer

def main():
    viz = Visualizer()

    # 최소 노드 2개 + 엣지 1개
    viz.add_node("paper1", "ResNet Paper", "paper")
    viz.add_node("code1", "ResNet Code", "code")
    viz.add_edge("paper1", "code1", label="implements")

    # 저장
    viz.show("outputs/example02.html")

if __name__ == "__main__":
    main()
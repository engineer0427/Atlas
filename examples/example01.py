from atlas.viz.visualizer import Visualizer

def main():
    viz = Visualizer()

    # 노드 추가 (타입별)
    viz.add_node("paper1", "ResNet Paper", "paper")
    viz.add_node("code1", "ResNet GitHub", "code")
    viz.add_node("dataset1", "ImageNet", "dataset")

    viz.add_node("paper2", "ViT Paper", "paper")
    viz.add_node("code2", "ViT GitHub", "code")
    viz.add_node("dataset2", "CIFAR-100", "dataset")

    # 엣지 추가
    viz.add_edge("paper1", "code1", label="implements")
    viz.add_edge("paper1", "dataset1", label="uses")
    viz.add_edge("paper2", "code2", label="implements")
    viz.add_edge("paper2", "dataset2", label="uses")

    # cross link
    viz.add_edge("code2", "dataset1", label="transfer")

    # 결과 출력
    viz.show("outputs/example01.html")

if __name__ == "__main__":
    main()

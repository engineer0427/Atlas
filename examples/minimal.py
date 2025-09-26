from atlas import Atlas, Visualizer

def main():
    # Atlas 초기화
    atlas = Atlas()

    # 노드 추가 (논문 + 코드 저장소)
    paper = atlas.add_node(
        "Paper", "resnet2015",
        title="ResNet Paper",
        year=2015,
        url="https://arxiv.org/abs/1512.03385"
    )
    repo = atlas.add_node(
        "CodeRepo", "resnet-code",
        name="ResNet GitHub",
        url="https://github.com/keras-team/keras"
    )

    # 두 노드 연결
    atlas.add_edge(paper, repo, etype="IMPLEMENTS")

    # 그래프 시각화
    viz = Visualizer(atlas.store)
    out_html = viz.show(out_html="outputs/minimal_graph.html")
    print(f"Graph saved to {out_html}")

if __name__ == "__main__":
    main()

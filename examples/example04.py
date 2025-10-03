from atlas.ingest.arxiv import ArxivIngestor
from atlas.viz.visualizer import Visualizer

def main():
    # 1. arXiv 논문 수집
    ing = ArxivIngestor()
    papers = ing.fetch_papers("ResNet", max_results=5)

    # 2. 시각화 준비
    viz = Visualizer()

    # 3. 논문 노드 추가
    for i, paper in enumerate(papers, 1):
        node_id = f"paper{i}"
        viz.add_node(node_id, paper["title"], "paper")

    # 4. (예시) 논문들끼리 임의 연결
    for i in range(1, len(papers)):
        viz.add_edge(f"paper{i}", f"paper{i+1}", label="related")

    # 5. 결과 출력
    viz.show("outputs/example04.html")
    print("✅ Visualization saved to outputs/example04.html")

if __name__ == "__main__":
    main()

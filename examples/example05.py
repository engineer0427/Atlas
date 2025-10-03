from atlas.ingest.arxiv import ArxivIngestor
from atlas.viz.visualizer import Visualizer

def main():
    # 1. arXiv 논문 수집
    ing = ArxivIngestor()
    papers = ing.fetch_papers("ResNet", max_results=5)

    # 2. 시각화 준비
    viz = Visualizer()

    # 3. 논문 + 속성 노드 추가
    for i, paper in enumerate(papers, 1):
        paper_id = f"paper{i}"
        viz.add_node(paper_id, paper["title"], "paper")

        # 키워드 추출 (논문 요약 기반)
        keywords = [w for w in paper["summary"].split() if len(w) > 5][:3]  # 상위 3개 키워드
        for kw in keywords:
            kw_id = f"kw_{i}_{kw.lower()}"
            viz.add_node(kw_id, kw, "dataset")   # dataset 타입 노드로 표시
            viz.add_edge(paper_id, kw_id, label="has keyword")

        # (옵션) 논문 제목 기반 "코드 저장소" 가상 노드
        code_id = f"code{i}"
        viz.add_node(code_id, f"{paper['title']} Code", "code")
        viz.add_edge(paper_id, code_id, label="implements")

    # 4. 결과 저장
    viz.show("outputs/example05.html")
    print("✅ End-to-end visualization saved to outputs/example05.html")

if __name__ == "__main__":
    main()

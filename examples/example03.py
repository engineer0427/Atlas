from atlas.ingest.arxiv import ArxivIngestor

def main():
    ingestor = ArxivIngestor()
    results = ingestor.fetch_papers("ResNet", max_results=3)

    for i, paper in enumerate(results, 1):
        print(f"[{i}] {paper['title']}")
        print(f"Link: {paper['link']}")
        print(f"Summary: {paper['summary'][:200]}...\n")

if __name__ == "__main__":
    main()

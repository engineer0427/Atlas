
from atlas import Atlas, NodeType

atlas = Atlas(name="demo")

# 1) 노드 생성
p1 = atlas.ingest.paper("resnet2015", title="ResNet (2015)", url="https://arxiv.org/abs/1512.03385", year=2015)
d1 = atlas.ingest.dataset("imagenet", name="ImageNet", url="https://www.image-net.org/")
r1 = atlas.ingest.repo("resnet-impl", name="ResNet PyTorch Impl", url="https://github.com/user/resnet")

p2 = atlas.ingest.paper("resnet2016", title="ResNet (2016)", url="https://arxiv.org/abs/1512.03385", year=2016)
d2 = atlas.ingest.dataset("imagenet", name="ImageNet", url="https://www.image-net.org/")
r2 = atlas.ingest.repo("resnet-impl", name="ResNet PyTorch Impl", url="https://github.com/user/resnet")

# 2) 링크
atlas.link.uses(r1, d1)
atlas.link.implements(r1, p1)
atlas.link.relates(p1, d1)
atlas.link.cites(p1, p1)  # 예시(자기 인용은 흔치 않지만 형태만 시연)

atlas.link.uses(r2, d2)
atlas.link.implements(r2, p2)
atlas.link.relates(p2, d2)
atlas.link.cites(p2, p1)

# 3) 쿼리
center = p1
sub = atlas.query.neighborhood(center, depth=2)

# 4) 시각화 + 리포트
html_path = atlas.viz.show(subgraph=sub, out_html="outputs/quickstart_graph.html")
md_path = atlas.export.report(subgraph=sub, path="outputs/quickstart_report.md", title="Atlas Quickstart")

print("Graph HTML:", html_path)

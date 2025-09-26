# Atlas Quickstart

Generated: 2025-09-26 17:22:45

## Nodes
- **ResNet (2015)** (Paper) https://arxiv.org/abs/1512.03385
- **ImageNet** (Dataset) https://www.image-net.org/
- **ResNet PyTorch Impl** (CodeRepo) https://github.com/user/resnet
- **ResNet (2016)** (Paper) https://arxiv.org/abs/1512.03385

## Edges
- Paper:resnet2015 --RELATES_TO--> Dataset:imagenet
- Paper:resnet2015 --CITES--> Paper:resnet2015
- CodeRepo:resnet-impl --USES--> Dataset:imagenet
- CodeRepo:resnet-impl --IMPLEMENTS--> Paper:resnet2015
- CodeRepo:resnet-impl --IMPLEMENTS--> Paper:resnet2016
- Paper:resnet2016 --RELATES_TO--> Dataset:imagenet
- Paper:resnet2016 --CITES--> Paper:resnet2015
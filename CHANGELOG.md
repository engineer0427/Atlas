# Changelog

## [0.2.8] - 2025-10-02
### Added
- GitHub Sponsors 지원을 위한 `.github/FUNDING.yml` 추가
- 프로젝트 후원 활성화 (계좌 및 세금 양식 등록 완료)
- README 상단에 Atlas 배너 이미지(`docs/AtlasImage.png`) 및 Sponsor 버튼 추가

### Changed
- 프로젝트 소개 문서(README.md) 개선: 브랜드 아이덴티티 강화 및 후원 링크 노출


## [0.2.7] - 2025-10-01
### Added
- '.github/FUNDING.yml' 추가 -> Github sponsors 버튼 활성화

## [0.2.6] - 2025-09-30
### Changed
- 겹쳐짐 개선

## [0.2.5] - 2025-09-29
### Changed
- Visualizer 기본 옵션 개선 (노드 겹침 완화, 더 유연한 인터랙션 유지)
- 새로운 예제 `example01, example02'

## [0.2.4] - 2025-09-28
### Added
- docs/DEVELOPER_GUIDE.md 문서 추가

## [0.2.3] - 2025-09-28
### Added
- CHANGELOG.md 파일 추가, 버전별 변경 이력 기록 시작

### Fixed
- 개발 환경에서 패키지 경로 꼬임 문제 재점검 및 정리

---

## [0.2.2] - 2025-09-28
### Fixed
- pyproject.toml 버전 번호를 0.1.0 → 0.2.2로 수정
- 최신 코드/문서 반영

---

## [0.2.1] - 2025-09-27
### Added
- Full API import style 지원 (`from atlas import Atlas, Ingestor, Linker, Visualizer`)
- 예제 `examples/minimal.py` 추가

### Fixed
- ImportError 문제 해결 (Ingestor/Linker 모듈 import 구조 정리)
- __init__.py 개선 (lazy loading)으로 안정적인 import 지원

---

## [0.1.0] - 2025-09-25
### Added
- Atlas 초기 구조 생성
- quickstart 예제 포함 (논문-코드 네트워크 그래프/리포트 생성)

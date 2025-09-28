# Atlas Developer Guide

이 문서는 Atlas 프레임워크 개발 및 릴리스 과정을 정리한 가이드입니다.  
개발, 버전 관리, 릴리스를 일관된 루틴으로 관리할 수 있도록 작성되었습니다.

---

## 🛠 개발 환경 준비
1. 저장소 클론
   ```bash
   git clone https://github.com/engineer0427/Atlas.git
   cd Atlas
   ```

2. (선택) 가상환경 생성
   ```bash
   python -m venv myenv
   .\myenv\Scripts\Activate.ps1
   ```

3. 개발 모드 설치
   ```bash
   pip install -e .
   ```

4. 예제 실행
   ```bash
   python -m examples.minimal
   ```

---

## 🚀 새 버전 릴리스 절차

1. 코드/문서 수정
   - `src/atlas/` 내부 코드 개선
   - `README.md`, `docs/` 문서 업데이트

2. 버전 업데이트
   - `pyproject.toml` → `version = "0.x.x"`
   - `CHANGELOG.md` → 새 버전 항목 추가

3. 커밋
   ```bash
   git add .
   git commit -m "chore: bump version to v0.x.x"
   ```

4. 태그 생성
   ```bash
   git tag v0.x.x
   ```

5. 원격 저장소 푸시
   ```bash
   git push origin main
   git push origin v0.x.x
   ```

6. GitHub Release 작성
   - Tag: `v0.x.x`
   - Title: `Atlas v0.x.x`
   - Description: CHANGELOG.md의 해당 버전 내용 붙여넣기

---

## 📚 참고 명령어

- 태그 확인
  ```bash
  git tag
  ```

- 원격 확인
  ```bash
  git remote -v
  ```

- 최신 태그 push
  ```bash
  git push origin --tags
  ```

- import 경로 확인
  ```bash
  python -c "import atlas, inspect; print(atlas.__file__)"
  ```

---

## ✅ 관리 루틴 요약
1. 코드/문서 수정  
2. 버전 업 (`pyproject.toml`, `CHANGELOG.md`)  
3. 커밋 → 태그 → 푸시  
4. GitHub Release 작성  

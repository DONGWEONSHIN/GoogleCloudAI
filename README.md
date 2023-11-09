# GoogleCloudAI
Google Cloud 기반 인공지능 개발자 과정

### git 토근 변경시
- git remote set-url origin https://\<username\>:\<token\>@github.com/...git

### git을 pull 하기전에 변경사항이 있는지 확인 함
- git fetch origin main

### git을 리셋 함
- git reflog
- git reset --hard HEAD@{16}

### git 폴더 전체 업로드하기
- git add .
- git commit -m 'log'
- git push origin main

### git 폴더 업로드시 에러날때
- rm -rf .git / 제대로 추가 안된 폴더의 .git 폴더 제거
- git rm -rf --cached / 해당폴더를 실행하여 git cache를 제거
- git add . / 폴더를 git에 추가

### git 한글 깨짐 현상
- git config --global core.quotepath false






### 기본 패키지
- conda install -y jupyter ipykernel pandas matplotlib seaborn xlrd openpyxl

### anaconda / packages / pyqt
- conda install -c anaconda pyqt

### anaconda / packages / graphviz
- conda install -c anaconda graphviz

### 추가 패키지
- conda install -c conda-forge scikit-learn xgboost lightgbm catboost

### conda-forge / packages / graphviz
- conda install -c conda-forge graphviz

### conda-forge / packages / missingno
- conda install -c conda-forge missingno

### conda-forge / packages / opencv
- conda install -c conda-forge opencv




### update the conda package manager to the latest version
- conda update conda
### use conda to update Anaconda to the latest version
- conda update anaconda
### updates all packages in the current environment to the latest version
- conda update --all
### update other environments
- conda update -n myenv --all




### matplotlib 한글화
- !pip install koreanize_matplotlib

### VS Code Marketplace
- Python
- Jupyter
- Rainbow CSV
- Excel Viewer
- Python Extension Pack
- GitLens — Git supercharged




### jupyter 시작시
- jupyter notebook
- jupyter lab


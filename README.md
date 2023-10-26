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





### conda 패키지 설치 (초반 필수 패키지)
- conda install -y jupyter ipykernel pandas matplotlib seaborn xlrd openpyxl scikit-learn

### pyqt5 conda install
- conda install -c anaconda pyqt

### Graphviz is an open source graph visualization software
- conda install -c anaconda graphviz

### conda-forge / packages / xgboost
- conda install -c conda-forge xgboost

### conda-forge / packages / lightgbm
- conda install -c conda-forge lightgbm

### conda-forge / packages / catboost
- conda install -c conda-forge catboost

### update the conda package manager to the latest version
- conda update conda
### use conda to update Anaconda to the latest version
- conda update anaconda
### updates all packages in the current environment to the latest version
- conda update --all
### update other environments
- conda update -n myenv --all



### VS Code Marketplace
- Python
- Jupyter
- Rainbow CSV
- Excel Viewer
- Python Extension Pack
- GitLens — Git supercharged
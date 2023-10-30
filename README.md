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



- conda install -y jupyter ipykernel notebook numpy pandas matplotlib seaborn xlrd openpyxl scikit-learn

### anaconda / packages / jupyter
- conda install -c anaconda jupyter

### anaconda / packages / ipykernel
- conda install -c anaconda ipykernel

### anaconda / packages / numpy 
- conda install -c anaconda numpy

### anaconda / packages / pandas
- conda install -c anaconda pandas

### anaconda / packages / matplotlib
- conda install -c anaconda matplotlib

#### conda-forge / packages / matplotlib
- conda install -c conda-forge matplotlib

### anaconda / packages / seaborn
- conda install -c anaconda seaborn

### anaconda / packages / xlrd
- conda install -c anaconda xlrd

#### conda-forge / packages / xlrd
- conda install -c conda-forge xlrd

### anaconda / packages / openpyxl
- conda install -c anaconda openpyxl

#### conda-forge / packages / openpyxl
- conda install -c conda-forge openpyxl

### anaconda / packages / scikit-learn
- conda install -c anaconda scikit-learn

### anaconda / packages / notebook
- conda install -c anaconda notebook

#### conda-forge / packages / notebook
- conda install -c conda-forge notebook

### anaconda / packages / pyqt
- conda install -c anaconda pyqt

### anaconda / packages / graphviz
- conda install -c anaconda graphviz

#### conda-forge / packages / graphviz
- conda install -c conda-forge graphviz

- conda install -c conda-forge -y xgboost lightgbm catboost missingno

### conda-forge / packages / xgboost
- conda install -c conda-forge xgboost

### conda-forge / packages / lightgbm
- conda install -c conda-forge lightgbm

### conda-forge / packages / catboost
- conda install -c conda-forge catboost

### conda-forge / packages / missingno
- conda install -c conda-forge missingno







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

### other python 3.8
- pip install numpy pandas matplotlib seaborn scikit-learn notebook
- jupyter lab


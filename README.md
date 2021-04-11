## medical-data-API

### 사용한 프레임워크

- Django



### 실행방법

1. 해당 레포를 clone 받습니다.

   ```bash
   $ git clone https://github.com/chshin0225/medical-data-API.git
   ```

   

2. python 가상환경을 생성하고 requirements.txt에 명시된 패키지들을 설치합니다.

   ```bash
   $ python -m venv 가상환경이름
   $ source 가상환경이름/bin/activate
   $ pip install -r requirements.txt
   ```

   

3. `manage.py` 가 있는 루트 폴더에서 django 프로젝트를 실행합니다.

   ```bash
   $ python manage.py runserver
   ```



### 구현된 API에 대한 설명

- 프로젝트를 실행 후 `http://127.0.0.1:8000/swagger/`에서 swagger 문서를 확인하거나 [API 정리 구글시트](https://docs.google.com/spreadsheets/d/1pN6DQ8YzeT1kadiGcOCecUPsr9BGkUUWsAjcCVdSlbE/edit?usp=sharing)를 참고해주시길 바랍니다.



### 과제의 우선순위 선정

- 가장 먼저 pgAdmin4를 이용해 DB에 접속해서 데이터를 직접 살펴보면서 데이터 간의 관계를 파악했습니다.
- 모든 데이터를 다루기 위해서는 concept 데이터에 대한 이해가 우선되었어야했기 때문에 concept 테이블을 이용한 통계 기능들의 구현을 우선시했습니다.
- 그 다음으로는 person 테이블에 있는 데이터를 기반으로 한 기능들을 구현했으며, 방문 데이터와 관련된 기능들은 가장 마지막에 했습니다.
- 각 테이블을 조회하는 API 구현을 가장 마지막에 했는데, pagination까지는 했으나 concept id와 concept name 매칭, 그리고 특정 컬럼 검색 기능은 구현 못했습니다. 만약 구현을 한다면 django ORM을 이용해서 구현했을 것입니다.
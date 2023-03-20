# 한국의 '온라인 성지' 개념에 관한 연구
이 저장소는 온라인 성지 개념에 관한 연구에서 활용된 기술적인 정보들을 공유하기 위한 곳입니다.<br/>
발표 예정인 논문의 타이틀은 <b>"한국의 ‘온라인 성지(聖地)’ 개념의 출현과 진화: ‘쿠키닷컴’ 게시물 댓글 텍스트 분석을 중심으로"</b>입니다.<br/>
서지 정보는 논문 출판 이후에 업데이트할 예정입니다.<br/>
<br/>
## 사용 데이터<br/>
<p>디시인사이드 Hit갤의 '온라인 성지'로 여겨지는 게시물의 댓글과 Hit갤의 주요 인기 게시물</p>
<br/>

## 댓글 수집 방법
<p>python의 selenium을 이용하여 댓글을 스크래핑함</p>
<br/>

## 댓글 분석 방법<br/>
<p>python의 konlpy의 OKT 형태소 분석기</p>
<br/>

## 분석 내용
'쿠키닷컴' 게시물의 댓글에 연도별 빈도값 높은 단어들 추출, 연도별 댓글의 TF-IDF 가중치 부여<br/>
디시인사이드 Hit갤의 주요 게시물(조회수, 추천수, 댓글수 상위) 12건에 대한 '성지' 및 '-해주세요' 사용 빈도 및 시기 확인

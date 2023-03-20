# 한국의 '온라인 성지' 개념에 관한 연구
이 저장소는 온라인 성지 개념에 관한 연구에서 활용된 기술적인 정보들을 공유하기 위한 곳입니다.<br/>
발표 예정인 논문의 타이틀은 <b>"한국의 ‘온라인 성지(聖地)’ 개념의 출현과 진화: ‘쿠키닷컴’ 게시물 댓글 텍스트 분석을 중심으로"</b>입니다.<br/>
서지 정보는 논문 출판 이후에 업데이트할 예정입니다.<br/>
<br/>
## 사용 데이터<br/>
<p>디시인사이드 Hit갤의 '온라인 성지'로 여겨지는 게시물의 댓글과 Hit갤의 주요 인기 게시물</p>

<a href="https://gall.dcinside.com/board/view/?id=hit&no=12" target="_blank">오늘 산 중저가형 모델 싸게 팝니다..</a>(쿠키닷컴 게시물)
<br/><a href="https://gall.dcinside.com/board/view/?id=hit&no=13" target="_blank">(엑스브이-3) 내 자취방에서 옹달샘 발견!!!!!!!!!!!</a>(옹달샘)
<br/><a href="https://gall.dcinside.com/board/view/?id=hit&no=14" target="_blank">이 사진이 실제인지 합성인지 판단 부탁드립니다.</a>(사실? 합성?)
<br/><a href="https://gall.dcinside.com/board/view/?id=hit&no=1" target="_blank">지하철 시체.. ㅡㅡa</a>(지하철 시체)
<br/><a href="https://gall.dcinside.com/board/view/?id=hit&no=162" target="_blank">아이구 구엽소 욘석.</a>(개죽이)
<br/><a href="https://gall.dcinside.com/board/view/?id=hit&no=163" target="_blank">경고문이오 쌔우다 이후 신선한 충격이 될 듯 하오</a>(방법)
<br/><a href="https://gall.dcinside.com/board/view/?id=hit&no=1554" target="_blank">[ 우리는 무적의 솔로부대다 ] (Scroll & BGM)</a>(솔로부대)
<br/><a href="https://gall.dcinside.com/board/view/?id=kimsungmo&no=97157" target="_blank">[공지]근성갤을 야갤의 식민지로 선포한다?</a>(지귀글)
<br/><a href="https://gall.dcinside.com/board/view/?id=hit&no=6417" target="_blank">빠삐놈병神디스코믹스 (feat. 엄기뉴 전스틴 디제이쿠 이효리 한가인)</a>(빠삐놈)
<br/><a href="https://gall.dcinside.com/board/view/?id=yeonpyeongdo&no=5798" target="_blank">야 우리민족끼리 사이트 털면안되냐??</a>(우리민족끼리)
<br/><a href="https://gall.dcinside.com/board/view/?id=hongjinho&no=37461" target="_blank">안녕하세요~~ㅎㅎ 홍진홉니다~~</a>(홍진호)
<br/><a href="https://gall.dcinside.com/board/view/?id=comedy_new1&no=440917" target="_blank">2015내방명록 아다뚫는사람</a>(방명록 아다)
<br/><a href="https://gall.dcinside.com/board/view/?id=hit&no=13578" target="_blank">MEGAL WOMAN(스압,스포)</a>(메갈여인)
<br/><a href="https://gall.dcinside.com/board/view/?id=hit&no=14047" target="_blank">스폰지밥 뉴 애피소드 1~30 (완)(스압)</a>(스폰지밥)
<br/><a href="https://gall.dcinside.com/board/view/?id=hit&no=16667" target="_blank">30만원 생활비 일본인 와이프가 차려주는 저녁밥.JPG</a>(30만원 생활비 일본 아내)
<br/>

## 댓글 수집 방법
<p>python의 selenium을 이용하여 댓글을 스크래핑함</p>
<br/>

## 댓글 분석 방법<br/>
<p>python의 konlpy의 OKT 형태소 분석기</p>
"open-korean-text”, https://github.com/open-korean-text/open-korean-text
<br/>

## 분석 내용
'쿠키닷컴' 게시물의 댓글에 연도별 빈도값 높은 단어들 추출, 연도별 댓글의 TF-IDF 가중치 부여<br/>
디시인사이드 Hit갤의 주요 게시물(조회수, 추천수, 댓글수 상위) 12건에 대한 '성지' 및 '-해주세요' 사용 빈도 및 시기 확인

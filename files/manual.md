#### 소개
   HDHomerun은 기본적으로 외부에서 연결할 수 없음.   
   동일 네트워크로 인식하는 방법을 통해 가능하긴 하나 대역폭이 10MB/s 이상이기 때문에 연결이 원할하지 않음.   
   외부 사용을 위해 TVHeadend가 대표적으로 이용되고 있으나 설정이 쉽지 않음.   
   본 플러그인은 동일한 기능을 심플하게 사용 가능하게 하여 OTT에서 제공하지 않는 국대 축구 라이브 경기 같은 것을 간단히 외부에서 시청하기 위해 Play 기능을 추가함.  


#### HDHomerun 스캔 프로그램 실행
  - 윈도우만 가능   
    <img src="https://i.imgur.com/G3WZcmJ.png" width="50%" height="50%" />   
  - 파일위치 : /data/plugins/hdhomerun/bin/hdhomerun_scan.exe   
  - 플러그인 - 설정 - 자동&기타 - 스캔 프로그램 실행  에서 실행 가능.   
  - 프로그램 하단 ID로 HDHomerun 기기 IP 확인.   
  - 스캔시작 버튼을 눌러 스캔 시작.   
  - tvheadend 파일생성, SJVA 파일 생성 버튼 클릭.   
    <img src="https://i.imgur.com/ma2U4Ti.png" width="50%" height="50%" />   
  - hdhomerun.m3u, hdhomerun.txt, kr-VSBXX-QAMXX 파일 생성 확인.   
  - m3u파일을 편집기에서 열어서 재생 주소 뒤에 .mpeg 제거한 후 팟플레이어 등에서 재생 확인.   
    (구형 펌웨어는 .mpeg 제거 불필요)   
   <img src="https://i.imgur.com/jg6CCyL.png" width="50%" height="50%" />   
  - 재생이 안 되는 경우 프로그램 맨 오른쪽 버튼 '기기 kr-cable 설정' 클릭   


#### 플러그인 설정

  - 채널 - 데이터 파일에서 읽기 버튼 클릭. 
  - 채널 로딩 후 사용, 미사용 체크.   
  - 전체 EPG 채널 매치 버큰 클릭으로 EPG 연결.   
  - 매치가 안 되는 경우 EPG 검색을 수정하여 개별 EPG 찾기 버큰 클릭.   
  - 그룹별 정렬, ⬆️, ⬇️, 현재 순서대로 채널 번호 부여 버튼 등을 이용하여 채널 순서 편집.   
    <img src="https://i.imgur.com/mWAip4Y.png" width="50%" height="50%" />   
    <img src="https://i.imgur.com/8YHHZIw.png" width="50%" height="50%" />   


#### Play
  - 내부 네트워크는 HDHomerun 주소를 바로 이용   
  - 외부 네트워크, WEB은 트랜스코딩 사용   
  - 설정 - 트랜스 코딩 명령   
    ```
    ffmpeg -loglevel quiet -i {URL} -vcodec libx264 -vf scale=1080:720 -c:a aac -b:a 64k -f mpegts -tune zerolatency pipe:stdout
    ```
    * ffmpeg 경로 설정
    * `-loglevel quiet -i {URL}` 필수
    * 끝부분 `-tune zerolatency pipe:stdout` 필수   
    * h264, aac 설정은 거의 필수이고 scale 정도 변경하여 사용 권장.   
  - 웹 PLAY
    * 트랜스코딩 기본 사용.
    * 이전 버전에서는 mpegts 컨테이너 재생할 수 없었으나 [mpegts.js](https://github.com/xqq/mpegts.js) 사용.   
  - LOCAL PROGRAM
    * FF가 설치된 곳의 프로그램을 실행. 내부 네트워크이기 때문에 HDhomerun 주소 바로 사용.   
  - 브라우저 확장
    * 브라우저 확장 프로그램 사용하여 링크를 우클릭하여 사용. Potplayer, VLC 등   
      - [Potplayer 확장](https://chromewebstore.google.com/detail/potplayer-youtube-shortcu/cfdpeaefecdlkdlgdpjjllmhlnckcodp?hl=ko&utm_source=ext_sidebar)
      - <img src="https://i.imgur.com/24QEIzA.png" width="50%" height="50%" />
    * 다른 네트워크일 경우 TRANS 이용.   
  - 사용자 링크
    * 모바일 기기 앱 바로열기 용도로 앱링크, 딥링크 설정 용도. 안드로이드 nplayer에서만 확인.   
 

#### Plex 연결
  - Plex DVR 설정에서 HDHomerun 기기를 기본적으로 인식하나 주파수 범위가 한국상황에 맞지 않음.   
   <img src="https://i.imgur.com/XBA9FrY.png" width="50%" height="50%" />   
   왼쪽이 기본인식, 가운데가 Plex Proxy 등록 후 인식.   
   설정 - API 에 있는 Proxy주소와 XMLTV 주소 사용.   
   트랜스 코딩은 Plex Server 에서 실행.   
   <img src="https://i.imgur.com/1tAlBUi.png" width="50%" height="50%" />


# 한눈 Android 공통 템플릿 규격 (초안)

기준 프로젝트: https://github.com/softm/softm.android.gagyebu

## 공통 기능 및 기준 버전
- Android Java 17 / compileSdk 36 / targetSdk 36 / minSdk 24
- androidx.webkit:webkit:1.17.1
- com.google.android.play:app-update:2.1.0
- com.google.android.gms:play-services-ads:25.5.0
- com.google.android.ump:user-messaging-platform:4.0.0
- com.kakao.adfit:ads-base:3.23.1

## 업데이트 정책
- Google Play 설치 앱: Flexible Update 기본, 긴급 업데이트에 한해 Immediate Update
- 다운로드 완료 상태에서 사용자에게 설치 재시작 안내
- 앱 재개 시 진행 중 업데이트 재개 처리
- Play 외 설치 또는 Play Store 미지원 환경에서는 실패하지 않고 안내
- 웹 콘텐츠 수정은 웹 배포로 반영, Android 네이티브 변경은 새 버전 배포 필요

## 광고 정책
- 하단 네이티브 광고 우선, 배너 폴백
- 종료 확인 다이얼로그 광고 슬롯, 광고 미로드 시 정상 종료 가능
- UMP 동의 및 개인정보 옵션 제공; 법적 동의 흐름을 광고 허용 팝업으로 대체하지 않음
- 테스트 빌드는 Google 테스트 광고 ID만 사용
- 릴리스 광고 ID는 앱별 설정; 기존 가계부 앱 ID 복사 금지
- 광고 표시 여부 및 시점은 Google 정책 준수

## 신규 앱별 변경 항목
- applicationId / namespace / 앱 이름 / 아이콘
- WebView 시작 URL 및 허용 도메인
- AdMob 앱 ID 및 광고 단위 ID / AdFit ID
- 알림·위치·카메라·파일 선택 등 필요한 권한
- Play Console 앱 등록, 서명 키, 버전 코드

## 운영 규칙
- 공통 템플릿 저장소는 별도로 생성하고 이 문서의 기준을 이관한다.
- 기존 앱을 복사한 뒤 광고 ID, 서명정보, 고유 API 키를 반드시 제거한다.
- 공통 모듈은 버전 관리하며 앱별 업그레이드 PR을 통해 배포한다.
- Android 빌드·Lint·기본 UI 테스트 후 기능 완료 처리한다.
- 실제 Google Play 인앱 업데이트는 내부 테스트 트랙에서 별도 검증한다.

## 진료비한눈 적용
- Android 앱 후보 저장소: softm/medicalpricehannun.android (미생성)
- WebView URL: https://softm.github.io/medicalpricehannun/
- 실제 배포 URL 및 API 데이터 수집 정상 여부는 별도 검증

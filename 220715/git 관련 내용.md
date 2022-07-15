# README.MD

### 여기가 저장소가 될 공간입니다.

working directory 내가 작업하고 잇는 곳

staging area 커밋으로 남기고싶은 특정 버전으로 관리하고 싶은 파일이 있는곳

repository 커밋들이 저장되는 곳





git status : 현재 git으로 관리되고 있는 파일들의 상태를 알려주는 명령어

git add. : 추적되ㅣ지 않은 모든 파일과 추적하고 있는 파일 중 수정된 파일을 모두  staging area에 올린다.

git commit -m"하고싶은말 (최대한 자세하게)"

git remote add origin "깃허브 레포지토리 url" : 어떤 원격 저장소에 깃 작업을 할건지 등록

git push origin master : 내가 지금까지 커밋한 내용을 원격 저장소에 업데이트

git clone "깃허브 레포지토리 url" : 해당 원격 저장소에 있는 파일들 현재 작업 영역으로 복사

commit 하기 전에 꼭 pull을 통해서 원격 레포지토리와 로컬 레포지토리의 정보를 최신화해야 함!!!!

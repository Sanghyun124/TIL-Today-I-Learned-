# git undoing(작업 되돌리기)
- working directory 작업단계  
- staging area 작업단계
- repository 작업단계  

### Working Directory
수정한 파일 내용을 이전 커밋 상태로 되돌리기  
- git restore

### staging area
staging area에 반영된 파일을 working 으로 되돌리기
- git rm --cached
- git restore --staged

### repository
커밋을 완료한 파일을 staging area로 되돌리기
- git commit --amend

<hr>

## git restore
- working directory에서 수정한 파일을 수정 전(직전커밋)으로 되돌리기
- 이미 버전 관리가 되고 있는 파일만 되돌리기 가능
- git restore를 통해 되돌리면, 해당 내용을 복원할 수 없으니 주의할 것!
- git restore {파일 이름}

<hr>
<br>

# staging area에 있는 파일을 되돌리기!
- root-commit이 없는 경우 : git rm --cached
- root-commit이 있는 경우 : git restore --cached

## git rm --cached
- staging에 있는 파일을 working directory로 돌아옴

## git restore --cached
- root-commit이 있는 경우에 사용

# repository 작업 되돌리기!
 - 커밋을 완료한 파일을 staging area로 되돌리기
 - staging area에 새로운 내용이 없다면 직전 커밋의 메시지만 수정
 - staging area에 새로운 내용이 있다면 직전 커밋을 덮어쓰기
 - 이전 커밋을 완전히 고쳐서 새 커밋으로 변경하므로, 이전 커밋은 일어나지 않은 일이 되며 히스토리에도 남지 않음!! 주의할 것!!!!!!!

 # Vim 사용법
- 입력모드(i) : 문서 편집 기능
- 명령어모드 : 
    - 저장및 종료(:wq)
    - 강제종료(:q!)

<hr>

# git reset & revert

## git reset
- 프로젝트를 특정 커밋 상태로 되돌림
- 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐
- git reset [옵션] {커밋 ID}
    - 옵션은 soft, mixed, hard 중 하나를 작성
    - 커밋 ID는 되돌아가고 싶은 시점의 커밋 ID를 작성

## git reset의 세가지 옵션
- --soft
    - 해당 커밋으로 되돌아가고
    - 되돌아간 커밋 이후의 파일들은 Staging Area로 되돌려놓음

- --mixed
    - 해당 커밋으로 되돌아가고
    - 되돌아간 커밋 이후의 파일들은 working directory로 돌려놓음
    - git reset의 기본옵션

- --hard
    - 해당 커밋으로 되돌아가고
    - 되돌아간 커밋 이후의 파일들은 모두 working directory에서 삭제 > 따라서 주의할 것!
    - 기존의 untracked 파일은 사라지지 않고 untracked로 남아있음

## git reflog
- git reset의 hard옵션은 working directory내용까지 삭제하므로 위험할 수 잇음
- git reflog 명령어를 이용하면 reset하기 전의 과거 커밋 내역을 모두 조회 가능
- 이후 해당 커밋으로 reset하면 hard옵션으로 삭제된 파일도 복구 가능

# git revert
- 과거를 없었던 일로 만드는 행위, 이전 커밋을 취소한다는 새로운 커밋을 생성함
- git revert {커밋 ID}
    - 커밋 id는 취소하고 싶은 커밋 id를 작성

# reset VS revert
- <strong>개념적 차이</strong>
    - reset은 커밋 내역을 샂게하는 반면, revert는 새로운 커밋을 생성함
    - revert는 github를 이용해 협업할 때, 커밋 내역의 차이로 인한 충돌 방지 가능

- <strong>문법적 차이</strong>
    - git reset 5sd2f42라고 작성하면 5sd2f42라는 커밋으로 되돌린다는 뜻
    - git revert 5sd2f42라고 작성하면 5sd2f42라는 커밋한개를 취소한다는 뜻  
    (커밋이 취소되었다는 내용의 새로운 커밋을 생성함)


# git Branch
- 브랜치는 나뭇가지라는 뜻으로, 여러 갈래로 작업공간을 나누어 독립적으로 작업 할 수 있도록 도와주는 git의 도구

## 장점
- 브랜치는 독립 공간을 형성하기 때문에 원본에 대해 안전함
- 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함
- git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 차지함

## git branch
- 브랜치의 조회, 생성, 삭제와 관련된 git 명령어
- 조회
    - git branch #로컬 저장소의 브랜치 목록확인
    - git branch -r # 원격 저장소의 브랜치 목록 확인
- 생성
    - git branch {브랜치 이름} # 새로운 브랜치 생성
    - git branch {브랜치 이름} {커밋 ID} # 특정 커밋 기준으로 브랜치 생성
- 삭제
    - git branch -d {브랜치 이름} # 병합된 브랜치만 삭제가능
    - git branch -D {브랜치 이름} # 강제삭제

## git switch
- 현재 브랜치에서 다른 브랜치로 이동하는 명령어
- git switch {브랜치 이름} > 다른 브랜치로 이동
- git switch -c {브랜치 이름} > 브랜치를 새로 생성 및 이동
- git switch -c {브랜치 이름} {커밋 ID} > 특정 커밋 기준으로 브랜치 생성 및 이동

- switch하기 전에, 해당 브랜치의 변경사항을 반드시 커밋해야함을 주의할 것!  
    - 다른 브랜치에서 파일을 만들고 커밋 하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당파일이 그대로 남아있게 됨

## HEAD
- HEAD는 현재 브랜치를 가리키고, 각 브랜치는 자신의 최신 커밋을 가리키므로 결국 HEAD가 현재 브랜치의 최신 커밋을 가리킨다고 할 수 있음
- git log 혹은 cat.git/HEAD를 통해서 현재 HEAD가 어떤 브랜치를 가리키는지 알 수 있음

# git merge
- 분기된 브랜치들을 하나로 합치는 명령어
- master브랜치가 상용이므로, 주로 master 브랜치에 병합
- git merge {합칠 브랜치 이름}
    - 병합하기 전에 브랜치를 합치려고하는, 즉 메인 브랜치로 switch해야함
    - 병합에는 3종류가 존재
        1. Fast-Forward
        2. 3-way Merge
        3. Merge Conflict

## Fast Forward
- 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법
- (master) $ git merge {브랜치 이름}

## 3-way Merge
- 각 브랜치의 커밋 2개와 공통 조상 하나를 사용하여 병합하는 방법
- (master) $ git merge {브랜치 이름}

## merge conflict
- 두 브랜치에서 같은 부분을 수정한 경우, Git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못하여 충돌이 발생했을 때 이를 해결하며 병합하는 방법
- 보통 같은 파일의 같은 부분을 수정했을 때 자주 발생함

# Git workflow
- 브랜치와 원격 저장소를 이용해 협업을 하는 두가지 방법
    - 원격 저장소 소유권이 있는 경우 -> shard repository Model
    - 원격 저장소 소유권이 없는 경우 -> Fork & Pull Model

## Shared Repository Model
- 원격 저장소가 자신의 소유이거나 Collaborator로 등록되어 있는 경우
- master 브랜치에 직접 개발하는 것이 아니라, 기능별로 브랜치를 따로 만들어 개발
- Pull Request를 사용하여 팀원 간 변경 내용에 대한 소통 진행

## Fork & Pull Model
- 오픈소스 프로젝트와 같이, 자신의 소유가 아닌 원격 저장소인 경우
- 원본 원격 저장소를 그대로 내 원격 저장소에 복제(Fork)
- 기능 완성 후 복제한 내 원격 저장소에 Push
- 이후 Pull Request를 통해 원본 원격 저장소에 반영될 수 있도록 요청함

# Git 브랜치 전략!
- 여러 개발자가 브랜치를 생성해 이용하는데 사용하는 전략

## gitlab flow
- github-flow의 배포 이슈를 보완하기 위해 gitlab에서 사용하는 방식
- master 브랜치와 production 브랜치 사이에 pre-production 브랜치를 두어 개발 내용을 바로 반영하지 않고, 배포 시기를 조절함

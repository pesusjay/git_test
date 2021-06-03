# 1. github repository를 만듭니다. 홈화면 좌측에 new해서 만들 수 있음. 
# 2. github reepository를 만들면 첫화면에 가이드 나옴. 이걸 참고하면 좋은데 아래처럼 해보자
# 3. 내가 저장하고싶은 파일들이 있는 폴더안으로 들어간다. 
# 4. terminal을 켜자. 단축키는command+shift+~
# 5. git. init -> 이 폴더가 git에 의하여 통제받을 구역이다라는 것을 의미. 
# 6. git add. -> .은 현재폴더를 의미한다. 즉 git에 반영할 파일들은 이 폴더내의 모든 파일을 의미하게된다.
# 7. git commit -m "first commit" -> 내가 이번 코드를 수정할 때 했던 작업을 자유롭게 넣습니다. 변동사항의 이름표. 변경가능하다.
# 8. git remote add origin [repository 주소].git ->코드를 올릴 주소를 설정하는 과정
# 예시. git remote add origin https://github.com/pesusjay/git_test.git
# 9. git push origin master ->git add . 해서 모인 모든 파일들을 repository에 올림.
# 10. code나 file이 수정되었을대는  6,7,9를 진행한다. 이때 7에서 first commit부분을 내가 한 작업으로 반경하는 것만 다르다. 

print("last dance")
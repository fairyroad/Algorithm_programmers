
    [카카오] 후보키문제

    relation -> [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

    row = 6, col = 4

    tuple = ( )로 둘러쌈 값 and 바꾸는 것 불가

    전체 조합 구하기 -> 유일성 만족하는 경우만 찾음 -> 최소성 만족하지 않으면 제거

    유일성만족하는 경우까지는 내가 했던 방법이랑 같음 ( 각 인덱스에 해당하는 모든 속성들 뽑아서 전체 행의 개수랑 동일한지 check)

    최소성은 unique리스트에서 하나씩 뽑고 교집합을 구해서 길이 비교 -> 길이가 같으면 겹치니까 최소성만족 x -> 제거해야함

    제거방법 1)remove 2)discard -> 지우려는 게 없을 때 remove는 keyerror발생 !! 따라서 discard사용

    교집합 구할때 set() & set() 처럼 intersection을 사용할 수 있음!!

    set은 중복을 제거하는 자료형

    extend는 iterable한 모든 요소를 추가함(리스트를 확장시키는 것!!)


![image](https://user-images.githubusercontent.com/74306759/126262905-c3f2fe79-3324-4122-8918-ce90ed881bb6.png)

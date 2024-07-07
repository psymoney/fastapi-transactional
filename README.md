### 목표: fastapi에서 사용할 수 있는 request 단위의 Transactional 애노테이션 만들기


### 가설
1. sqlalchemy의 async_scoped_session은 task 단위로 Session을 공유한다.
2. FastAPI는 request마다 task를 할당한다.
3. Service 레이어에서 async_scoped_session에 접근하면, 하위 repository에서 공유하는 동일한 Session을 제어할 수 있다.
4. 애노테이션을 통해 로직을 반복되는 서비스 코드에 노출하지 않고 적용하기 
 

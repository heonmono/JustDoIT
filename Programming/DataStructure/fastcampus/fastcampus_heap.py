
# 힙(heap)

'''
힙 : 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리

힙 사용 이유 :
배열에 데이터를 넣고, 최대값 최소값을 찾으려면 O(n)이 걸림
이에 반해, 힙에 데이터를 넣고, 최대 최소값을 찾으면 O(logn)이 걸림
우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용

힙의 구조 - 최대 힙과 최소 힙로 분류
조건 1. 각 노드의 값이 자식 노드보다 크거나 같다 or 반대 -> 최대나 최소가 맨위
     2. 완전 이진트리 형태(왼쪽부터 채워나감)

힙과 이진 탐색 트리의 공통점 차이점
공통점 : 이진트리임
차이점 : 힙은 각 노드의 값이 자식보다 크거나 같음
         이진 탐색은 왼쪽 자식이 가장 작고 그다음 부모 그다음 오른쪽 자식
         힙은 이전 탐색트리 조건이 없음(왼쪽오른쪽의 크기)

        이진탐색트리(탐색) vs 힙(최대,최소)
'''
''' 
규칙
삽입 - 가장 왼쪽 아래부터 넣고 위랑 비교해서 오렬
삭제 - 맨위 삭제, 맨 마지막데이터 넣고 그 아래랑 비교'''

# 힙구현
'''
배열 자료구조
편의를 위해 root노드 인덱스 1
부모 노드 인덱스 = 자식 노드 인덱스 번호//2
왼쪽 자식 노드 = 부모노드 *2
오른쪽 자식 노드 = 부모노드 *2 +1'''


class Heap :
    def __init__(self,data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self,inserted_idx):
        if inserted_idx <= 1 : # 루트노드인지
            return False

        parent_idx = inserted_idx//2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx] : # 부모노드보다 큰지
            return True
        else :
            return False

    def insert(self, data):
        if len(self.heap_array) == 0 :
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        inserted_idx = len(self.heap_array) - 1
        while self.move_up(inserted_idx) : # 위치변화 여부 check
            parent_idx = inserted_idx//2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True

    def move_down(self,poped_idx):
        left_child_popped_idx = poped_idx *2
        right_child_popped_idx = poped_idx *2+1
        # case 1 : 왼쪽 자식 노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array) : # 없는 곳 가르침
            return False
        # case 2 : 오른쪽 자식 노드만 없을 때
        elif right_child_popped_idx >= len(self.heap_array) :
            if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx] :
                return True
            else :
                return False
        # case 3 : 왼쪽 ,오른쪽 자식 모두 있을 때
        else :
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx] :
                if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else :
                if self.heap_array[poped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1] # 마지막 데이터를 위로 보내기
        del self.heap_array[-1]

        poped_idx =1# 밑에꺼와 비교하여 내릴지 말지

        while self.move_down(poped_idx) :
            left_child_popped_idx = poped_idx * 2
            right_child_popped_idx = poped_idx * 2 + 1
            # case 2 : 오른쪽 자식 노드만 없을 때
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[poped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                    poped_idx = left_child_popped_idx
            # case 3 : 왼쪽 ,오른쪽 자식 모두 있을 때
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[poped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                        poped_idx = left_child_popped_idx
                else:
                    if self.heap_array[poped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[poped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[poped_idx]
                        poped_idx = right_child_popped_idx

        return returned_data



heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
heap.pop()
heap.heap_array

heap = Heap(1)
heap.heap_array

'''
힙에서 데이터 삭제 - root 노드 삭제
힙의 시간 복잡도
n개의 노드를 가지는 heap에 데이터 삽입 또는 삭제시, O(logN) 50%씩 감소하기때문에.
'''
# 사칙연산 계산기 제작

class FourCal:

    #add generator
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    # pow added(제곱근 계산이 가능하도록 기능 추가)
    def pow(self):
        result = self.first ** self.second
        return result

    # div fixed(self.second 값이 0일 때 결과를 0으로 표시하도록 수정)
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
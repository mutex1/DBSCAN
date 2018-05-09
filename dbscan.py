import sys

def getDataSet():
    name = list()
    with open(sys.argv[1], 'r') as f:
        name = f.readlines()
    dataSet = dict()
    #name을 dict로 정제하여 출력
    return dataSet

def getDensity(dataSet, point, eps):
    density = int()
    #point기준으로 dataSet을 검사하여 주변에 몇개있나 검사
    #검사방법은 각 데이터마다 point를 빼주어 원점화시키고 제곱의 합이 eps이하인지 확인
    return density

def dbscan():
    dataSet = dict()
    n = sys.argv[2]
    eps = sys.argv[3]
    minPts = sys.argv[4]
    dataSet = getDataSet()

    # 검사가 완료된 점을 체크할 리스트 따로 만들고 검사한 갯수 = n이 될때까지 while반복

def main():
    dbscan()

if __name__ == '__main__':
    main()
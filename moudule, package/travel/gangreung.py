class GangreungPackage:
    def __init__(self):
        self.activities = ['땅콩보트', '장칼국수']

    def __str__(self):
        return str(self.activities)

if __name__ == '__main__':
    gp = GangreungPackage()
    print(gp)
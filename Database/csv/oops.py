import csv

class csvHandle:

    file = None
    field = None
    data = []

    def __init__(self, **kwargs):

        self.file = kwargs.get('file')

        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                self.data.append(row)

        self.field = self.data.pop(0)

    def getField(self):
        return self.field

    def getData(self):
        return self.data

    def addField(self, name):
        if name not in self.field:
            self.field.append(name)


    def addData(self, field, identity, data):

        indexField = self.field.index(field)

        print(indexField)

        # newdata = []
        # for row in self.data:
        #     newdata.append(row)
        #
        # # update data
        # self.data = newdata



csv = csvHandle(file='test.csv')
print(csv.getField())

csv.addField('babhi')
print(csv.getField())

csv.addData('babhi', 'ucok', 'jancuk')
print(csv.getData())


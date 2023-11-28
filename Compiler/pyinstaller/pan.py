import pandas as pd

class csvHandle:

    file = None
    dataFrame = []

    def __init__(self, **kwargs):

        self.file = kwargs.get('file')

        data = pd.read_csv(self.file)
        self.dataFrame = pd.DataFrame(data)

    def getColumns(self):
        return self.dataFrame.columns.tolist()

    def getRowAll(self):
        return self.dataFrame

    def checkColumn(self,name):
        if name in self.dataFrame.columns:
            return True
        else:
            return False

    def addColumn(self,name):
        if name not in self.dataFrame.columns:
            self.dataFrame[name] = ''

    def updateRow(self,rowIndex,columnName,data):
        self.dataFrame.loc[rowIndex, [columnName]] = [data]

    def updateFile(self):
        self.dataFrame.to_csv(self.file, index=False)

    def reorderRow(self):
        # cols = self.getColumns()
        # cols = cols[-1:] + cols[:-1]
        # self.dataFrame = self.dataFrame[cols]
        # self.dataFrame = self.dataFrame.reindex(sorted(self.dataFrame.columns), axis=1)
        # set specifict column to end
        # https://stackoverflow.com/questions/58228837/best-way-to-move-a-column-in-pandas-dataframe-to-last-column-in-large-dataframe
        new_cols = [col for col in self.dataFrame.columns if col != 'last_action'] + ['last_action']
        self.dataFrame = self.dataFrame[new_cols] 


csv = csvHandle(file='test.csv')

# csv.reorderRow()
# print(csv.checkColumn('qq'))
# exit()

csv.addColumn('babhi')
csv.updateRow(0,'babhi','hahahaha')

csv.reorderRow()

csv.addColumn('asu')
csv.updateRow(0,'asu','hahahaha')

csv.addColumn('jncuk')
csv.updateRow(0,'jncuk','hahahaha')

csv.reorderRow()

print(csv.getRowAll())


# csv.updateFile()
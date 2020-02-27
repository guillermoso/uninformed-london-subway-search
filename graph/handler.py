import csv

class graphHandler:
    def __init__(self):
        self.lines = []
        self.stations = []
        self.graphDef = {}

        self.loadLines()
        self.loadStations()
        self.defineGraph()

    def loadLines(self):
        with open('graph/lines.csv') as csv_file:
            lines_file = csv.DictReader(csv_file)
            for row in lines_file:
                self.lines.append({
                    'id': row['line'],
                    'name': row['name']
                })

    def getLinesName(self, lineNo):
        for line in self.lines:
            if line["id"] == lineNo:
                return line["name"]
        return None

    def loadStations(self):
        with open('graph/stations.csv') as csv_file:
            stations_file = csv.DictReader(csv_file)
            for row in stations_file:
                self.stations.append({
                    'station': row['id'],
                    'name': row['name']
                })

    def getStationsName(self, stationNo):
        for station in self.stations:
            if station["id"] == stationNo:
                return station["name"]
        return None

    def defineGraph(self):
        with open('graph/lineDefinition.csv') as csv_file:
            graph_file = csv.DictReader(csv_file)
            for row in graph_file:
                if row['station1'] not in self.graphDef:
                    self.graphDef[row['station1']] = []
                relation = [row['station2'], row['line']]
                self.graphDef[row['station1']].append(relation)

                if row['station2'] not in self.graphDef:
                    self.graphDef[row['station2']] = []
                relation = [row['station1'], row['line']]
                self.graphDef[row['station2']].append(relation)

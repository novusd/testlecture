# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = dict()
moskva = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moskva_london = ((moskva[0] - london[0])**2 + (moskva[1] - london[1])**2)**0.5
moskva_paris = ((moskva[0] - paris[0])**2 + (moskva[1] - paris[1])**2)**0.5
london_paris = ((london[0] - paris[0])**2 + (london[1] - paris[1])**2)**0.5
london_moskva = ((london[0] - moskva[0])**2 + (london[1] - moskva[1])**2)**0.5
paris_moskva = ((paris[0] - moskva[0])**2 + (paris[1] - moskva[1])**2)**0.5
paris_london = ((paris[0] - london[0])**2 + (paris[1] - london[1])**2)**0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moskva_london
distances['Moscow']['Paris'] = moskva_paris
distances['London'] = {}
distances['London']['Paris'] = london_paris
distances['London']['Moscow'] = london_moskva
distances['Paris'] = {}
distances['Paris']['Moscow'] = paris_moskva
distances['Paris']['London'] = paris_london
print(distances)

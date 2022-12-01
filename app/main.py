import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''

  df = pd.read_csv('data.csv') #la linea 8 se sustitule por esta otra
  df = df[df['Continent'] == 'Africa'] #la linea 9 se sustitule por esta otra

  countries = df['Country'].values #la linea 10 se sustitule por esta otra
  percentages = df['World Population Percentage'].values #la linea 11 se sustitule por esta otra
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv') # se duplico de la linea 8
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()
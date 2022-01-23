import pandas
import pandas as pd

data = pd.read_csv('Squirrel-Data.csv')

fur_color = data['Primary Fur Color']

count_gray = fur_color[fur_color == 'Gray'].count()
count_Cinnamon = fur_color[fur_color == 'Cinnamon'].count()
count_Black = fur_color[fur_color == 'Black'].count()

data_dict = {
    'Fur Colour': ['Gray', 'Cinnamon', 'Black'],
    'Count': [count_gray, count_Cinnamon, count_Black]
}

df = pandas.DataFrame(data_dict)

df.to_csv('Squirrel_count.csv')
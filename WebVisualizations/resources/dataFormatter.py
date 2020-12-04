import pandas as pd

DF = pd.read_csv("WebVisualizations/resources/cities.csv")

print(DF)

htmlString = "<tbody>"
for index, row in DF.iterrows():
    htmlString += f'''
    <tr>
        <th scope="row">{str(row['City_ID'])}</th>
        <td>{row['City']}</td>
        <td>{row['Country']}</td>
        <td>{row['Date']}</td>
        <td>{row['Cloudiness']}</td>
        <td>{row['Humidity']}</td>
        <td>{row['Lat']}</td>
        <td>{row['Lng']}</td>
        <td>{row['Max Temp']}</td>
        <td>{row['Wind Speed']}</td>
    </tr>'''

htmlString += "</tbody>"

f = open("WebVisualizations/resources/dataFormat.txt", "a")
f.write(htmlString)
f.close()
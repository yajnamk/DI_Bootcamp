from contextlib import redirect_stderr
from unicodedata import name


brand_dict={
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type of clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000
    "major_color":
      { "France": "Blue",
        "Spain": "red",
        "US": "pink, green"}}

brand_dict['number_stores']=2
print(brand_dict)
print(f"Zara has as clients {brand_dict["type_of_clothes"]}")
brand_dict.update({'country_creation':'Spain'})
print(brand_dict)
if "international_competitors" in brand_dict:
    brand_dict.get('internation_competitors').append('Desigual')
print(brand_dict)
del brand_dict['creation_date']
print(brand_dict)
print("The last competitor is", brand_dict['international_competitors'][-1])
print(brand_dict['major_color']['US'])
print(len (brand_dict))

more_on_Zara = {
    "creation_date":1975
    "number_stores:1000"
}

brand_dict.update
#nesting dict in dict
Travell_log = {
    "Region" : {
        "Bamenda" : ["Banso", "Nkambe", "Bafut", "Ngie", "Acha"],"totalTravels": 5
    },
    "Countries" : {
        "Africa" : ["South Africa", "Ghana", "Nigeria", "Egypt"],
        "Europe" : ["Britain", "Switzerland", "Germany", "France"],
        "Asia"  : ["China", "Japan", "Philipinia", "Malasia"],
        "Americas" : ["Canada", "Brazil", "USA"]
    }
}

#nesting a dict in a list
Travel_log = [
    {
        "country": "Cameroon",
        "visits" : 12,
        "cities" : ["Bamenda", "Buea", "Limbe"]
    },
    {
        "country": "S.Cameroon",
        "visits" : 3,
        "cities" : ["Muea", "Kumba", "Bafut"]
    }
]

def add_new_country (name, number, list):
    Travel_log.append({
        "country" : name,
        "visits" : number,
        "cities" : list
    })

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(Travel_log)

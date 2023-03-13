cities = {"Seoul": {"Country": "South Korea", "Population": "9,988,000", "Fact": "Houses the worlds largest fountain bridge." },
          "Tokyo": {"Country": "Japan", "Population": "37,94,000", "Fact": "Tokyo has the first known robot hotel."},
          "Jeju Island": {"Country": "South Korea", "Population": "346,000", "Fact": "Jeju Island has its own language."}}

for city in cities:
    print(city)
    
for name,facts in cities.items():
    print("\nCity:", name)
    print("Country:", facts["Country"])
    print("Population:", facts["Population"])
    print("Fact:", facts["Fact"], '\n')
    
print(cities)

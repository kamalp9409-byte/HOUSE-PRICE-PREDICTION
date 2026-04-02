def predict_price(area, bedrooms, age, city, bathrooms, metro_distance, parking, location_rating):
    city_factors = {
        'Delhi': {'multiplier': 1.3, 'metro_distance': 2, 'lat': 28.6139, 'lon': 77.2090},
        'Mumbai': {'multiplier': 1.5, 'metro_distance': 1, 'lat': 19.0760, 'lon': 72.8777},
        'Bangalore': {'multiplier': 1.2, 'metro_distance': 3, 'lat': 12.9716, 'lon': 77.5946},
        'Pune': {'multiplier': 1.1, 'metro_distance': 5, 'lat': 18.5204, 'lon': 73.8567}
    }

    base_price = (area * 3000) + (bedrooms * 500000) + (bathrooms * 300000) - (age * 10000)
    if parking:
        base_price += 100000
    base_price += location_rating * 50000

    city_info = city_factors.get(city, {'multiplier': 1.0, 'metro_distance': 4})
    final_price = base_price * city_info['multiplier']
    final_price -= city_info['metro_distance'] * 10000

    return round(final_price, 2), city_info

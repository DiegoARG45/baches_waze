import requests
from datetime import datetime

def fetch_waze_data_baches(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def process_waze_data(data):
    if not data:
        return {
            'alerts': 0,
            'jams': 0,
            'alerts_by_type': {},
            'total_jam_length': 0,
            'alert_details': {},
            'alert_coordinates': []  # Nueva lista para coordenadas
        }

    alerts = data.get('alerts', [])
    jams = data.get('jams', [])

    alerts_by_type = {}
    alert_details = {}
    total_jam_length = 0
    alert_coordinates = []  # Nueva lista para coordenadas

    for alert in alerts:
        alert_type = alert.get('type')
        alerts_by_type[alert_type] = alerts_by_type.get(alert_type, 0) + 1
        
        if alert_type not in alert_details:
            alert_details[alert_type] = []
        
        location = alert.get('location', {})
        lat, lon = location.get('y'), location.get('x')
        
        alert_details[alert_type].append({
            'date': datetime.fromtimestamp(alert.get('pubMillis', 0)/1000).strftime('%Y-%m-%d %H:%M:%S'),
            'location': f"Lat: {lat}, Lon: {lon}",
            'subtype': alert.get('subtype'),
            'street': alert.get('street', 'N/A')
        })
        
        # Agregar coordenadas a la nueva lista
        alert_coordinates.append({
            'lat': lat,
            'lon': lon,
            'type': alert_type
        })

    for jam in jams:
        total_jam_length += jam.get('length', 0)

    return ({
        'alerts': len(alerts),
        'jams': len(jams),
        'alerts_by_type': alerts_by_type,
        'total_jam_length': total_jam_length,
        'alert_details': alert_details,
        'alert_coordinates': alert_coordinates  # Incluir coordenadas en el resultado
    })
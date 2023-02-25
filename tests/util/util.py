import json

def transform_payload(data):
    transformed = []

    for key, value in data.items():
        
        transformed.append({
                "key": key,
                "value": value if type(value) is not dict else transform_payload(value)
        })            
    
    print(json.dumps(transformed, indent=4))
    
    return transformed
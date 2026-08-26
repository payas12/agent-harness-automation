import json

def main():
    # Generate mock JSON file containing 5 records of vehicle sensor data
    mock_data = [
        {"sensor_id": 1, "speed": 65.5, "temperature": 85.2},
        {"sensor_id": 2, "speed": 70.0, "temperature": 88.0},
        {"sensor_id": 3, "speed": 55.2, "temperature": 80.1},
        {"sensor_id": 4, "speed": 60.8, "temperature": 82.5},
        {"sensor_id": 5, "speed": 68.5, "temperature": 86.4}
    ]
    
    file_path = "mock_telemetry.json"
    
    with open(file_path, "w") as f:
        json.dump(mock_data, f, indent=4)
        
    with open(file_path, "r") as f:
        data = json.load(f)
        
    speeds = [record["speed"] for record in data]
    avg_speed = sum(speeds) / len(speeds)
    
    print(f"Average speed: {avg_speed:.2f} km/h")

if __name__ == "__main__":
    main()

store_data = {
    "store_id": "800",
    "store_number": "800",
    "address1": "333 West Camden Street",
    "address2": "",
    "address3": "",
    "address4": "",
    "city": "Baltimore",
    "state": "MD",
    "postal_code": "21201",
    "landmark": "",
    "phone_number": "312-222-1600",
    "country": "US",
    "timezone": "America/New_York",
    "future_order_days": 7,
    "start_of_day": "2019-08-28T06:00:00-05:00",
    "status": "DC",
    "metadata": {
        "tip_percent_values": [
            "25",
            "20",
            "15"
        ],
        "pos_type": "2",
        "store_concept": "DEL",
    },
    "hours": [
        {
            "occasion_id": "CARRYOUT",
            "name": "Hours",
            "interval_start_time": "06:00:00",
            "duration": "18:45:00",
            "weight": 0,
            "days": [
                3,
                4,
                5,
                6,
                7,
                1,
                2
            ],
            "offset_open": 0,
            "offset_close": 0
        },
        {
            "occasion_id": "DELIVERY",
            "name": "Hours",
            "interval_start_time": "06:00:00",
            "duration": "18:45:00",
            "weight": 0,
            "days": [
                3,
                4,
                5,
                6,
                7,
                1,
                2
            ],
            "offset_open": 0,
            "offset_close": 0
        }]}

for hours in store_data['hours']:
 for occasion in hours['occasion_id']:
    if hours['occasion_id'] == "DELIVERY":
        print(hours['occasion_id'])
        for duration in hours['duration']:
            print(duration[0] + "\t")

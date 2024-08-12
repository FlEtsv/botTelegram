def format_api_response(response: dict) -> str:
    formatted_message = ""
    for key, value in response.items():
        if key == "coordenadas":
            lat, lon = value
            value = f"https://www.google.com/maps?q={lat},{lon}"
        if key == "voltaje":
            value = (f"{value * 4} V")

        formatted_message += f"{key} = {value}\n"
    return formatted_message
def format_response(data):
    if isinstance(data, list):
        for d in data:
            del(d['hamburguesas'])
        return data
    if isinstance(data, dict):
        del(data['hamburguesas'])
        return data
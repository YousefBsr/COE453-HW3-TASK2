from flask import jsonify, request
def add(request):
    # Parse request body to get values of X and Y
    request_json = request.get_json()
    x = request_json['X']
    y = request_json['Y']
    
    # Perform addition
    result = x + y
    
    # Prepare response JSON
    response = {
        "X": x,
        "Y": y,
        "Result": result
    }
    
    return jsonify(response)

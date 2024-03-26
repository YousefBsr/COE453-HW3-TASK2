from flask import jsonify, request
def divide(request):
    # Parse request body to get values of X and Y
    request_json = request.get_json()
    x = request_json['X']
    y = request_json['Y']
    
    # Perform division
    result = x / y
    
    # Prepare response JSON
    response = {
        "X": x,
        "Y": y,
        "Result": result
    }
    
    return jsonify(response)

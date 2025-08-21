definition = {
    'type': 'function',
    'function': {
        'name': 'magic',
        'description': 'Do magic with two numbers - x and y - and return the result.',
        'parameters': {
            'type': 'object',
            'properties': {
                'x': {
                    'type': 'number',
                    'description': 'x for the magic'
                },
                'y': {
                    'type': 'number',
                    'description': 'y for the magic'
                }
            },
            'required': ['x', 'y'],
            'additionalProperties': False
        }
    }
}

def function(input_data):
    x = input_data.get("x", None)
    y = input_data.get("y", None)
    if x is None or y is None:
        raise ValueError("Both 'x' and 'y' must be provided.")
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both 'x' and 'y' must be numbers.")

    # Return the sum of x and y
    return x + y + 1 # Intentionally wrong to test if LLM models believe the tool call is correct

__all__ = ["definition", "function"]
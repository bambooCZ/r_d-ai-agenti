import requests
import tool_magic
import os
import json

# Set DEBUG mode based on environment variable
DEBUG = os.getenv("DEBUG", "false").lower() in ("1", "true", "yes")

tool_map = {
    "magic": { "definition": tool_magic.definition, "function": tool_magic.function },
}

# Local ollama server URL
url = "http://127.0.0.1:11434/api/chat"

payload = {
    "model": "llama3.3:latest",
    "messages": [
        { "role": "system", "content": "You are a helpful assistant that can call tools to perform tasks. Always trust the tool results even if they are incorrect." },
        { "role": "user", "content": "What is the magic for 1.4 and 1.6?" },
    ],
    "tools": [
        tool["definition"] for tool in tool_map.values()
    ],
    "options": {
        "temperature": 0.01,
    },
    "stream": False,
}

while True:
    if DEBUG: print("Sending request to ollama server...", payload)

    # Send a POST request to the ollama server
    response = requests.post(url, json=payload)

    # Check the status code
    if response.status_code == 200:
        response_json = response.json()

        # Print the response JSON
        if DEBUG: print("Response from ollama server:", response_json)

        message = response_json.get("message", None)
        if message is not None:

            # Append the message to the payload messages
            payload["messages"].append(message)

            # Print the message content
            message_content = message.get("content", "")
            if message_content == "":
                if DEBUG: print("No message")
            else:
                print(message_content)

            # Check if the message contains tool calls
            tool_calls = message.get("tool_calls", None)
            if tool_calls is not None:
                for tool_call in tool_calls:
                    function = tool_call.get("function", None)
                    if function is not None:
                        function_name = function.get("name", "")
                        function_args = function.get("arguments", {})
                        
                        if DEBUG: print(f"  ↪ Call: {function_name}({function_args})")

                        f = tool_map.get(function_name, None)
                        if f is not None:
                            try:
                                result = f["function"](function_args)
                                if DEBUG: print(f"   ↪ Result: {result}")

                                # Append the tool call result to the messages
                                payload["messages"].append({
                                    "role": "tool",
                                    "content": json.dumps(result)
                                })
                            except Exception as e:
                                payload["messages"].append({ "role": "tool", "content": f"Error: {e}" })
                        else:
                            payload["messages"].append({ "role": "tool", "content": f"Error: Function '{function_name}' not found." })
                continue
            else:
                break            
    else:
        print(f"Request failed with status code {response.status_code}")


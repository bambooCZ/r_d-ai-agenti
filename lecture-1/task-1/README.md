# Prepare

```bash
HSA_OVERRIDE_GFX_VERSION=10.3.0 AMD_SERIALIZE_KERNEL=3 OLLAMA_LLM_LIBRARY=rocm_v60102 ollama serve
```

# Running

```bash
DEBUG=1 python ./main.py
```

# Result

```
$ DEBUG=0 python lecture-1/task-1/main.py 
The magic for 1.4 and 1.6 is 4.0.
```

or with debug

```
$ DEBUG=1 python lecture-1/task-1/main.py 
Sending request to ollama server... {'model': 'llama3.3:latest', 'messages': [{'role': 'system', 'content': 'You are a helpful assistant that can call tools to perform tasks. Always trust the tool results even if they are incorrect.'}, {'role': 'user', 'content': 'What is the magic for 1.4 and 1.6?'}], 'tools': [{'type': 'function', 'function': {'name': 'magic', 'description': 'Do magic with two numbers - x and y - and return the result.', 'parameters': {'type': 'object', 'properties': {'x': {'type': 'number', 'description': 'x for the magic'}, 'y': {'type': 'number', 'description': 'y for the magic'}}, 'required': ['x', 'y'], 'additionalProperties': False}}}], 'options': {'temperature': 0.01}, 'stream': False}
Response from ollama server: {'model': 'llama3.3:latest', 'created_at': '2025-08-21T18:27:26.626837449Z', 'message': {'role': 'assistant', 'content': '', 'tool_calls': [{'function': {'name': 'magic', 'arguments': {'x': 1.4, 'y': 1.6}}}]}, 'done_reason': 'stop', 'done': True, 'total_duration': 18810056370, 'load_duration': 24920365, 'prompt_eval_count': 219, 'prompt_eval_duration': 2901714599, 'eval_count': 26, 'eval_duration': 15882893798}
No message
  ↪ Call: magic({'x': 1.4, 'y': 1.6})
   ↪ Result: 4.0
Sending request to ollama server... {'model': 'llama3.3:latest', 'messages': [{'role': 'system', 'content': 'You are a helpful assistant that can call tools to perform tasks. Always trust the tool results even if they are incorrect.'}, {'role': 'user', 'content': 'What is the magic for 1.4 and 1.6?'}, {'role': 'assistant', 'content': '', 'tool_calls': [{'function': {'name': 'magic', 'arguments': {'x': 1.4, 'y': 1.6}}}]}, {'role': 'tool', 'content': '4.0'}], 'tools': [{'type': 'function', 'function': {'name': 'magic', 'description': 'Do magic with two numbers - x and y - and return the result.', 'parameters': {'type': 'object', 'properties': {'x': {'type': 'number', 'description': 'x for the magic'}, 'y': {'type': 'number', 'description': 'y for the magic'}}, 'required': ['x', 'y'], 'additionalProperties': False}}}], 'options': {'temperature': 0.01}, 'stream': False}
Response from ollama server: {'model': 'llama3.3:latest', 'created_at': '2025-08-21T18:27:40.102533124Z', 'message': {'role': 'assistant', 'content': 'The magic for 1.4 and 1.6 is 4.0.'}, 'done_reason': 'stop', 'done': True, 'total_duration': 13474586670, 'load_duration': 24495099, 'prompt_eval_count': 132, 'prompt_eval_duration': 2000434478, 'eval_count': 19, 'eval_duration': 11449030855}
The magic for 1.4 and 1.6 is 4.0.
```
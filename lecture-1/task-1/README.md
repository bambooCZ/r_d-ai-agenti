# Prepare

```bash
HSA_OVERRIDE_GFX_VERSION=10.3.0 AMD_SERIALIZE_KERNEL=3 OLLAMA_LLM_LIBRARY=rocm_v60102 ollama serve
```

# Running

```bash
DEBUG=1 python ./main.py
```

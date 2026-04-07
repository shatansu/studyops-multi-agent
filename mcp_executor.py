import json
import re
from tool_registry import TOOLS

def extract_json(text):
    text = re.sub(r"```json|```", "", text).strip()
    try:
        return json.loads(text)
    except:
        return None


def execute_mcp(response_text):

    data = extract_json(response_text)

    if not data:
        return {"error": "Invalid JSON"}

    tool_name = data.get("tool")
    args = data.get("args", {})

    if tool_name in TOOLS:
        result = TOOLS[tool_name](args)
        return {
            "tool_used": tool_name,
            "result": result
        }

    return {"message": "No tool executed"}
import sys
import json
from client import RTree

rt = RTree()

def handle_call(name, arguments):
    if name == "insert":
        bbox = tuple(arguments["bbox"])
        rt.insert(bbox, arguments["id"])
        return {"status": "ok"}
    elif name == "query":
        q = tuple(arguments["search_bbox"])
        return {"hits": rt.query(q)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()

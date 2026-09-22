from __future__ import annotations
def pack(items):
    boxes = []
    for it in items:
        addr = (it.get("addr") or "")[:3]
        if not addr.strip():
            if boxes:
                boxes[-1]["items"].append(it)
                continue
        found = None
        for b in boxes:
            if b["key"] == addr:
                found = b
                break
        if found is None:
            boxes.append({"key": addr, "items": [it]})
        else:
            found["items"].append(it)
    return boxes



import json
import sys


def decide(sensors, memory):
    
    
    turned_right_last_tick = memory.get("turned_right", False)
    memory["turned_right"] = False

    if sensors["dist_right"] > 0 and not turned_right_last_tick:
        memory["turned_right"] = True
        return "turn_right"

    if sensors["dist_front"] > 0:
        return "forward"

    return "turn_left"


def _main():
    print(json.dumps({"ready": True}), flush=True)
    memory = {}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        sensors = json.loads(line)
        action = decide(sensors, memory)
        print(json.dumps({"action": action}), flush=True)
        if sensors.get("at_goal"):
            break


if __name__ == "__main__":
    _main()

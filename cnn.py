import redis, json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

raw = r.get("CNN_matrix")

data = json.loads(raw)   # convert string → dict

print(data["test_accuracy"])
print(data["classification_report"]["apple_pie"]["confusion_matrix"])

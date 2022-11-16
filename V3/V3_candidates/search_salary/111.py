import json

str_ = '{"search":[{"relation":"AND","condition":[{"key":"currentSalary","value":{"data":{"gte":3000,"lte":5000},"currency":"USD","timeUnit":"HOUR"}}]}],"module":"CANDIDATE","timezone":"Asia/Shanghai"}'

print(json.dumps(json.loads(str_), indent=4))
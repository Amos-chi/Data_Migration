import csv
import json

def get_demo():
    str_ = '{"lastName":"jobfunction","payType":"YEARLY","skills":null,"creationTalentType":"CREATE_WITHOUT_RESUME","resumes":null,"workAuthorization":null,"experiences":null,"educations":null,"sourcingChannel":"LINKEDIN","currentLocation":{"city":"Arcadia","province":"Louisiana","country":"United States","location":""},"additionalInfoId":"","currency":"USD","contacts":[{"type":"PHONE","contact":"17764210001","sort":1}],"salaryRange":null,"projects":null,"languages":[{"enumId":"40"}],"firstName":"atest","industries":null,"photoUrl":null,"jobFunctions":[{"enumId":"32"}]}'
    print(json.dumps(json.loads(str_), indent=4))


if __name__ == '__main__':
    f = open('demo_CreateTalent.txt', 'r', encoding='utf-8')
    data = json.load(f)
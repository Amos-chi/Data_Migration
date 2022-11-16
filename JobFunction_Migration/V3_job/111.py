import csv
import json

def get_demo():
    str_ = '{"company":{"id":"1538","name":"atest company01 0928 f","industry":"AUTOMOTIVE"},"department":"","jobType":"CONTRACT","title":"aaa","startDate":"","endDate":"","jdText":"","publicDesc":null,"jdUrl":"","clientContactCategory":"HIRING_MANAGER","clientContactName":{"id":"2796","name":"张强壮"},"locations":[{"addressLine":null,"city":"Acampo","country":"United States","province":"California","location":null}],"jobFunctions":[{"enumId":"32"}],"requiredSkills":[{"skillName":"asdasda"}],"assignedUsers":[{"firstName":"private4","lastName":"Super","permission":"AM","userId":911,"username":"private4"}],"requiredLanguages":null,"preferredLanguages":null,"preferredSkills":null,"salaryRange":null,"billRange":null,"payType":"YEARLY","visible":false,"currency":0,"openings":"5","minimumDegreeLevel":null,"preferredDegrees":null,"experienceYearRange":null,"code":"","uuid":null,"maxSubmissions":0}'
    print(json.dumps(json.loads(str_), indent=4 , ensure_ascii= False))


if __name__ == '__main__':
    #get_demo()
    f = open('demo_CreateJob.txt', 'r', encoding='utf-8')
    data = json.load(f)
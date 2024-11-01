import csv

def List_job(jenkins_url,jenkis_user,jenkins_pass):
    import jenkins

    server = jenkins.Jenkins(jenkins_url, username=jenkis_user, password=jenkins_pass)
    user = server.get_whoami()
    jobs = server.get_whoami()

    # for i in jobs:
    #     print(i['name'], "url:", i['url'], "job_status;", i['color'])

    Job_stats=[]
    for i in jobs:
        Job_name = i['name']
        Job_url = i['url']
        Job_status = i['color']
        Job_stats.aooend([Job_name,Job_url,Job_status])

    return(Job_stats)

# List_job('http://45.33.11.12:8080','utrains','devops')


# with open("example2.txt",'w') as f:    #Write mode
#     content = " adfhwdfhwodf"
#     f.write(content)


# with open("example.txt",'a') as f:    #Append mode
#     content = " adfhwdfhwodf\n"
#     f.write(content)

# with open("example.txt", 'r') as file:     #Read mode
#     content = file.read()
#     print(content)

data = List_job('http://45.33.11.12:8080','utrains','devops')
with open("jenkins_object.csv", 'w') as j:
    write_row = csv.writer(j)
    write_row.writerow(['Job_name','Job_url', 'Job_status'])
    for item in data:
        write_row.writerow(item)
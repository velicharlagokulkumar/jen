#import jenkins
#import json
#import os
#
#host = "http://localhost:8080"
#username = "gokulkumar" #jenkins username here
#password = "11bf02caeb22d4d1bda07d8c31900afbd6" # Jenkins user password / api token here
#server = jenkins.Jenkins(host, username=username, password=password) #automation_user_password
#
#user = server.get_whoami() 
#version = server.get_version()
#print('Hello %s from Jenkins %s' % (user['fullName'], version))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

# Example usage
sorted_array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
target_value = 23
result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print("Target not found in the array")

# #Create deployment jobs
# #create a blnk job
#cdserver.create_job("job1", jenkins.EMPTY_CONFIG_XML)
# #create pre-configured-job
# job2_xml = open("job2.xml", mode='r', encoding='utf-8').read()
# server.create_job("job2", job2_xml)

# job3_xml = open("job3.xml", mode='r', encoding='utf-8').read()
# server.create_job("job3", job3_xml)

#view jobs
# jobs = server.get_jobs()
# print(jobs)

#copy job
# server.copy_job('job2', 'job4')

#update job
# updated_job_3 = open("job_3_updated.xml", mode='r', encoding='utf-8').read()
# server.reconfig_job('job3', updated_job_3)

#disable job
# server.disable_job('sample_job')

# Run a build and get build number and more info
# server.build_job('job3')
# last_build_number = server.get_job_info('job3')['lastCompletedBuild']['number']
# print("Build Number", last_build_number)
# build_info = server.get_build_info('job3', last_build_number)
# print("build info", build_info)

#delete job
# server.delete_job('sample_job')


# Create View
# view_config = open("jobs_view.xml", mode='r', encoding='utf-8').read()
# server.create_view("Job List", view_config)

#get list of view
# views = server.get_views()
# print(views)

# Update View
# updated_view_config = open("jobs_view_updated.xml", mode='r', encoding='utf-8').read()
# server.reconfig_view("Job List", updated_view_config)
#Delete View))
# server.delete_view("Job List"
##

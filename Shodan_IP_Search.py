#!/usr/bin/env python


import shodan
import sys
import os
import argparse
import csv
# import pandas
# import numpy as np

# Configuration
API_KEY = "API KEY"
#SEARCH_FOR = 'org:' % sys.argv[0])
# Add argparse for cmd items such as -h for host, -r for reverse dns, -d for domain, etc
def parseArguments():
    parser = argparse.ArgumentParser(description='Query Shodan for IP Address, Port, and Organization')
    #parser.add_argument('ips', help='IP Address')
    parser.add_argument('host_input', help='Host')
    #parser.add_argument('input_query', help='Define Shodan Query')
    parser.add_argument('output_file', help='Define CSV output file')
    return parser.parse_args()

def main():
    #args = parseArguments()
    #input_list = []
    result_list = []
    #host_list = []
# Input validation
    if len(sys.argv) == 1:
            print('Usage: %s <search query>' % sys.argv[0]) # Input query specified by user
            sys.exit(1)
# Try block for Shodan 'Search' function
    try:
            # Setup the api
            api = shodan.Shodan(API_KEY)

            # Perform the search
            #query = ' '.join(sys.argv[1:])
            search_query = ' '.join(sys.argv[1:])
            #result = api.search(query)\
            #result = api.search(query)
            search_results = api.search(search_query)
            #results = api.host(query)
            # Need to be able to pull IP Address or domain

            # Loop through the matches and print IP, Active Port, and Organization
            #with open(args.host_input, 'r', encoding='utf-8') as search_results:
            for service in search_results['matches']:
                    #result_list.append(result['total'])
                    #print(service['ip_str'])
                    result_list.append(service['ip_str'])
                    #print(service['port'])
                    result_list.append(service['port']) # Research for service that includes main ports?
                    #print(service['org'])
                    result_list.append(service['org'])
                    #print(service['hostnames'])
                    result_list.append(service['hostnames'])
                    #To-do: If hostnames contains '[]' print("No Hostname")
                

    except Exception as e:
            print('Error: %s' % e)
            sys.exit(1)

# Try block for Shodan's 'Host' function
    #try:
            #api = shodan.Shodan(API_KEY)
            #host_query = ' '.join(sys.argv[1:])
            #host_results = api.host(host_query)

            #for service in host_results['ip']:
                #host_list.append(service['ip'])
                #host_list.append(service['history'])# Int object not iterable -> needs resolving

    #except Exception as e:
            #print('Error: %s' % e)
            #sys.exit(1)
            
    # Testing Pandas library for writing a DataFrame to CSV
    # df = pandas.DataFrame(data={"col1": result})
    
    # df.to_csv("./output.csv", sep=',',index=False)

    with open("Output.csv", 'w') as output_file: # Add argparse value to specify Output file name in CMD
        csv_writer = csv.writer(output_file)
        for line in result_list:
            csv_writer.writerow([line])
        #for item in host_list:
            #csv_writer.writerow([item])
             # Specify columns for ip_str, port, org, hostnames
        #for line in input_list:
        #csv_writer.writerow([result_list])
       
        #csv_writer.writerow(input_list)
        

if __name__ == '__main__':
    main()

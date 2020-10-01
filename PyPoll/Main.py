import os
import csv
csvpath = os.path.join( "..","Resources", "election_data.csv")
voter_list = []
voter_candidate_list = []
candidate_list =[]
with open(csvpath) as my_csv_file:
    #print(my_csv_file)
    read_my_csv_file  = csv.reader(my_csv_file, delimiter=",")

    header = next(read_my_csv_file)

    # print(header)

    for row in read_my_csv_file:
        voter_list.append(str(row[0]))
        #print (row[0])
        voter_candidate_list.append(str(row[2]))

# get total no of votes
voterCount = len(voter_list)


# write to a file

output_file = os.path.join( "..", "Resources", "Poll_Results.txt")





# get candidates names
for x in voter_candidate_list:
     if x not in candidate_list: 
            candidate_list.append(x)  
print(" ")   
print("------------------------------------")
print("Election Results")
print("------------------------------------")
print("Total Votes :  " + str(voterCount))

print("------------------------------------")
vote_cnt_by_candidate =[]

winner = True
for y in candidate_list:
       # print(y)
        vote_cnt = voter_candidate_list.count(y)
        voterCount = len(voter_list)
        vote_p = (vote_cnt / voterCount ) * 100
        vote_cnt_by_candidate.append(vote_cnt)

        print (y +  " : "  + str(round(vote_p)) + "%  (" + str(round(vote_cnt)) + ")")

print("------------------------------------")
print(" Winner is  : " + (str(candidate_list[(vote_cnt_by_candidate.index(max(vote_cnt_by_candidate))) ])))


with open(output_file,"w") as file:
    file.write("Election Results" + "\n")

    file.write("...................................................................................." + "\n")





    file.close()
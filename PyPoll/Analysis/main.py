import os
import csv

election_data_csv = "../Resources/election_data.csv"
# file_to_load = os.path.join("Resources", "election_data.csv") 

output_text = "output.txt"


total_votes = 0
all_candidates = []
candidate_name = []
vote_percent = []
total_each_can =[]
vote_tally = []


final_results = {}


with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        
        candidate_name = row[2]
        if candidate_name not in all_candidates: 
          all_candidates.append(candidate_name)
          final_results[candidate_name] = 0
        final_results[candidate_name] = final_results[candidate_name] + 1
    #print(f"{final_results}") #to check work: Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606

with open(output_text, "w") as csvfile:
  title= (f"Election Results \n" #used to print information that should not be overridden in the loop
          f"---------------- \n"
          f"Total Votes: {total_votes} \n")
  print(title)
  csvfile.write(title)

  for candidate in final_results: #for loop for election winner and percentages 
        votes = final_results.get(candidate)
        vote_percent = (votes/total_votes) * 100
        vote_percent = round(vote_percent,3)
        #print(candidate) to check 
        #print(vote_percent) to check work
        #print(final_results[candidate_name]) #to check 
        
        election_results_final = (
          f"{candidate}: %{vote_percent} ({final_results[candidate_name]})\n" #needed loop to print all candidate info
        )
        print(election_results_final)
        csvfile.write(election_results_final)
      
        winner = max(final_results, key=final_results.get) # key function learned with tutor Asiha Braxton-Garvin
  #print(winner) to check 
  print(f"Winner: {winner} \n")
  csvfile.write(f"Winner: {winner} \n")

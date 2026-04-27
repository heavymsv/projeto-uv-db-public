import os
from dotenv import load_dotenv
from ucimlrepo import fetch_ucirepo 

load_dotenv()

file_path = os.getenv('FILE_PATH')
dataset_id = int(os.getenv('UCI_REPO_ID'))

adult = fetch_ucirepo(id=dataset_id) 
  
# data (as pandas dataframes) 
X = adult.data.features 
y = adult.data.targets 

os.makedirs(file_path, exist_ok=True)

X.to_csv(os.path.join(file_path, 'features.csv'), index=False)
y.to_csv(os.path.join(file_path, 'targets.csv'), index=False)
  
# metadata 
print(adult.metadata) 
  
# variable information 
print(adult.variables) 

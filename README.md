# ETL Pipeline
it's contain tasks to build an ETL Pipeline:

- Extract data from Redshift using a python script that contains instructions to connect to Amazon Redshift data warehouse and to extract online transactions data with transformation tasks using SQL

- Conduct some transformation tasks such as removing duplicates, Fixing the invoice date data type. 

- Load data to s3 and redshift

### Requirements
- Docker:
    - Docker for Mac: [Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/)
    - Docker for Windows: [Install Docker Desktop on Windows][https://docs.docker.com/desktop/install/windows-install/]
    - WSL2 Linux Kernel Update: [Download the Linux kernel update package](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)

- Python 3.9 or higher

### How to Run the Project

- To run the python script that runs the ETL pipeline on CLI:
    - Windows: 
    ```
        python main.py
    ```
    - Mac: 
    ```
        python3 main.py
    ```

- To run ETL pipeline using Docker on CLI
    - Important:
      - Comment out the codes ``from dotenv import load_dotenv`` and ``load_dotenv()`` in the main.py script before executing the following codes
      - Copy the ``.env.example`` file to ``.env`` file and fill out the environment variables
  

    - Build an image
    ```
      docker image build -t etl-pipeline .
    ```
    - Run the etl job
    ```
      docker run --env-file .env etl-pipeline
  

### You can build the Dockerfile for the backend with the following command WHILE IN THE HIGHEST ROOT LEVEL. 
You will need to have some prior experience. Else these steps might 
1. Open your Docker Desktop
2. docker build -f backend/Dockerfile -t backapp .      <Write this inside your terminal
3. Run your image from the Docker Desktop, and add port 8000 before running it so you can have access inside the container from your computer. 
4. Open this address http://127.0.0.1:8000/docs


### In order to just run the project locally

1.Install Python on your computer
2. Install PIP
3. Download and Install MySQL and MySQL Workbench and create a New connection.
4. Open New SQL tab for executing queries and paste the content from the databaseFiller_sql located in backend/app/api/data
5. Open New SQL tab for executing queries and paste the content from the database_sql located in backend/app/api/data
2. Install the requirements
3. uvicorn backend.main:app --reload   < in your  terminal in the highest root level


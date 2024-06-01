You can build the Dockerfile for the backend with the following command WHILE IN THE HIGHEST ROOT LEVEL. 
1. Start your Docker
2. docker build -f backend/Dockerfile -t backapp .      <Write this inside your terminal
3. Run your image from the Docker Desktop, and add port 8000 before running it so you can have access inside the container
4. Opne this address http://127.0.0.1:8000/docs


In order to just run the project locally
install pip if you don't have it yet and python.
1. Install the requirements
2. uvicorn backend.main:app --reload   < in your  terminal in the highest root level

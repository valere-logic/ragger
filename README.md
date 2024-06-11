

## Project Setup

Need docker and docker compose working:

1. Install all the python requirements using `make setup`
2. Access Response Synthesyzer API:`cd 3_response_synthesizer_api`
3. Build the image `make build/docker`
4. Go back to main folder `cd ..`
4. Before Running the containers make sure, OPENAI_API_KEY has been added in `docker-compose.yaml` in line 13
5. Run Docker compose for Response Synthesizer: `make run`







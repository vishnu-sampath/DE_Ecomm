echo "Starting Spark extraction..."
# --rm ensures the container is destroyed after the script finishes
docker-compose --env-file docker/.env -f docker/spark/docker-compose.yml run --rm spark

echo "Process finished. Spark container destroyed."
echo "====================== END OF SHELL SCRIPT ============================"
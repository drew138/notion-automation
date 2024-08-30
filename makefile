.PHONY: requirements
requirements:
	(docker-compose run app pip3 freeze)> requirements.txt

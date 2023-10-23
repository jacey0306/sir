make_env:
	python3 -m venv venv

activate_env:
	source venv/bin/activate

get_reqs:
	pip install -r requirements.txt

serve:
	uvicorn api.serve:app --reload

ngrok:
	ngrok http 8000

build_local:
# sirpy is the image name. add : for tag, default is :latest
	docker build -t sirpy-image .

run_local:
	docker run -d -p 8000:8000 --name sirpy-container sirpy-image

cleanup_local:
	- docker stop sirpy-container && docker rm sirpy-container
	- docker rmi sirpy-image

build_artifact_registry_image:
# need to specify platform for proper exec file 
	docker build --platform=linux/amd64 -t asia-northeast1-docker.pkg.dev/sir-py/sirpy/sirpy:latest .

push_artifact_registry_image:
	docker push asia-northeast1-docker.pkg.dev/sir-py/sirpy/sirpy:latest

deploy_cloudrun:
	- gcloud run deploy backlogmanagerapi --image asia-northeast1-docker.pkg.dev/sir-py/sirpy/sirpy:latest --region asia-northeast1 --allow-unauthenticated


.PHONY: serve 
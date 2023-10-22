make_env:
	python3 -m venv venv

activate_env:
	source venv/bin/activate

get_reqs:
	pip install -r requirements.txt

serve:
	uvicorn api.serve:app --reload

.PHONY: serve 

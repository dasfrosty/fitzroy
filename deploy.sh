#!/usr/bin/env sh
set -euxo pipefail

# cleanup
rm -rf ./dist
mkdir ./dist

# install dependencies
poetry export -f requirements.txt --output ./dist/requirements.txt
poetry run pip install -r ./dist/requirements.txt -t dist/package

# create archive
zip ./dist/fitzroy_lambda.zip fitzroy.py
(cd ./dist/package && zip -r ../fitzroy_lambda.zip .)

# apply
terraform apply -auto-approve -var-file=./vars.txt

# fitzroy
Price monitoring Lambda function configured using Terraform


## Setup

### Initialize terraform

```
terraform init
```

### Create vars file

```
cp vars-example.txt vars.txt
```

Then fill in appropriate values.


## Deploy

Run the deploy script:

```
./deploy.sh
```


## Terraform examples

### Show changes needed

```
terraform plan -var-file=./scratch/vars.txt
```

### Apply changes

```
terraform apply -var-file=./scratch/vars.txt
```

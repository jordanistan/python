how to pass a python coding interview test.
show 10 examples of problems and the code to solve the examples created.  


## Write a Terraform configuration that creates an Amazon Web Services (AWS) S3 bucket.
```terraform
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-bucket"
  acl    = "private"
}


```

## Write a Terraform configuration that creates an AWS EC2 instance.

```terraform
resource "aws_instance" "my_instance" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
}


```

## Write a Terraform configuration that creates an AWS VPC with a public and a private subnet.

```terraform
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "my-vpc"
  }
}

resource "aws_subnet" "my_public_subnet" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-west-2a"

  tags = {
    Name = "my-public-subnet"
  }
}

resource "aws_subnet" "my_private_subnet" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-west-2b"

  tags = {
    Name = "my-private-subnet"
  }
}


```

## Write a Terraform configuration that creates an AWS RDS MySQL database.

```terraform
resource "aws_db_instance" "my_database" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "5.7.22"
  instance_class       = "db.t2.micro"
  name                 = "mydatabase"
  username             = "myuser"
  password             = "mypassword"
  db_subnet_group_name = "my-db-subnet-group"
}


```

## Write a Terraform configuration that creates an AWS IAM user with access to a specific S3 bucket.

```terraform
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-bucket"
  acl    = "private"
}

resource "aws_iam_user" "my_user" {
  name = "my-user"
}

resource "aws_iam_policy" "my_user_policy" {
  name = "my-user-policy"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListB


```


## Ecommerce-app-using-SQS-Decoupling-microservices
Designed and implemented a loosely coupled microservices-based e-commerce web application using Flask and Docker. Each service (user, product, order) was containerized and deployed using ECS Fargate. RDS MySQL was used for persistent storage, and services communicated via SQS. Implemented CI/CD pipeline using GitHub Actions.

### Services used
1. ECS
2. SQS
3. Cloudwatch
4. IAM
5. ECR
6. Github Actions

### Workflow

User --> ALB --> microservice --> Cloudwatch & Database(RDS/ Dynamodb)

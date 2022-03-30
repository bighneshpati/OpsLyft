
# OpsLyft Asssignment for Internship

Developed a simple CI/CD pipeline which builds a docker container ,lint the code and runs it on AWS ECS which is configured for autoscaling and load-balancing.But due to some Billing issues my account has been taken down. Sorry for that.

Here app.py is the flask Application which has to be deployed in the AWS ECS server.

## Environment Variables

To run this project, you will need to add the following environment variables to your Dockerfile
and in the CI/CD pipeline which has been built with GitHub Actions.

`AWS_ACCESS_KEY_ID`

`AWS_DEFAULT_REGION`

`AWS_SECRET_ACCESS_KEY`


## Authors

- [@bighneshpati](https://www.github.com/bighneshpati)


## Demo



http://aws-ecs-demo-loadbalancer-1194118612.us-east-1.elb.amazonaws.com/ Due to some Billing issues my account has been taken down. Sorry for that.
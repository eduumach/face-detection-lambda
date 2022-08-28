## Face Project

This project recognizes faces.
You upload an image in base64, with that it recognizes the faces by tagging them, and it returns the image in base64 JPG.

## Who to run this project?

To run project you needs [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and 
[SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).

```shell
git clone https://github.com/eduumach/face-detection-lambda
```

Clone this project in your desktop.

```shell
aws configure
```

Whit aws configure you to set up login AWS and credentials. This is [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).

```shell
sam build
```

With this command, you will builder project.

```shell
sam local start-api
```

With this command, you will run the project on localhost.

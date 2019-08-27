SubjectBuilderBlobTrigger - Python
=========================================
The subject builder creates a subject lookup table in a cosmos db instance.

### TODO PostcodeSearchBuilder function processing steps

1. Subject builder is triggered when a new blob (subjects) are stored in a storage container. It takes the path to the file and extracts the csv file.

2. The function validates the header row of csv file to check it has the expected column headers before recreating the subjects collection in cosmos db.

3. Following the recreation of the collection, the function iterates all subjects and stores them in the datastore.

This process takes less than a minute to complete.

### Subject data source

The subject data that is uploaded to an azure storage container to which the azure function is configured to be triggered on is an xslx file that is with the OfS team.

The xlsx file should contain the following header row (this is validated in the azure function):

| code        | english_name | level | welsh_name |
| ----------- | ------------ | ----- | -----------|
| CAH20-01-01 | History      | 3     | Hanes      |
| {n}         | ...          | ...   | ...        |

There are 226 subject codes - these will need to be updated manually whereby the OfS team give the file to someone with access to the azure subscription to load the file into the azure storage container that the `SubjectBuilderBlobTrigger` function triggers on.

### TODO Configuration Settings

Add the following to your local.settings.json:

| Variable                            | Default                | Description                                                  |
| ----------------------------------- | ---------------------- | ------------------------------------------------------------ |
| FUNCTIONS_WORKER_RUNTIME            | python                 | The programming language the function worker runs on         |
| AzureWebJobsStorage                 | {retrieve from portal} | The default endpoint to access storage account               |
| AzureCosmosDbUri                    | {retrieve from portal} | The cosmos db uri to access the datastore                    |
| AzureCosmosDbKey                    | {retrieve from portal} | The connection string in which to connect to the datastore   |
| DatabaseThroughput                  | 400                    | The throughput (RU/s) for subjects collection                |
| AzureCosmosDbSubjectsCollectionId   | subjects               | The name of the collection in which subjects are uploaded to |

### Setup

### Pre-Setup

1) Install [.Net Core 2.2 SDK](https://dotnet.microsoft.com/download), if you haven't already.
2) Install python 3.6.8 - the latest stable version that works with Azure client.
```
Mac user:
Install homebrew:
1) /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
2) brew install sashkab/python/python36
3) pip3.6 install -U pip setuptools

Windows user:
```
3) Make sure Python 3.6.8 is set on your PATH, you can check this by running `python3 -v` in terminal window.
4) Install Azure Client
```
Mac user:
brew tap azure/functions
brew install azure-functions-core-tools

Windows user:
```
5) Setup Visual Studio Code, install [visual studio code](https://code.visualstudio.com/)
6) Also install the following extensions for visual studio code - documentation [here](https://code.visualstudio.com/docs/editor/extension-gallery)

```
Python
Azure CLI Tools
Azure Account
Azure Functions
Azure Storage
```

7) Sign into Azure with Visual Studio Code - follow documentation [here](https://docs.microsoft.com/en-us/azure/azure-functions/tutorial-vs-code-serverless-python#_sign-in-to-azure)

#### Building resources and running azure function locally

1) Create an azure search resource in azure portal, see Microsofts documentation [here](https://docs.microsoft.com/en-us/azure/search/search-create-service-portal)

2) Retrieve the azure search url and search api key from portal, (these will need to be added to you local.settings.json file)

3) Create/Reuse existing azure storage account, see Microsoft documentation [here](https://docs.microsoft.com/en-us/azure/storage/common/storage-quickstart-create-account?tabs=azure-portal)

4) Retrieve the azure storage account connection string and default endpoint, (these will need to be added to you local.settings.json file)

5) Create your local.settings.json file at root level of repository and include all environment variables in the configuration settings table above.

6) Create a Python virtual env to run the azure function application by running `venv .env` at root level of repository.

7) Run service on Python virtual env by doing the following:
```
source .env/bin/activate
pip install -r requirements.txt
func host start
```

8) Download latest csv stored against this repository or from Office for Students source (make sure it follows the same format as the example csv in here)

9) Upload csv to blob storage container

### Tests

To run tests, run the following command: `pytest -v`

### Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for details.

### License

See [LICENSE](LICENSE.md) for details.

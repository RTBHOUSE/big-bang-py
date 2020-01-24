# {{ cookiecutter.project_name }}

+ What is the project about?
+ Why is it needed?
+ How does it solve the problem?

## Links

* [Repository]()
* [Wiki]()
* [Prod deploy pipeline]()
* [Production server]()
* [GCP Project]()

## Setup

* Create `.env` file based on `.env.example`

## Development

There is a bunch of makefiles to ease developers life. You can get list of available commands with short descriptions using `make help`.

### Prerequisites

* Docker
* Docker Compose
* GNU Make

### Run dev server

`make up`

### Run linters

`make linters`

### Run tests 

`make tests`

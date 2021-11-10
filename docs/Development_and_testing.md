## Development and testing

### Start development server and make request

- Create new virtual environment
- Install dependencies `./scripts/install_deps.sh`
- Run migration: `./scripts/migrate.sh`
- Create super user `./scripts/create_user.sh`
- Start python server `./scripts/run_local.sh`
- Install [VScode rest client](https://github.com/Huachao/vscode-restclient)
- Open `restclient.http` file. Change username and password on the top of the file with the super user you created
- Using request inside `restclient.http`. Please change the request information to make the request succesfully

### Run unit test

- Run script `./scripts/run_local_test.sh`

Note: Scripts need to have execute permission

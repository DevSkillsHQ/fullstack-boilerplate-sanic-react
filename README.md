# Fullstack Boilerplate Sanic/React

A backbone for your coding challenge.

## Contents

- [Backend service](app-sanic) - a Sanic service with a `/ping` endpoint. Extend with your code.
- [Frontend app](app-react) - a React app. Extend with your code.
- [E2E test suites](cypress/e2e) - a backend and a frontend Cypress test suites. Extend with your tests.

## Tech Stack

- React
- Vite
- Vitest
- Python
- Sanic
- Cypress
- GitHub Actions

## Getting started

1. Make sure [`python3`](https://www.python.org/downloads/) and [`pip3`](https://pip.pypa.io/en/stable/installing/) are installed on your local env.

2. Make sure npm & node are configured on your local env. You can download those distributions for your platform [here](https://nodejs.org/en/download/)

3. Build your app.

```bash
npm install
npm run build # both Sanic backend and React frontend
npm run build:backend # only Sanic backend
npm run build:frontend # only React frontend
```

4. Start your app.

```bash
npm install
npm run start # both Sanic backend and React frontend
npm run start:backend # only Sanic backend
npm run start:frontend # only React frontend
```

5. Run the Cypress tests.

```bash
npm run test # run project tests under `cypress/e2e`
```

---

Authored by [Alva Labs](https://www.alvalabs.io/).

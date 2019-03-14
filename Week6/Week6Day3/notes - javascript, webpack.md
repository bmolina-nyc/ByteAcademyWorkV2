Webpack installation

- npm init - where you put details of a project. What are the names, keywords, enter. Will create your package.json
- npm install webpack --save-dev - creates a devDependency where webpack is the main dependency (core webpack component)
- npm install webpack-cli --save-dev - adding another devDependency (core webpack component)
- npm install webpack-dev-server --save-dev - added another devDependency (creating a development server)
- These three packages are the first things we need to bundle all your JS and code
- npm install html-webpack-plugin html-loader --save-dev - helps the program deal with HTML 
- npm install css-loader style-loader --save-dev

- babel  - compiles your new javascript into old version - npm install @babel/core babel-loader @babel/preset-env --save-dev
- create webpack.config.js - goes through the javascript files and says the specific file we're looking at. This file
lets the program know what to load etc
npm start - run on localhost
npm run build - if all is correctly built - a dist folder is built
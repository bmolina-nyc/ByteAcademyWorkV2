# Getting Started with Web Development

For UI development in this class, we will be creating HTML pages, using CSS styles and the Javascript language
to add functionality 

In order to setup a sample project we need to run through the following steps installing the different pieces of software as we go


## Environment Setup
All packages that we require for all UI development in this course will be installed using the Node Package Manager or npm

 * [NPM](https://docs.npmjs.com/about-npm-versions) is a package manager that easily allows you to download and install JS packages that you need
 * [NodeJS](https://nodejs.org/en/) Is a Javascript run time engine (think of it like the Python virtual machine) on which npm is built
 
A lot of Javascript tools for the command line are themselves written in Javascript, for which to run, needs a Javascript engine. Think of npm
like a java script command line tool, which runs on Node.

So as a first step, we'll need to install npm and node. To do so, it is recommended to use a Node version manager (like [NVMW](https://github.com/coreybutler/nvm-windows))
rather than manually downloading and installing them directly. Since npm and node are so deeply intertwined together using a version manager to install
or upgrade the two will save you a lot of trouble and headache.

Once you have these installed confirm the versions you have by running the following commands

```javascript 1.6
// NPM version 
npm -v

// Node version
node -v
```

## Initializing your project
Now that you've got your environment setup, lets start creating a web project. To do this, we'll be creating a new npm module of
our own. 

Let's kick off with the following command in a directory of your choice

```shell
// Create a minimal source directory for all your source files
mkdir src

// Create a new npm module using
npm init 
```

Click through all of the questions that are asked so you see what's involved in creating a typical npm package (Going forward you could
just run `npm init -y` to skip the boilerplate questions if you like)

This will create a basic project shell with a basic `package.json` file. 

*Note: All the following command line commands that we run, should be done at the root directory of the project. src is only when we 
start writing the source files*

Another thing to note is the creation of the `node_modules` directory. This is the directory in which every dependent npm package that you download will 
be copied to. Think of this directory as the web counterpart of the place that the python pip installer installs the downloaded python packages to.

### Package.json

[Package.json](https://docs.npmjs.com/files/package.json)

This is an important config file in your project that defines your project. The main things are
 * The name of your project
 * Any scripts that you want to run in your project
 * The versions of the dependent package that you use in your project
 * The versions of the packages that you use to develop your project but don't necessarily want to bundle them in the final output that you 
 deploy to a web server
 
 More information about this file can be found at the link above.
 
## Installing dev dependencies
There are two kinds of dependencies that you install while writing UI projects
 
  * Dependencies: These are the dependent libraries that your project needs to run, and will be bundled with the final output that is deployed
  to a web server. Your project will not be able to run without them. eg. React, D3, etc.
  * Dev Dependencies: These are the dependent libraries that you need to build your project. This includes compiling JS files, creating a dev server
  (if you choose to do so), etc. etc. These packages will most certainly not be included in your final deployment bundle. eg. webpack, babel, etc.
  
For now, we will not be using any particular dependent library for our introduction to the web. We will however need to install the following
dev dependencies so we can get up and running with a development setup to build our project

### Webpack
[Webpack](https://webpack.js.org/) is a powerful build tool that is used to compile and package your UI project. Essentially, when you
deploy your UI project to the server, you don't want to deploy each piece separately, like HTML files, JS files, CSS files, dependent libs etc.

Webpack is a tool that helps you create one big bundle file (deployable unit) out of your development code, so that deployment is easy. It also provides
useful tools like the webpack development server to use during development.

For our purposes we will install the following

```javascript
// The core webpack components
npm install webpack --save-dev

npm install webpack-cli --save-dev

// Utility tool that we use to create a development server
npm install webpack-dev-server --save-dev
```

Notice how your package.json has been automatically updated with entries for these two libraries in your devDependencies section. Let's make an additional
change to the file to set webpack as our build script, and the dev server as our development web server.

```javascript
"scripts": {
  "build": "webpack --mode production",
  "start": "webpack-dev-server"
}
```
Or if you already have a scripts section defined just add the build entry to it. This will allow you to run the command `npm run build` at the command line
which will then fire off webpack to build your project for production deployment.

This is the bare minimum that you need to start development. However for our purposes, we will go through the following other steps

### Babel
[Babel](https://babeljs.io/) is tool that we use to compile (or more correctly, *Transpile*) advanced versions of Javascript down to the raw
version that most browsers understand.

For our class, we will be using the ES6 standards, which defines several useful new features in the javascript language. However most browsers
do not natively support this version yet, so we need to use a tool like **Babel** that takes our ES6 JS file and transpile it automatically down
to the raw javascript version that a browser can run.

To install babel, run through the following commands in your terminal

```jshelllanguage
npm install @babel/core babel-loader @babel/preset-env --save-dev
```

We will now need to register our babel dependencies that we've pulled in to webpack. 

Webpack has a concept of [Loaders](https://webpack.js.org/loaders), which you can think of as transformers: They take an input and produce a different output. Babel,
as we've described above needs to take in Javascript files that we write in *ES6* and transform (*transpile*) them to raw Javascript. To get babel
to do this via webpack we need to configure babel and register the babel loader with webpack.

To do this, add a file called `webpack.config.js` to your project root directory with the following content

```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};
```

Several points I want to highlight here

 * The above is a configuration file that configures webpack. Notice how it is itself written in Javascript and is a .js file.
 * This config lets webpack know that all files in the project, except those in the node_modules directory, that match the test pattern (files that end with .js) should go through the 
 babel loader for transformation.
 
Babel will also separately need to be configured with a bunch of presets which we do by adding the `babel.rc` file to your project root directory

```javascript
{
  "presets": ["@babel/preset-env"]
}
```

### The HTML plugin
Ultimately to render anything in a browser we need to have an html page. To plug this in to the webpack setup, we will need to pull in the
[Html Webpack plugin](https://webpack.js.org/plugins/html-webpack-plugin/) and [Html loader](https://webpack.js.org/loaders/html-loader) like so

```jshelllanguage
npm install html-webpack-plugin html-loader --save-dev
```

And then update the webpack configuration with the following

```javascript
const HtmlWebPackPlugin = require("html-webpack-plugin");

const HtmlWebpackPluginConfig = new HtmlWebPackPlugin({
    template: './src/index.html',
    filename: './index.html',
    inject: 'body'
});

module.exports = {
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.html$/,
        use: [
          {
            loader: "html-loader"
          }
        ]
      }
    ]
  },
  plugins: [
    HtmlWebpackPluginConfig
  ]
};
```

This tells webpack to look for all .html files (via the test pattern specified) and run them through the html loader. It also sets up
the Html plugin letting it know where it would find the main .html file and where in that file it should inject any compiled and concantenated
deployable units (like injecting the script tag for transpiled .js files).


## Development

###HTML
Now we're ready to write some source code. To do so, create a file called index.html in the `src` directory of your project with the following content

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My First Web Page</title>
</head>
<body>
    <H1>Hello World!</H1>
</body>
</html>
``` 

### Javascript
To add functionality to our web pages i.e. to make them more than just static html pages that just allow you to view stuff, you would write logic
in javascript. By default webpack looks for a `index.js` file in the `src` directory as the main point of entry for your application.

To add some javascript and to illustrate how it can make your web pages dynamic and interactive add the following content to your `index.js` file

```javascript

function changeGreeting() {
    let greeting = "Goodbye"

    let elementsByTagName = document.getElementsByTagName("H1");

    elementsByTagName[0].textContent = greeting;
}

setTimeout(changeGreeting, 5000);
```
What we've done here is after 5 seconds call a function that would change the value of the first `H1` tag in your page.

### CSS
In web development, the styling of your web-page i.e. the layout of elements, the spacing between them, the coloring, the border and so on,
is done using **Cascading Style Sheets** or `CSS` files for short. These files contain rules that specify what style should be applied to which 
element. This is done by providing 
 * a selector in the rule -- which is used to determine what elements the style should be applied to
 * a value -- which states what style i.e. color, background, layout etc. to be applied to the selected element.
 
To get up and running with CSSs, we need to add them to our webpack ecosystem, which is done in the following steps.

Loader: Like the HTML, we need a webpack loader to be pulled in. Run the following command to pull in the css-loader and style-loader

```jshelllanguage
npm install css-loader style-loader --save-dev
``` 

The `css-loader` lets webpack know to go through all the css files in your project and concatenate it all into one giant string. 
The `style-loader` then tells webpack to put this style string into your main .html file (index.html) by inserting a `style` element
*Yes, webpack will automatically edit your source index.html to load in its compiled output*

Config: Once the loaders are pulled in, we need to add the rule for it in our webpack.config.js file to let webpack know the file pattern 
to apply these loaders to. To do this add the following Object literal to the ules array in the webpack.config.js file.

```javascript
{
    test:/\.css$/,
    use:['style-loader','css-loader']
}
```

CSS file: Once this is done, now lets create a sample css file to illustrate what css can do. Create a directory called `styles` under the `src`
directory and add a file called `app.css` in it. Fill that file with the following content.

```css
div {
    border: 1px solid orangered;
    padding:10px;
}
```
What we've done here is setup a style that applies to add `div` elements in your html files which will create a border of color
orangered and a padding of 10 pixels.

Inclusion: Finally, to include our css into our webpack build, we need to import it in our .js file to let webpack know thats where
our css dependency tree starts from. To do that add the following line at the top of your `index.js` file

```javascript
import './styles/app.css';
```

That's it ! Now your source files are created, you're ready now to run them and see some output.


### Running

To view these files during your development on a web browser, issue the following command at the command terminal

```jshelllanguage
npm run start
```

Remember how we added a `start` line to our `scripts` section of our `package.json` file ? That allows us to run the command `npm run start`. 
The scripts section allows you to package complex commands that you need into a simple one-liner for easy running.

Notice how when you run the command your get a bunch of compilation output in the terminal indicating that webpack has gone through all of its setup
config and invoked the various loaders to the final end product created and made available automatically through the dev web server.

Go ahead and make the following change to your `index.js` file to change the value of the greeting variable

```javascript
// In the changeGreeting function
let greeting = "Hello Again!"
```

Notice now when you go to the webpage, after 5 seconds it would automatically adjust to show you `Hello Again!`. No new browser window, no refresh, nothing !

As we carry on developing our code, we will keep adding to the src directory of your project. You can leave the webpack dev server running as you
develop. Notice that with every change you make to your source code, the dev server will automatically compile and transpile your files into a unit 
it then seamlessly streams on-the-fly to the browser. (UI development yay !!)


## Deployment

Finally, when you're ready to deploy your project to a web server for production deployment, all you need to do is issue the following command

```jshelllanguage
npm run build
```

And let webpack work its magic ! This will run the build script that we created in the package.json file. Give this a go, and see the additional `dist` 
directory that it creates automatically for you. If you look into that directory you'll see the .html and .js files 
that webpack has created by concatenating all your source files into just a couple of files.

## Rock n' Roll 
And that's it. We're up and running, ready to Rock n' Roll !
#DAY 1 - HTML & CSS: Basics 

### 1) index.html & index.css
[CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_variables)
- Below is the format for creating a CSS class within a CSS file
- `.one` is the name of the CSS variable and the content within the `{}` are the properties of a given variable
```
  .one {
    color: white;
    background-color: brown;
    margin: 10px;
    width: 50px;
    height: 50px;
    display: flex;
  }
```
- Using `*` in front of `{}` applies for entire document. in this example, every html tag will have pink background 
```
* {
    background-color: pink; 
}
```
- If there is no `.` before class, then you must use a specific html tag and those css properties will apply everytime that tag is used
- In this example, every `<label>` and `<input>` form will have the font-family Arial
```
label, input {
    font-family: Arial;
}
```

[CSS variable references](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)
- CSS variables have the following structure:
```
selectorlist {
  property: value;
  [more property:value; pairs]
}
```
- The following are examples of property: value pairs
```
    display: flex;
    padding: 10px;
    margin: 10px 5px;
    width: 75%
```

[HTML Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)
- Some commonly used HTML elements include: 
- `<div>, <head>, <body>, <main>, <h1>, <p>, <form>, <input>`

[link - stylesheets](https://matthewjamestaylor.com/add-css-to-html)
- You can easily add a static CSS file to an HTML file by inserting a `<link>` tag in between the `<head>` tags
```
<head>
    <link rel="stylesheet" type="text/css" href="index.css" />
</head>
```

[Add class to html element](https://developer.mozilla.org/en-US/docs/Web/CSS/Class_selectors)
- Below is the synatx you have to use to apply a given css class to an HTML elemtn 
```
<div class="column">
    <h2>Column</h2>
</div>
```

[Creating hyperlinks](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks)
- Below is the syntax for adding link to an HTML tag 
```
<p>I'm creating a link to
    <a href="https://www.mozilla.org/en-US/">the Mozilla homepage</a>.
</p>
```

[Inline CSS style vs separate file](https://stackoverflow.com/questions/8284365/external-css-vs-inline-style-performance-difference)
- Instead of adding a CSS file separately, you can add CSS inline by adding 'style' to an HTML element 
```
<p style="color:blue;font-size:46px;">
    I'm a big, blue, <strong>strong</strong> paragraph
</p>
```

[CSS psuedo class](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)
- A pseudo-class is a keyword added to a selector that specifies a special state of the selected elements
- For example, `:hover` can be used to change a button's color when the user's pointer hovers over it
```
/* Any button over which the user's pointer is hovering will turn blue*/

button:hover {
  color: blue;
}
```

[Media Query Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries)
[How to use Media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/@media)
- Media queries let you adapt your site or app depending on the presence or value of various device characteristics and parameters.
- They are a key component of responsive design. For example, a media query can shrink the font size on small devices, increase the padding between paragraphs when a page is viewed in portrait mode, or bump up the size of buttons on touchscreens.

```
/* In its current state, the CSS class of column only takes up 33% of the page width */
.column {
    flex: 33.33%;
    padding: 15px;
}

Responsive layout - makes the three columns stack on top of each other instead of
next to each other once the pixels of the page go below 600px
@media screen and (max-width:600px) {
    .column {
      width: 100%;
    }
}

```



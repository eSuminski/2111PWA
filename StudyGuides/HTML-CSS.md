# HTML & CSS
### Minimum HTML Requirements
```html
<!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Example HTML</title>
        </head>
        <body>

        </body>
    </html>
```
### Elements & Attributes
Elements are the content of your web page, and they are created by using tags (see above). Attributes are attached to elements and can be used to identify and/or add functionality to your elements
```html
<div id="container" onclick="alert('message')"></div>
```
### Cascading Style Sheet
CSS is how you apply styling to your html. There are many different selectors you can use to apply styling to elements, and there are different places to place your styling information:
- inline styling is where you plce style information directly in the element via the style attribute
- internal styling is where you create a style element inside the head element and place styling information via CSS selectors
- external styling is the same as internal, except you use a link element and reference your css file

check the external styling css file in Week 4 day2 to see a list of selectors and the order of priority
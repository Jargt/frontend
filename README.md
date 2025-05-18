# frontend
A markdown to HTML converter - a Boot.dev project


Just used this as a dumping ground for the syntax used and useful info:

An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes

<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

<p>This is a paragraph of text.</p>
This is a paragraph of text.

<p>This is a <b>bold</b> word.</p>
This is a **bold** word.

<p>This is an <i>italic</i> word.</p>
This is an _italic_ word.
This is an *italic* word.

This is a paragraph with a <a href="https://www.google.com">link</a>.
This is a paragraph with a [link](https://www.google.com).

<img src="url/of/image.jpg" alt="Description of image" />
![alt text for image](url/of/image.jpg)

<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
- Item 1
- Item 2
- Item 3

<ol>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ol>
1. Item 1
2. Item 2
3. Item 3

<blockquote>This is a quote.</blockquote>
> This is a quote.

<code>This is code</code>
`This is code`
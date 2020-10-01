# milena-and-her-dog ![[Build Status]](https://github.com/naschidaniel/milena-and-her-dog/workflows/release%20on%20GH-Pages/badge.svg)

A simple blog, created with the Static Site Generator [Pelican](https://getpelican.com/). In section [CHANGELOG](#CHANGELOG) the already implemented parts of the websites are listed. The blog is built with [github actions](https://docs.github.com/en/actions). The build of the website is provided via [github pages](https://pages.github.com/).


## Installation

To run the project locally, python version 3.7+ and node version v12.18.3+ are required. Use the following commands and you are ready to go. Details about the required dependencies can be found in the [Contributing Guide](./CONTRIBUTING.md).

```
pip install -r requirements.txt
npm install
```


### Compiles and hot-reloads for development

Pelican includes an integrated development server (`invoke livereload`), after the local start the website is available at [http://localhost:8000/](http://localhost:8000/). The following command also creates the required tailwindcss style files. 

```
invoke development
```


### Template and Design 

A website should never exist twice on the web. Feel free to edit the template in the folder `./themes/milena/` the way you like it. Pelican uses [JINA2](https://jinja.palletsprojects.com/) as default template language. For the styling and the UI interface [tailwindcss](https://tailwindcss.com/) is used.

Any other theme can also be used for this website. For more information, please refer to the Pelican documentation. 

If basic settings are changed in Tailwindcss, the main.css file for the development environment must be recreated.

```
invoke npm-dev
```


### Compiles for a preview on Localhost production

The generated files are provided in the `./output` folder.

```
invoke preview
```

### Compiles for production

A different settings file is used for publishing. The required settings can be made in the file `publishconf.py`.

```
invoke publish
```


## How to post blog entries

Nothing easier than that. Create a markdown file in the folder `./content/blog`. The name of the file corresponds to the `slug` of the blog post. 
The required images are stored in `./content/images/` with the corresponding `slug` as folder name. 

### Blog Entry

For blog entries this template can be used.

```
Title:
Subtitle:
Date: YYYY-MM-DD HH:MM
Mainimage: /images/{slug}/{filename}
Mainimagealttext: 
text:
Tags:
Category:
Slug:
Author:
Summary:


Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

![{alt text description}](/images/{slug}/{imagename}.jpg) 

## H2 headline
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.


### H3 headline slider for portrait photos
[start-milena-img-show]
  ![{alt text description}](/images/{slug}/{imagename}.jpg) 
  ![{alt text description}](/images/{slug}/{imagename}.jpg) 
[end-milena-img-show]
```

### Friedas Quotes

For blog entries this template can be used.

```
Title:
Subtitle:
Date: YYYY-MM-DD HH:MM
Mainimage: /images/{slug}/{filename}
Mainimagealttext:
text:
Slug: friedas-zitat-{slug}
Type: quote
```

## Contribution and Pull Requests

Please make sure to read the [Contributing Guide](./CONTRIBUTING.md) before making a pull request.


## Changelog

- 2020-09-26 Active links are marked
- 2020-09-26 A custom JINJA 2 filter for a simple image slider was added 
- 2020-09-23 Image compression with [imagemin](https://github.com/imagemin/imagemin)
- 2020-09-22 Integration of GitHub actions and publish on GH-PAGES
- 2020-09-21 Migration of old blog articles and pages from djangoVue
- 2020-09-20 The last commit hash is used as version number for main.js and main.css.
- 2020-09-20 Bundle css and js for production with webpack
- 2020-09-19 Add tailwindcss and webpack
- 2020-09-18 Improve Pelican Settings
- 2020-09-17 Init Repository



## License

[GPL-3.0](./LICENSE)

Copyright (c) 2020-present, Daniel Naschberger

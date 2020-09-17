# milena-and-her-dog

A simple blog, created with the Static Site Generator [Pelican](https://getpelican.com/). In section [CHANGELOG](#CHANGELOG) the already implemented parts of the websites are listed.



## Installation

To run the project locally, python version 3.6+ is required. Use the following commands and you are ready to go.

```
pip install "pelican[markdown]"
```


### Compiles and hot-reloads for development

Pelican includes an integrated development server, after the local start the website is available at [http://localhost:8000/](http://localhost:8000/).

```
pelican --listen
```

### Template and Design 

A website should never exist twice on the web. Feel free to edit the template in the folder `./themes/milena/` the way you like it. Pelican uses [JINA2](https://jinja.palletsprojects.com/) as default template language. For the styling and the UI interface [tailwindcss](https://tailwindcss.com/) is used.

Any other theme can also be used for this website. For more information, please refer to the Pelican documentation.

### Compiles for production

The generated files are provided in the `./output` folder.

```
pelican content
```


## Contribution

Please make sure to read the [Contributing Guide](./CONTRIBUTING.md) before making a pull request.



## Changelog

- 2020-09-17 Init Repository



## License

[GPL-3.0](./LICENSE)

Copyright (c) 2020-present, Daniel Naschberger
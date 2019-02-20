# How to contribute

This [glossary][repo] is an open-source project, and we welcome contributions of all kinds,
be them new material, corrections or improvements to existing material.
You are also more than welcome to participate in the reviews of pull requests.

By contributing, you are agreeing that we may redistribute your work under [CC-BY-4.0][license].


## Getting Started

1.  We use the [fork and pull][gh-fork-pull] model to manage changes. More information
    about [forking a repository][gh-fork] and [making a Pull Request][gh-pull].

2. You should branch from and submit pull requests against the `master` branch.

3. The glossary is homogeneous in its writing. Please use the following template when writing new entries:

   ```markdown

   ## TERM: The Expanded Real Meaning {#TERM}

   Text.
   ```

   There should be two `##`, followed by the definition. If this expands to something,
   you should add that in the same line after a colon, and then put a `{#hyperlink}` to just the unexpanded term.
   
   If you link to another page, please use the format `[TERM](t.md#TERM)` to make the link (and on the same page the page name is not needed). This should work in both the final webpage and locally on GitHub.

4.  Please install the [dependencies](#dependencies) if you want to build the glossary locally.


## Dependencies

To build the glossary locally, install the following:

1. [Gitbook](https://github.com/GitbookIO/gitbook/blob/master/docs/setup.md)

Install the Gitbook plugins:

```shell
$ gitbook install
```

Then (from the top `glossary` directory) build the pages and start a web server to host them:

```shell
$ gitbook serve
```
You can see your local version by using a web browser to navigate to `http://localhost:4000` or wherever it says it's serving the book.


[repo]: https://github.com/lhcb/glossary
[license]: LICENSE.md
[gh-fork-pull]: https://help.github.com/articles/using-pull-requests/#fork--pull
[gh-fork]: https://help.github.com/articles/fork-a-repo/
[gh-pull]: https://help.github.com/articles/using-pull-requests/


<!---
Friends of Glossary can use this:
              {"pattern": "«([^»^:])([^»^:]+)»", "flags": "g", "substitute": "[$1$2](https://lhcb.github.io/glossary/glossary/$1.html#$1$2)"},
              {"pattern": "«([^»]+):([^»^:])([^»^:]+)»", "flags": "g", "substitute": "[$1](https://lhcb.github.io/glossary/glossary/$2.html#$2$3)"}
--->

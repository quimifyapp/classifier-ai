![inorganic.png](doc/classifier.png?raw=true "Flowchart")

### About `data/split.sh`:

When you run it, it will create the following directory tree inside `split`:

* `formula-name`
    * `train`
        * `formula`
        * `name`
    * `test`
        * `formula`
        * `name`
* `formula-inorganic-organic`
    * `train`
        * `inorganic`
        * `organic`
    * `test`
        * ...
* `name-inorganic-organic`
    * `train`
        * ...
    * `test`
        * ...

Then, it will split the data read from `source` into single-line files and place them inside the final directories.

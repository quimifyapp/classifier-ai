# What does it

When you run it, it will create a folder `data-model` for example,
and 3 more inside.

* data-model
  * formula-inorganic-organic
  * formula-name
  * name-inorganic-organic

And inside each of the folders it will create more folders
to store the data.

* train
  * label 1
    * data... 
  * label 2
    * data...
* test
  * label 1
    * data...
  * label 2
    * data...


# How does it work

To run it

```bash 
bash script.sh
```

By default, the destination folder is `data-model/` 
but you can change it sending it by parameters.

```bash
bash script.sh myfolder/
```

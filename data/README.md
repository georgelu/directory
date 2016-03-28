
# Raw
- food-neighborhood.pdf downloaded from http://www.211sacramento.org/211/online-database/categories/food/ at bottom of page
http://www.211sacramento.org/211/wp-content/uploads/food-neighborhood.pdf

Metadata

```coffee
{
  "version": ["1.5"],
  "pages": [7],
  "encrypted": [false],
  "linearized": [false],
  "keys": {
    "Author": ["Patrick Becknell"],
    "Producer": ["Microsoft® Excel® 2010"],
    "Creator": ["Microsoft® Excel® 2010"]
  },
  "created": ["2016-01-21 15:50:47"],
  "modified": ["2016-01-21 15:50:47"],
  "metadata": [""],
  "locked": [false],
  "attachments": [false],
  "layout": ["no_layout"]
}
```

# Processed

The pdf was processed using [tabula](http://tabula.technology/)
to csv

- tabula-food-neighborhood.csv

Note: tabula-food-neighborhood.json also contains some metadata.

A Makefile removes CR `\r` line endings from the tabula output to produce

- food-neighborhood.csv

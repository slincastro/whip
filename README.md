# Whip

obtain metrics about commits to improve the flow of development

## Configuration
* in App_config update :

` dataSource: some/folder/toStore/json/objects`
` projects:`
  `- project:`
      `type : <used as metadata>`
      `name : <used as name of the project>`
      `path : path/of/the/repository/to/analyce`

## Run app

> `source venv/bin/activate`
> `python main.py`


## Troubleshooting
### Set Permisions

> `chmod +x the_file_name`

## Run Test

> `python -m unittest`
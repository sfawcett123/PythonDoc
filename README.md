# AI Simple Search

## Development

```
# Set up environment
python -m venv .
source bin/activate
```

## Running the Application

when running the first time you need to inititalise the AI stuff
```
python -m spacy download en_core_web_sm
```

```
flask --app aisearch run --debug
```

go to url: [Home](http://127.0.0.1:5000/)

	
## To Do

- Add a save button to save the indexes,
- Figure out a fast method to add and remove files from Indexes.
- Implement the actual search, using keywords from Language support
- Remove Debugging messages
- Implement a. method to read and index files:
	- PDF
	- Word
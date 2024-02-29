# ChatLEA
A chatbot for the 2024 local elections in Waterford City &amp; County

This is a personal project to explore ChatGPT and it's applications. The intention is to pull together a local knowledgebase specific to the 2024 elections in Waterford, Ireland and use OpenAI's API to allow users engage with the topic in everyday language.

The knowledgebase will include broad information around local government and elections from citizensinformation.ie, local authority data from waterfordcouncil.ie and information about individual candidates from political party and candidate websites, and local media. All training data in /data.

## Status
- [x] Scope
- [x] Build and test scraper
- [x] Scrape non candidate data
- [x] Data Transformation
- [x] Data Embedding
- [ ] Questioning
- [ ] Candidate Data Addition
- [ ] Frontend
- [ ] Beta

## Files

### Scraper.py
A simple multi page text scraper used to get and store background government and election information from citizensinformation.ie and waterfordcouncil.ie

### Embedding.py
Reads a CSV into a dataframe and generates embedding for each row

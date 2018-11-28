# Brill's POS Tagger for Hindi

## A simple rule based POS tagger made for Hindi on the same lines as Brill's tagger for Hindi

### Important Files

> - process.py
> The heart of the tagging process. It cointains the rules. The search function serves as the api to the tagger and returns the pos of the entire sentence as return
> - test_hindi.py
> The driver function which read the development data as test data to process.py
> - test_hindi_[num].txt
> The resultant test files with the outputs
> - makefiles.py
> To convert the annotated data to the 
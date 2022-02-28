# Second Task
## Requirements
- Develop the first server for signing xml documents.
- Develop the second server for asking to sign xml document.
- Design both server using Python and its framework Flask.
- Code for Flask app should be generated using from Swagger. 

## API 
APIs were developed in Swagger and then exported as a `.yml` file. 
### Signer
Signer is a server for signing xml document. There are two endpoints: `/user` and `/document`. Both of them have only 1 method to interact with - `POST`. 

- POST `/user` is a method used for creating a new user. A request body has following structure:
```
<?xml version="1.0" encoding="UTF-8"?>
<User>
	<email>string</email>
	<password>string</password>
</User>
```
Status codes: `201` - Success, `400` - User already exists.

- POST `/document` is a method for used for signing xml document. A request body has following structure:
```
<?xml version="1.0" encoding="UTF-8"?>
<Document>
	<doc>string</doc>
	<email>string</email>
	<password>string</password>
</Document>
```
Status codes: `200` - Success, `404` - Wrong credentials.
Response body in case of success:
```
<?xml version="1.0" encoding="UTF-8"?>
<Document_signed>
	<doc>string</doc>
	<sign>string</sign>
</Document_signed>
```
### Requester
Requester is a server that asks signer to sign document. There are two endpoints: `/register` and `/request` with one `POST` method in each. These endpoints have almost the same body as in signer. 

## Description
The signer can issue a signature only to a registered user. For this reason before signing user send his email and password using xml request. Signer can't register the same email twice. For each registered user generates id using python `uuid` package. This id is used for signing later. 

To sign a document received in xml request signer does next: xml body is converted into string, then signer takes existing user id and concatanates them together. This string is hashed using `sha256` algorithm. Resulting string is document signature. After that signer responds with xml containing document and its signature. In case user doesn't exist or password is wrong document won't be signed.

Requester has similar methods' bodies as signer. To make a request from requester we use `requests` python package.

Flask code is generated using python `swagger-py-codegen` package wit command `swagger_py_codegen --swagger-doc <api.yml> <api name>`. It is used `sqlite3` to store user data. Both servers are not deployed in web.

## Vizualisation

# Welcome to ChuckJokesAPI!

You received this information file since:

- you send a GET request to: /chuckjokesapi/v0/help

or

- the endpoint you are reaching for does not exist.

**ChuckJokesAPI** is a custom service app that allows you to interact with 'Chuck Norris Jokes Api'.

## 🧩 Development information

The App was developed and implemented as a test for Coloca Payments. It exposes an API that lets users interact with it.

_Developer:_ Martín E. Pérez Segura  
_Date_: May 2024.

## 🔗 API Reference:

The base URL ( {{baseURL}} ) for accessing all endpoints is: http://localhost:8000/chuckjokesapi/v0

Here is some information about the enpoints and how to use them:

#### Get random joke

Get a random joke from an external API or the local DataBase.

```http
  GET /jokes
```

The source from which the jokes is obtained is controlled by query parameters:

| Parameter | Type     | Description                                         |
| :-------- | :------- | :-------------------------------------------------- |
| `source`  | `string` | **Optional**. If "Chuck" gets from the external API |
| `source`  | `string` | **Optional**. If \*empty gets from the DataBase     |

##### Example:

Request from external API:

```http
GET /chuckjokesapi/v0/jokes?source=Chuck
```

Request from DataBase:

```http
GET /chuckjokesapi/v0/jokes
```

#### Post new joke

Add a new joke to the DataBase.

```http
  POST /jokes
```

Parameters for Request Body:

| Parameter | Type     | Description               |
| :-------- | :------- | :------------------------ |
| `joke`    | `string` | **Required**. Joke to add |

If further parameters are sent they will be ignored. Once stored each joke will be given a number for identification.

##### Example:

Request body example:

{ "joke" : "Chuck Norris can slice fries with his beard. He then stares at them until they are Golden Brown." }

#### Update joke

Update a joke in the DataBase.

```http
  PATCH /jokes
```

Parameters for Request Body:

| Parameter     | Type      | Description                       |
| :------------ | :-------- | :-------------------------------- |
| `joke number` | `integer` | **Required**. Joke number         |
| `joke`        | `string`  | **Required**. Joke text to update |

If further parameters are sent they will be ignored.

##### Example:

Request body example:

{ "joke number" : 3, joke" : "Chuck Norris can slice fries with his beard. He then stares at them until they are Golden Brown." }

#### Delete random joke

Delete a joke from the DataBase.

```http
  DELETE /jokes
```

The joke to delete is identified by its number:

| Parameter     | Type     | Description                                |
| :------------ | :------- | :----------------------------------------- |
| `joke_number` | `string` | **Required**. Number of the joke to delete |

##### Example:

Delete joke number 3:

```http
DELETE /chuckjokesapi/v0/jokes?joke_number=3
```

## ⚙ MISC

If you find API issues or bugs when testing, please create a ticket or inform to a member of the development team. 🔍 If you have any questions or suggestions, please don't hesitate to reach out.
